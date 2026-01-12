
import os

categories = [
    "Strategy",
    "Leadership",
    "Fintech",
    "Energy Transition",
    "Technology",
    "Venture Building",
    "Essays"
]

template = """---
title: "{title}"
groupByYear: false
showSummary: true 
cascade:
  showSummary: true
---
"""

for category in categories:
    formatted_category = category.lower().replace(" ", "-")
    dir_path = f"content/categories/{formatted_category}"
    file_path = f"{dir_path}/_index.md"

    os.makedirs(dir_path, exist_ok=True)
    
    with open(file_path, "w") as f:
        f.write(template.format(title=category))
    
    print(f"Created {file_path}")

