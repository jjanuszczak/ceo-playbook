import os
import json
import random
import requests
from datetime import datetime
from dotenv import load_dotenv
from html.parser import HTMLParser

# Load variables from the .env file into the system environment
load_dotenv()

# Configuration
READWISE_TOKEN = os.getenv("READWISE_TOKEN")

# Fallback pattern (highly recommended)
# os.getenv returns None if the key doesn't exist
if not READWISE_TOKEN:
    raise ValueError("API token missing! Check your environment or .env file.")

HEADERS = {
    "Authorization": f"Token {READWISE_TOKEN}",
    "Content-Type": "application/json"
}

# ==========================================
# ZERO-DEPENDENCY HTML PLAIN-TEXT EXTRACTOR
# ==========================================

class HTMLTextExtractor(HTMLParser):
    """Parses structural HTML and extracts clean, human-readable plain text."""
    def __init__(self):
        super().__init__()
        self.result = []
        # Structural HTML tags that imply a line break or content separation
        self.block_tags = {'p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'br', 'article', 'section'}

    def handle_starttag(self, tag, attrs):
        if tag in self.block_tags:
            self.result.append('\n')

    def handle_endtag(self, tag):
        if tag in self.block_tags:
            self.result.append('\n')

    def handle_data(self, data):
        self.result.append(data)

    def get_text(self) -> str:
        raw_text = "".join(self.result)
        # Strip trailing whitespaces and remove excessive empty padding gaps
        lines = [line.strip() for line in raw_text.splitlines()]
        return "\n".join([line for line in lines if line])

def clean_html_to_text(html_string: str) -> str:
    """Helper wrapper to cleanly translate document HTML to formatted text."""
    if not html_string:
        return ""
    parser = HTMLTextExtractor()
    parser.feed(html_string)
    return parser.get_text()


# ==========================================
# READWISE READER API (v3) - DOCUMENTS
# ==========================================

def readwise_list_documents(location: str, page_size: int = 50) -> list:
    """Fetches a list of documents from Readwise Reader API v3 for a specific location."""
    url = "https://readwise.io/api/v3/list/"
    params = {
        "location": location,
        "limit": page_size,
        "withHtmlContent": "true"  # ENHANCEMENT 1: Instruct API to include the full raw source HTML
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.exceptions.RequestException:
        return []

def get_recent_library_documents(limit: int = 5) -> list:
    """Aggregates, parses, and returns the most recent documents across Library states."""
    target_locations = ["new", "later", "shortlist"]
    all_docs = []

    for loc in target_locations:
        docs = readwise_list_documents(location=loc, page_size=20)
        all_docs.extend(docs)

    # Sort documents by creation date descending
    all_docs.sort(key=lambda doc: doc.get("created_at", ""), reverse=True)
    selected_docs = all_docs[:limit]

    formatted_docs = []
    for doc in selected_docs:
        # ENHANCEMENT 1: Hydrate plain text by extracting strings out of the returned markup
        raw_html = doc.get("html_content", "")
        plain_text = clean_html_to_text(raw_html)

        formatted_docs.append({
            "title": doc.get("title"),
            "author": doc.get("author"),
            "location": doc.get("location"),
            "url": doc.get("url") or doc.get("source_url"),
            "created_at": doc.get("created_at"),
            "document_text": plain_text  # Document text payload added here
        })

    return formatted_docs


# ==========================================
# READWISE API (v2) - BOOKS & HIGHLIGHTS
# ==========================================

def readwise_list_books(page_size: int = 200) -> list:
    """Fetches a list of categorized sources (books) from Readwise API v2."""
    url = "https://readwise.io/api/v2/books/"
    params = {
        "category": "books",
        "page_size": page_size
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.exceptions.RequestException:
        return []

def readwise_get_highlights_for_book(book_id: int) -> list:
    """Fetches all highlights attached to a specific book ID."""
    url = "https://readwise.io/api/v2/highlights/"
    params = {"book_id": book_id}
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.exceptions.RequestException:
        return []


# ==========================================
# FILTERING & SELECTION ENGINE
# ==========================================

def is_excluded(book: dict) -> bool:
    """Evaluates if a book hits the mandatory title or author exclusion filters."""
    title = book.get("title", "").strip().lower()
    author = book.get("author", "").strip().lower()

    exclusions = [
        ("american caesar", "william manchester"),
        ("underwriters of the united states", "hannah farber"),
        ("the code of capital", "katharina pistor")
    ]

    for ex_title, ex_author in exclusions:
        if ex_title in title or ex_author in author:
            return True

    banned_authors = ["warren buffett", "derek sivers"]
    if any(banned in author or banned in title for banned in banned_authors):
        return True

    return False

def get_random_highlights(target_count: int = 3) -> list:
    """Builds a filtered book pool and draws a random highlight from sampled selections."""
    raw_books = readwise_list_books(page_size=200)
    filtered_books = [book for book in raw_books if not is_excluded(book)]

    if len(filtered_books) < target_count:
        target_count = len(filtered_books)

    selected_books = random.sample(filtered_books, target_count)
    random_highlights_pool = []

    for book in selected_books:
        highlights = readwise_get_highlights_for_book(book["id"])
        
        if highlights:
            chosen_highlight = random.choice(highlights)
            
            # ENHANCEMENT 2: Extract Kindle ASIN identifier or fallback to standard source url strings
            asin = book.get("asin")
            amazon_url = f"https://www.amazon.com/dp/{asin}" if asin else book.get("source_url")

            random_highlights_pool.append({
                "book_title": book["title"],
                "book_author": book["author"],
                "amazon_url": amazon_url,  # Structured Amazon URL asset added here
                "highlight_text": chosen_highlight.get("text"),
                "highlighted_at": chosen_highlight.get("highlighted_at")
            })

    return random_highlights_pool


# ==========================================
# MAIN EXECUTION ROUTINE
# ==========================================

def main():
    if READWISE_TOKEN == "YOUR_READWISE_API_TOKEN_HERE":
        print(json.dumps({"error": "CRITICAL: Set your READWISE_TOKEN environment variable."}, indent=2))
        return

    # Process operations
    recent_library_docs = get_recent_library_documents(limit=5)
    random_book_highlights = get_random_highlights(target_count=3)

    # ENHANCEMENT 3: Assemble everything into a unified core JSON dictionary structure
    master_output = {
        "recent_documents": recent_library_docs,
        "random_highlights": random_book_highlights
    }

    # Render clean structural JSON layout
    print(json.dumps(master_output, indent=2))

if __name__ == "__main__":
    main()