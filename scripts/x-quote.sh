#!/bin/zsh

# Check that the original source URL and published quote URL were supplied.
if [ "$#" -ne 2 ]; then
  echo "Error: expected an original source URL and a published quote URL."
  echo "Usage: $0 <source-url> <published-quote-url>"
  exit 1
fi

# Resolve the repository root so the wrapper can be called from any directory.
script_dir="${0:A:h}"
repo_root="${script_dir:h}"
queue_script="$repo_root/.agents/skills/stage-signals-x-quotes/scripts/stage_signals_x_quotes.py"

# Stage only after the confirmed post was recorded successfully.
cd "$repo_root" || exit 1
uv run python "$queue_script" mark-posted \
  --source "$1" \
  --published-url "$2" \
&& uv run python "$queue_script" stage
