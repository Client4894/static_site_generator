import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        images_tups = extract_markdown_images(old_node.text)
        current = old_node.text
        for tup in images_tups:
            pos = current.find(f"![{tup[0]}]")
            tup_text = current[:pos]
            new_nodes.append(TextNode(tup_text, text_type_text))
            new_nodes.append(TextNode(tup[0], text_type_image, tup[1]))
            current = current[pos + 5 + len(tup[0]) + len(tup[1]):]
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        links_tups = extract_markdown_links(old_node.text)
        current = old_node.text
        for tup in links_tups:
            pos = current.find(f"[{tup[0]}]")
            tup_text = current[:pos]
            new_nodes.append(TextNode(tup_text, text_type_text))
            new_nodes.append(TextNode(tup[0], text_type_link, tup[1]))
            current = current[pos + 4 + len(tup[0]) + len(tup[1]):]
    return new_nodes
