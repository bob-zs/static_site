import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_nodes_with_different_text_types_are_not_equal(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.ITALICS)
    self.assertNotEqual(node, node2)

  def test_nodes_with_same_urls_are_equal(self):
    node = TextNode("This is a text node", TextType.BOLD, "https://example.com/")
    node2 = TextNode("This is a text node", TextType.BOLD, "https://example.com/")
    self.assertEqual(node, node2)

  def test_nodes_with_different_urls_are_not_equal(self):
    node = TextNode("This is a text node", TextType.BOLD, "https://example.com/")
    node2 = TextNode("This is a text node", TextType.BOLD, "https://example.org/")
    self.assertNotEqual(node, node2)

  def test_nodes_with_and_without_url_are_not_equal(self):
    node = TextNode("This is a text node", TextType.BOLD, "https://example.com/")
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertNotEqual(node, node2)

if __name__ == "__main__":
  unittest.main()