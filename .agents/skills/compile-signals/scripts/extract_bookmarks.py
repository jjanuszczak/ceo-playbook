import argparse
import datetime
import json
import os
import time
from DrissionPage import ChromiumPage, ChromiumOptions

PROFILE_DIR = os.path.expanduser("~") + "/.drission_chrome_profile"

def scrape_hydrated_page(page, url):
    """Navigates to a single tweet/article page and extracts fully rendered content."""
    try:
        print(f" -> Hydrating: {url}")
        page.get(url)
        
        # Give the page assets an extra moment to fully hydrate
        time.sleep(2.5)

        # Locate the core post container to isolate our search away from sidebars/comments
        main_tweet = page.ele('@data-testid=tweet', timeout=3)
        
        text_content = ""
        # Base classification from URL routing
        is_article = "/article/" in url and "/status/" not in url
        
        if main_tweet:
            # 1. Try extracting standard Tweet text content
            text_elem = main_tweet.ele('@data-testid=tweetText', timeout=0)
            if text_elem:
                text_content = text_elem.text
            
            # 2. Card Fallback: Look for rich preview card structures (Common for embedded X Articles)
            if not text_content:
                card_elem = main_tweet.ele('@data-testid=card.wrapper', timeout=0)
                if not card_elem:
                    card_elem = main_tweet.ele('[data-testid*="Card"]', timeout=0)
                
                if card_elem:
                    text_content = card_elem.text
            
            # 3. Ultimate Safety Fallback: Extract the entire text layer of the tweet container
            if not text_content:
                text_content = main_tweet.text
                
            # 4. Adaptive Type Check: If an "Article" badge is visible inside the post,
            # and it lacks standard tweet text, dynamically reclassify it as an Article.
            if "Article" in main_tweet.text and not main_tweet.ele('@data-testid=tweetText', timeout=0):
                is_article = True
        else:
            # Fallback if X routes to a pure full-screen standalone article view
            article_body = page.ele('tag:article', timeout=2)
            if article_body:
                text_content = article_body.text
                is_article = True

        # Extract Author Handle (URL slice approach is fastest and most reliable)
        handle = "Unknown"
        if "/status/" in url:
            try:
                handle = f"@{url.split('x.com/')[1].split('/')[0]}"
            except Exception:
                pass
                
        if handle == "Unknown" and main_tweet:
            user_name_container = main_tweet.ele('@data-testid=User-Name', timeout=0)
            if user_name_container:
                handle_span = user_name_container.ele('xpath:.//span[contains(text(), "@")]', timeout=0)
                if handle_span:
                    handle = handle_span.text

        # Extract Image URL (Scoped within main_tweet to avoid sidebar/ad pollution)
        image_url = None
        if main_tweet:
            card_media = main_tweet.ele('xpath:.//*[contains(@data-testid, "card.layout")]//img', timeout=0)
            if card_media:
                image_url = card_media.attr('src')
                
            if not image_url:
                image_elem = main_tweet.ele('@data-testid=tweetPhoto', timeout=0)
                if image_elem:
                    img_tag = image_elem.ele('tag:img', timeout=0)
                    image_url = img_tag.attr('src') if img_tag else None

            if not image_url:
                all_imgs = main_tweet.eles('tag:img')
                for img in all_imgs:
                    src = img.attr('src')
                    if src and not any(x in src for x in ["profile_images", "abs.twimg.com", "emoji"]):
                        image_url = src
                        break

        # Extract Timestamp
        time_elem = page.ele('tag:time', timeout=1)
        timestamp_str = time_elem.attr('datetime') if time_elem else None
        timestamp = datetime.datetime.fromisoformat(timestamp_str.replace("Z", "+00:00")) if timestamp_str else None

        return {
            "author_handle": handle,
            "type": "Article" if is_article else "Tweet",
            "text": text_content.strip(),
            "image_url": image_url,
            "timestamp": timestamp
        }
    except Exception as e:
        print(f"    x Error scraping individual page: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Extract recent X Bookmarks using Two-Pass Hydration.")
    parser.add_argument("--limit", type=int, default=5, help="Number of bookmarks to fetch")
    args = parser.parse_args()

    limit = max(1, min(args.limit, 15))
    print(f"Targeting {limit} unique bookmarks...")

    options = ChromiumOptions()
    options.set_user_data_path(PROFILE_DIR)
    page = ChromiumPage(options)
    
    print("Navigating to bookmarks timeline...")
    page.get("https://x.com/i/bookmarks")
    
    print("Waiting for page to load timeline...")
    page.ele('@data-testid=tweet', timeout=30)
    
    # ----------------------------------------------------
    # PASS 1: COLLECT TARGET URLS FROM THE TIMELINE
    # ----------------------------------------------------
    print("\n--- Pass 1: Collecting Bookmark Links ---")
    target_urls = []
    consecutive_no_change = 0
    
    while len(target_urls) < limit and consecutive_no_change < 5:
        initial_count = len(target_urls)
        tweet_elements = page.eles('@data-testid=tweet')
        
        for elem in tweet_elements:
            # Captures both standard status targets and pure article routing targets
            link_elem = elem.ele('xpath:.//a[contains(@href, "/status/") or contains(@href, "/article/")]', timeout=0)
            if link_elem:
                raw_url = link_elem.attr('href')
                clean_url = raw_url.split("?")[0] if "?" in raw_url else raw_url
                if clean_url not in target_urls:
                    target_urls.append(clean_url)
                    if len(target_urls) >= limit:
                        break
                        
        if len(target_urls) == initial_count:
            consecutive_no_change += 1
        else:
            consecutive_no_change = 0
            
        page.scroll.down(800)
        time.sleep(1.5)
        
    target_urls = target_urls[:limit]
    print(f"Found {len(target_urls)} bookmark target links. Starting deep scraping...")

    # ----------------------------------------------------
    # PASS 2: VISIT EACH URL INDIVIDUALLY FOR CLEAN DATA
    # ----------------------------------------------------
    print("\n--- Pass 2: Deep Scraping Pages ---")
    final_bookmarks = []
    
    for url in target_urls:
        tweet_id = url.split("/status/")[-1] if "/status/" in url else url.split("/")[-1]
        
        parsed_data = scrape_hydrated_page(page, url)
        if parsed_data:
            parsed_data["tweet_id"] = tweet_id
            parsed_data["url"] = url
            if parsed_data["timestamp"]:
                parsed_data["timestamp"] = parsed_data["timestamp"].isoformat()
            final_bookmarks.append(parsed_data)
            
    print(f"\nSuccessfully extracted {len(final_bookmarks)} bookmarks.")
    print(json.dumps(final_bookmarks, indent=2))

if __name__ == "__main__":
    print("Start")
    main()