from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link

)
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        sections = old_node.text.split(delimiter)
        split_nodes = []
        if len(sections) % 2 == 0:
            raise ValueError("missing closing delimiter")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i],text_type_text))
            else:
                split_nodes.append(TextNode(sections[i],text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    tuples = []
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    for match in matches:
        tuples.append(match)
    return tuples

def extract_markdown_links(text):
    tuples = []
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    for match in matches:
        tuples.append(match)
    return tuples

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        remaining_text = old_node.text
        image_tups = extract_markdown_images(remaining_text)

        if len(image_tups) == 0:
            new_nodes.append(old_node)
            continue

        for image_tup in image_tups:
            sections = remaining_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],text_type_text))
            new_nodes.append(TextNode(image_tup[0],text_type_image,image_tup[1]))
            remaining_text = sections[1]
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        link_tups = extract_markdown_links(remaining_text)

        if len(link_tups) == 0:
            new_nodes.append(old_node)
            continue

        for link_tup in link_tups:
            sections = remaining_text.split(f"[{link_tup[0]}]({link_tup[1]})",1)

            if len(sections) != 2:
                raise ValueError("invalid markdown")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],text_type_text))
            new_nodes.append(TextNode(link_tup[0],text_type_link,link_tup[1]))
            remaining_text = sections[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, text_type_text))

    return new_nodes

def text_to_textnodes(text):
    raw_textnode = TextNode(text, text_type_text)
    step1_image_nodes = split_nodes_image([raw_textnode])
    step2_link_nodes = split_nodes_link(step1_image_nodes)
    step3_code_nodes = split_nodes_delimiter(step2_link_nodes,"`", text_type_code)
    step4_bold_nodes = split_nodes_delimiter(step3_code_nodes, "**", text_type_bold)
    step5_italic_nodes = split_nodes_delimiter(step4_bold_nodes, "*", text_type_italic)
    return step5_italic_nodes
    
    