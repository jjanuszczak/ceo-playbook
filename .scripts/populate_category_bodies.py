
import os
import re

category_details = {
    "Strategy": {
        "body": "How organizations win over time.\n\n### Includes\n* Platform economics\n* Business models\n* Competitive advantage\n* Ecosystems\n* Long-term thinking\n* Market structure shifts\n\n### Typical reader\n* Board members, CEOs, founders, investors\n\n### Test\n* \"This post could be discussed in a boardroom.\""
    },
    "Leadership": {
        "body": "How people lead, decide, and scale themselves.\n\n### Includes\n* CEO reflections\n* Organizational health\n* Decision-making\n* Culture\n* Talent\n* Personal leadership growth\n\n### Important distinction\n* Leadership \u2260 management\n* This is about judgment, values, and influence"
    },
    "Fintech": {
        "body": "Your domain depth in financial systems and infrastructure.\n\n### Includes\n* Embedded finance\n* Payments\n* Banking models\n* Stablecoins\n* Open finance\n* Regulatory dynamics\n\n### Why a category (not just tags)?\n* Because this is a core pillar of your authority, not just a topic."
    },
    "Energy Transition": {
        "body": "Energy as the next system of innovation.\n\n### Includes\n* Distributed energy\n* EV infrastructure\n* Energy markets\n* Infrastructure economics\n* Climate + capital\n\n### Why separate from Strategy?\n* Because energy is becoming a domain pillar, not a subtopic."
    },
    "Technology": {
        "body": "Technology as an enabling force—not tutorials.\n\n### Includes\n* AI (conceptual, not how-to)\n* Software economics\n* Developer leverage\n* Systems thinking\n* Tool shifts (e.g. GenAI, automation)\n\n### Excludes\n* Step-by-step coding guides\n* Narrow technical docs (those should live elsewhere or be tagged heavily)"
    },
    "Venture Building": {
        "body": "The practice of building, funding, and scaling ventures.\n\n### Includes\n* Venture studios\n* Capital structuring\n* Fund design\n* Board dynamics\n* GTM strategy\n* Early vs scale-stage tradeoffs\n\n### This is different from Strategy\n* Strategy = what to do\n* Venture building = how it actually gets built"
    },
    "Essays": {
        "body": "Personal, reflective, integrative thinking.\n\n### Includes\n* Career reflections\n* Identity shifts\n* Long-form thinking\n* Synthesis across domains\n* Philosophy of work and impact\n\n### Why this matters\n* This category humanizes the site and makes the rest credible."
    }
}

def populate_category_body(file_path, new_body_content):
    if not os.path.exists(file_path):
        print(f"Skipping {file_path}: File not found.")
        return

    with open(file_path, 'r') as f:
        content = f.read()

    # Find the position of the second '---' delimiter
    # This assumes well-formed front matter starting and ending with '---'
    parts = content.split('---', 2) # Split into at most 3 parts: [before first ---, fm content, after second ---]

    if len(parts) < 3:
        print(f"Skipping {file_path}: Malformed front matter delimiters. Expected at least two '---'.")
        return

    # parts[0] is "" if the file starts with '---'
    # parts[1] is the front matter content
    # parts[2] is the content after the second '---' (the existing body, if any)

    front_matter_block = f"---\n{parts[1].strip()}\n---"
    
    # Append the new body content after the front matter block
    updated_content = (
        front_matter_block + "\n" + # Add a newline after the front matter closing delimiter
        new_body_content.strip() + "\n" # The new body content, ensure it ends with a newline
    )

    with open(file_path, 'w') as f:
        f.write(updated_content)
    
    print(f"Updated content for {file_path}")

if __name__ == "__main__":
    for category_name, details in category_details.items():
        formatted_category = category_name.lower().replace(" ", "-")
        file_path = f"content/categories/{formatted_category}/_index.md"
        populate_category_body(file_path, details["body"])
