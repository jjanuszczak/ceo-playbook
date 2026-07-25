# Pixabay Image Search

Use `scripts/find_pixabay_candidates.py` with `PIXABAY_API_KEY` to search for real-photo candidates. The tool reads the key from the process environment first, then from the project-root `.env` file. Do not commit `.env`.

The adapter calls the official Pixabay image endpoint with `image_type=photo`, `orientation=horizontal`, and `safesearch=true`. It rejects results tagged `AI generated`. Pixabay requires the application to show the source when displaying API search results, rate limits API keys, and disallows permanent hotlinking. Download an approved image into the Hugo leaf bundle rather than retaining a remote image URL. See [Pixabay API documentation](https://pixabay.com/api/docs/).

Do not treat a search result as an automatic license decision. Record the candidate page URL, creator, selected download URL, and current use-rights basis in `notes.md` and the GitHub issue.
