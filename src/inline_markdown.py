import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue

        splitted_nodes = []
        divided_texts = node.text.split(delimiter)

        do_all_delimiters_close = len(divided_texts) % 2 == 1
        if not do_all_delimiters_close:
            raise Exception(
                f"Error: Text has unclosed delimiter - {delimiter} - in text - {node.text} -"
            )

        for i in range(0, len(divided_texts)):
            text = divided_texts[i]
            if text == "":
                continue
            is_text_for_text_type = i % 2 == 1
            if is_text_for_text_type:
                splitted_nodes.append(TextNode(text, text_type))
            else:
                splitted_nodes.append(TextNode(text, TextType.TEXT))

        node_list.extend(splitted_nodes)
    return node_list

def extract_markdown_links(text):
    markdown_link_regex = r"(?<!!)\[(.*?)\]\(((?:https?:\/\/|www\.)[^\s]+|mailto:[^\s]+|tel:[^\s]+)\)"
    return re.findall(markdown_link_regex, text)

def extract_markdown_images(text):
    markdown_image_regex = r"!\[([^\[\]]*)\]\(((?:https?:\/\/|www\.)[^\s]+)\)"
    return re.findall(markdown_image_regex, text)

def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        if node != TextType.Text:
            node.list.append(node)
            continue
        
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            node_list.append(old_nodes)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            node_list.append(node)
            continue
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) !=2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                node_list.append(TextNode(sections[0], TextType.TEXT))
            node_list.append(TextType[link[0], TextType.LINK, link[1]])
            text = sections[1]
        if text != "":
            node_list.append(TextNode((text, TextType.TEXT)))
    return node_list

def split_nodes_image(old_nodes):
    node_list = []
    for node in old_nodes:
        if node != TextType.TEXT:
            node_list.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            node_list.append(node)
            continue

        for image in images:
            alt_text = image[0]
            image_url = image[1]
            text_sections = text.split(f"![{alt_text}({image_url})]", 1)
            if len(text_sections) != 2:
                raise ValueError("image brackets not closed")
            if text_sections[0] != "":
                node_list.append(TextNode(text_sections[0], TextType.TEXT))
            node_list.append(TextNode(alt_text, TextType.IMAGE, image_url))
        if text != "":
            node_list.append(TextNode(text, TextType.TEXT))
    return node_list
