import re
import os

def update_tags_in_frontmatter(file_path, new_tags):
    if not os.path.exists(file_path):
        print(f"Skipping {file_path}: File not found.")
        return

    with open(file_path, 'r') as f:
        content = f.read()

    # Find the start and end of the front matter
    first_delimiter_match = re.match(r'^(---)\s*\n?', content, re.MULTILINE)
    if not first_delimiter_match:
        print(f"Skipping {file_path}: No starting front matter delimiter found.")
        return

    first_delimiter_start_pos = first_delimiter_match.start()
    first_delimiter_end_pos = first_delimiter_match.end()

    second_delimiter_match = re.search(r'^(---)\s*\n?', content[first_delimiter_end_pos:], re.MULTILINE)
    if not second_delimiter_match:
        print(f"Skipping {file_path}: No ending front matter delimiter found.")
        return

    second_delimiter_start_pos_in_full_content = first_delimiter_end_pos + second_delimiter_match.start()
    second_delimiter_end_pos_in_full_content = first_delimiter_end_pos + second_delimiter_match.end()

    # Extract parts of the file
    pre_front_matter_content = content[:first_delimiter_start_pos]
    front_matter_content_raw = content[first_delimiter_end_pos:second_delimiter_start_pos_in_full_content]
    body_content = content[second_delimiter_end_pos_in_full_content:]

    # Process front matter line by line to replace tags
    front_matter_lines = front_matter_content_raw.split('\n')
    new_front_matter_lines = []
    
    tags_section_processed = False
    skipping_old_tags = False # Flag to indicate if we are currently skipping old tag lines

    new_tags_yaml_lines = []
    if new_tags:
        new_tags_yaml_lines.append("tags:")
        for tag in new_tags:
            new_tags_yaml_lines.append(f"  - {tag}")
    
    for line in front_matter_lines:
        if re.match(r'tags:\s*$', line) or re.match(r'tags:\s*\[.*\]', line): # Match 'tags:' or 'tags: [...]'
            if not tags_section_processed: # Only process the tags section once
                new_front_matter_lines.extend(new_tags_yaml_lines)
                tags_section_processed = True
                skipping_old_tags = True # Start skipping old tags lines
            continue
        
        if skipping_old_tags:
            if re.match(r'^\s*-\s*.*$', line) or line.strip() == '':
                # This is an old tag line or an empty line within the tags block, so skip it
                continue
            else:
                # We've encountered a line that is not part of the old tags block, so stop skipping
                skipping_old_tags = False
        
        # If not skipping old tags, or if we just stopped skipping, append the line
        new_front_matter_lines.append(line)
    
    # If no 'tags:' section was found and processed (and there are new tags to add), append the new tags section
    if not tags_section_processed and new_tags:
        if new_front_matter_lines and new_front_matter_lines[-1].strip() != '':
             new_front_matter_lines.append('') # Add a blank line for separation if needed
        new_front_matter_lines.extend(new_tags_yaml_lines)


    # Reconstruct the full content
    updated_content = (
        pre_front_matter_content +
        first_delimiter_match.group(0).strip() + "\n" +
        '\n'.join(new_front_matter_lines).strip() + "\n" +
        second_delimiter_match.group(0).strip() + "\n" + # Added newline here
        body_content
    )

    with open(file_path, 'w') as f:
        f.write(updated_content)
    print(f"Updated tags for {file_path}")

def parse_markdown_table(md_table_content):
    lines = md_table_content.strip().split('\n')
    header = [h.strip() for h in lines[0].split('|')[1:-1]]
    data = []
    for line in lines[2:]:
        values = [v.strip() for v in line.split('|')[1:-1]]
        data.append(dict(zip(header, values)))
    return data

if __name__ == "__main__":
    # Read markdown_table_content dynamically from tag_governance_proposal.md
    with open("tag_governance_proposal.md", "r") as f:
        markdown_table_content = f.read()

    processed_files_data = parse_markdown_table(markdown_table_content)

    for row in processed_files_data:
        file_path = row['File Path'].strip('`')
        proposed_tags_str = row['Proposed Tags']
        
        new_tags = [tag.strip().replace('`', '') for tag in proposed_tags_str.split(',')] if proposed_tags_str != '(none)' else []
        
        update_tags_in_frontmatter(file_path, new_tags)