import os
import json
from markdown_it import MarkdownIt
import re

# Function to extract and clean text content from a Markdown file
def extract_text_from_md(file_path):
    md = MarkdownIt()
    with open(file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
        # Remove HTML tags and extra whitespace
        text_content = re.sub(r'<[^>]*>', '', md_content).strip()
        # Remove '**', '|', and '\.' characters
        text_content = text_content.replace('**', '').replace('|', '').replace('\.', '')
        # Remove extra newlines and spaces
        text_content = ' '.join(text_content.split())
    return text_content

# Function to process all .md files in a directory and write to a JSONL file
def process_md_files_to_jsonl(directory_path, output_file):
    jsonl_data = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.md'):
            file_path = os.path.join(directory_path, filename)
            file_name = os.path.splitext(filename)[0]

            section = {
                "human": f"Tell me about {file_name}.",
                "assistant": extract_text_from_md(file_path)
            }

            jsonl_data.append(section)

    with open(output_file, 'w', encoding='utf-8') as jsonl_file:
        for section in jsonl_data:
            jsonl_file.write(json.dumps(section) + '\n')

if __name__ == "__main__":
    # Specify the directory containing the .md files and the output .jsonl file
    input_directory = 'doc_source'
    output_file = 'docs.jsonl'

    process_md_files_to_jsonl(input_directory, output_file)
