import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_nodes_with_different_text_types_are_not_equal(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.ITALIC)
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

class TestTextNodeToHTMLNode(unittest.TestCase):
  def test_text(self):
    text = "text node right here"
    node = TextNode(text, TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, text)
  
  def test_image(self):
    text = "image node right here"
    url = "https://www.boot.dev"
    node = TextNode(text, TextType.IMAGE, url)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, text)
    self.assertEqual(html_node.props, {"src": url, "alt": text })
  
  def test_bold(self):
    text = "This is bold"
    node = TextNode(text, TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, text)

if __name__ == "__main__":
  unittest.main()