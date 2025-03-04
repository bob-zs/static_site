import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        test_data = [
            # Bold tests
            (
                "A **bolded** word is here",
                "**",
                TextType.BOLD,
                [
                    TextNode("A ", TextType.TEXT),
                    TextNode("bolded", TextType.BOLD),
                    TextNode(" word is here", TextType.TEXT),
                ],
            ),
            (
                "There will be **two bolded** words here in this **text** here",
                "**",
                TextType.BOLD,
                [
                    TextNode("There will be ", TextType.TEXT),
                    TextNode("two bolded", TextType.BOLD),
                    TextNode(" words here in this ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" here", TextType.TEXT),
                ],
            ),
            (
                "Can bold at the **end**",
                "**",
                TextType.BOLD,
                [
                    TextNode("Can bold at the ", TextType.TEXT),
                    TextNode("end", TextType.BOLD),
                ],
            ),
            (
                "**Start with** bold in this sentence",
                "**",
                TextType.BOLD,
                [
                    TextNode("Start with", TextType.BOLD),
                    TextNode(" bold in this sentence", TextType.TEXT),
                ],
            ),
            # Code tests
            (
                "A `coded` word is here",
                "`",
                TextType.CODE,
                [
                    TextNode("A ", TextType.TEXT),
                    TextNode("coded", TextType.CODE),
                    TextNode(" word is here", TextType.TEXT),
                ],
            ),
            (
                "There will be `two coded` words here in this `text` here",
                "`",
                TextType.CODE,
                [
                    TextNode("There will be ", TextType.TEXT),
                    TextNode("two coded", TextType.CODE),
                    TextNode(" words here in this ", TextType.TEXT),
                    TextNode("text", TextType.CODE),
                    TextNode(" here", TextType.TEXT),
                ],
            ),
            (
                "Can code at the `end`",
                "`",
                TextType.CODE,
                [
                    TextNode("Can code at the ", TextType.TEXT),
                    TextNode("end", TextType.CODE),
                ],
            ),
            (
                "`Start with` code in this sentence",
                "`",
                TextType.CODE,
                [
                    TextNode("Start with", TextType.CODE),
                    TextNode(" code in this sentence", TextType.TEXT),
                ],
            ),
            # Italics Tests
            (
                "A *italicized* word is here",
                "*",
                TextType.ITALIC,
                [
                    TextNode("A ", TextType.TEXT),
                    TextNode("italicized", TextType.ITALIC),
                    TextNode(" word is here", TextType.TEXT),
                ],
            ),
            (
                "There will be *two italicized* words here in this *text* here",
                "*",
                TextType.ITALIC,
                [
                    TextNode("There will be ", TextType.TEXT),
                    TextNode("two italicized", TextType.ITALIC),
                    TextNode(" words here in this ", TextType.TEXT),
                    TextNode("text", TextType.ITALIC),
                    TextNode(" here", TextType.TEXT),
                ],
            ),
            (
                "Can italicize at the *end*",
                "*",
                TextType.ITALIC,
                [
                    TextNode("Can italicize at the ", TextType.TEXT),
                    TextNode("end", TextType.ITALIC),
                ],
            ),
            (
                "*Start with* italic in this sentence",
                "*",
                TextType.ITALIC,
                [
                    TextNode("Start with", TextType.ITALIC),
                    TextNode(" italic in this sentence", TextType.TEXT),
                ],
            ),
        ]

        for text, delimiter, text_type, expected_nodes in test_data:
            with self.subTest(text=text, delimiter=delimiter, text_type=text_type):
                node = TextNode(text, TextType.TEXT)
                splitted_nodes = split_nodes_delimiter([node], delimiter, text_type)
                self.assertListEqual(expected_nodes, splitted_nodes)
