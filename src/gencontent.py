import os
from blocks import markdown_to_html_node

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title")

def generate_page(from_path, template_path, dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()

    template_file = open(template_path, "r")
    template = template_path.read()
    template_path.close()

    html_node = markdown_to_html_node(markdown_content).TO_HTML

    title = extract_title(markdown_content)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.mkdir(dest_dir_path, exist_ok = True)
    to_file = open(dest_path, "w")
    to_file.write(template)
