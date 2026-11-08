import os
import ssl
import urllib.request
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def create_quote_card(output_path, quote_text, book_title, book_author, cover_url, bg_color=(245, 239, 235)):
    # Canvas size: 1100 x 618
    width, height = 1100, 618
    canvas = Image.new("RGBA", (width, height), (*bg_color, 255))
    draw = ImageDraw.Draw(canvas)

    # Fonts
    font_quote_path = "/System/Library/Fonts/Supplemental/Georgia.ttf"
    font_meta_path = "/System/Library/Fonts/Helvetica.ttc"
    
    font_size_quote = 30
    if len(quote_text) > 200:
        font_size_quote = 25
    elif len(quote_text) < 100:
        font_size_quote = 36

    font_quote = ImageFont.truetype(font_quote_path, font_size_quote)
    font_title = ImageFont.truetype(font_meta_path, 20)
    font_author = ImageFont.truetype(font_meta_path, 16)

    # Text wrapping for quote
    # Available width for text on left side: ~650px (x from 80 to 730)
    max_text_width = 650
    words = quote_text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font_quote)
        line_w = bbox[2] - bbox[0]
        if line_w <= max_text_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))

    # Calculate text height
    line_spacing = int(font_size_quote * 1.45)
    total_quote_height = len(lines) * line_spacing
    
    # Starting Y position (centered vertically somewhat)
    start_y = max(80, (height - total_quote_height - 120) // 2)

    # Draw vertical accent bar
    bar_x = 36
    bar_w = 12
    bar_y_start = start_y
    bar_y_end = start_y + total_quote_height
    draw.rectangle([bar_x, bar_y_start, bar_x + bar_w, bar_y_end], fill=(33, 33, 33, 255))

    # Draw quote lines
    text_x = 75
    y = start_y
    for line in lines:
        draw.text((text_x, y), line, font=font_quote, fill=(33, 33, 33, 255))
        y += line_spacing

    # Draw Title and Author below quote
    meta_y = y + 40
    # Clean/shorten title if too long
    display_title = book_title.split(":")[0] if len(book_title) > 40 else book_title
    draw.text((text_x, meta_y), display_title, font=font_title, fill=(50, 50, 50, 255))
    draw.text((text_x, meta_y + 28), book_author, font=font_author, fill=(80, 80, 80, 255))

    # Download and process book cover
    try:
        req = urllib.request.Request(cover_url, headers={"User-Agent": "Mozilla/5.0"})
        ctx = ssl._create_unverified_context()
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            cover_img = Image.open(BytesIO(resp.read())).convert("RGBA")
        
        # Scale cover image to height ~ 500
        target_h = 500
        target_w = int(cover_img.width * (target_h / cover_img.height))
        cover_resized = cover_img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        
        # Rotate cover slightly (-6 degrees)
        cover_rotated = cover_resized.rotate(6, expand=True, resample=Image.Resampling.BICUBIC)
        
        # Paste cover on the right side
        cover_x = width - cover_rotated.width + 60
        cover_y = (height - cover_rotated.height) // 2 - 20
        canvas.paste(cover_rotated, (cover_x, cover_y), cover_rotated)
    except Exception as e:
        print(f"Failed to process cover for {book_title}: {e}")

    # Convert to RGB and save
    final_img = canvas.convert("RGB")
    final_img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    out_dir = "content/signals/signals-week-45-2026"
    items = [
        {
            "filename": "segre.png",
            "title": "Ordinary Geniuses",
            "author": "Gino Segre",
            "quote": "“evolution stumbles upon solutions to problems by trying many avenues and is then quick to exploit them.”",
            "cover": "https://m.media-amazon.com/images/I/51Xco91bCwL._SL500_.jpg",
            "bg": (245, 239, 235)
        },
        {
            "filename": "lewis.png",
            "title": "Going Infinite",
            "author": "Michael Lewis",
            "quote": "“When people wanted to bet—or trade—with you, there was usually a reason: they knew something you did not.”",
            "cover": "https://m.media-amazon.com/images/I/61-8DTXRjdL._SL500_.jpg",
            "bg": (242, 237, 230)
        },
        {
            "filename": "forsgren.png",
            "title": "Accelerate",
            "author": "Nicole Forsgren PhD, Jez Humble, Gene Kim",
            "quote": "“In short, approval by an external body (such as a manager or CAB) simply doesn’t work to increase the stability of production systems, measured by the time to restore service and change fail rate.”",
            "cover": "https://images-na.ssl-images-amazon.com/images/I/41YpWJi9OoL._SL500_.jpg",
            "bg": (247, 242, 235)
        }
    ]

    for item in items:
        path = os.path.join(out_dir, item["filename"])
        create_quote_card(path, item["quote"], item["title"], item["author"], item["cover"], item["bg"])
