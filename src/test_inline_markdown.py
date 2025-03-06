import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images
)
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

    def test_extract_markdown_links(self):
        test_cases = [
            {
                "text": "This is text with a [oranges](https://en.wikipedia.org/wiki/Orange_(fruit))",
                "expected": [("oranges", "https://en.wikipedia.org/wiki/Orange_(fruit)")],
            },
            {
                "text": "Multiple links in this text with a [oranges](https://en.wikipedia.org/wiki/Orange_(fruit)) and [another link with a space](https://blog.boot.dev)",
                "expected": [("oranges", "https://en.wikipedia.org/wiki/Orange_(fruit)"), ("another link with a space", "https://blog.boot.dev")],
            },
            {
                "text": "This text has [invalid link](invalidlink) and [another invalid link](ftp://example.com).",
                "expected": [],
            },
            {
                "text": "This is just some plain text without any markdown links.",
                "expected": [],
            },
            {
                "text": "This is text with a [example](www.example.com), [Open in app](mailto:example@example.com), and [Connect](tel:+123456789).",
                "expected": [("example", "www.example.com"), ("Open in app", "mailto:example@example.com"), ("Connect", "tel:+123456789")],
            },
            {
                "text": "This text has [almost a link](not-a-real-link) and [another almost link](invalid://example.com).",
                "expected": [],
            },
            {
                "text": "This is not a link. This is an image ![alt](https://example.com/image.jpg).",
                "expected": [],
            }
        ]

        for case in test_cases:
            with self.subTest(case=case):
                matches = extract_markdown_links(case["text"])
                self.assertListEqual(matches, case["expected"])

class TestMarkdownLinkAndImageExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        test_cases = [
            {
                "text": "This is an image ![alt](https://example.com/image.jpg).",
                "expected": [("alt", "https://example.com/image.jpg")],
            },
            {
                "text": "Multiple images here with ![alt](https://example.com/image.jpg) and ![red](https://dummyimage.com/200x300/ff0000/ffffff).",
                "expected": [("alt", "https://example.com/image.jpg"), ("red", "https://dummyimage.com/200x300/ff0000/ffffff")],
            },
            {
                "text": "This is an image with spaces in alt text ![alt text with spaces](https://example.com/image.jpg).",
                "expected": [("alt text with spaces", "https://example.com/image.jpg")],
            },
            {
                "text": "This text has ![invalid image](invalidimage) and ![another invalid image](ftp://example.com/image.jpg).",
                "expected": [],
            },
            {
                "text": "This is just some plain text without any markdown images.",
                "expected": [],
            },
            {
                "text": "This is an image with special characters ![alt](https://example.com/image(1).jpg).",
                "expected": [("alt", "https://example.com/image(1).jpg")],
            },
            {
                "text": "This is almost an image ![almost an image](not-a-real-link) and ![another almost image](invalid://example.com).",
                "expected": [],
            },
            {
                "text": "This is not an image. This is a link: [oranges](https://en.wikipedia.org/wiki/Orange_(fruit))",
                "expected": [],
            }
        ]

        for case in test_cases:
            with self.subTest(case=case):
                matches = extract_markdown_images(case["text"])
                self.assertListEqual(matches, case["expected"])