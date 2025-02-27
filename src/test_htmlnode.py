import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
  def test_eq(self):
    node = HTMLNode("div", "value")
    node2 = HTMLNode("div", "value")
    self.assertEqual(node, node2)

  def test_test_with_different_value_are_not_eq(self):
    node = HTMLNode("div", "value")
    node2 = HTMLNode("div", "!not same value")
    self.assertNotEqual(node, node2)

  def test_method_props_to_html_returns_correctly(self):
    node = HTMLNode("div", "value", props={"id": "test-id", "class":  "test-class"})
    html = node.props_to_html()
    expected_html = 'class="test-class" id="test-id"'
    self.assertEqual(html, expected_html)

class TestLeafNode(unittest.TestCase):
  def test_eq(self):
    value = "This is a Leaf"
    node = LeafNode("div", value)
    node2 = LeafNode("div", value)
    self.assertEqual(node, node2)

  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
  
  def test_leaf_to_html_div(self):
    node = LeafNode("div", "Hello, world!")
    self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

if __name__ == "__main__":
  unittest.main()