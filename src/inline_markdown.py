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
