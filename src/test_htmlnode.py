import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        node = HTMLNode("div", "value", props={"id": "test-id", "class": "test-class"})
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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal Text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold Text</b>Normal Text<i>Italic Text</i>Normal Text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold Text</b>Normal Text<i>Italic Text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
