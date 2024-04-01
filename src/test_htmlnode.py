import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            "p", 
            "text inside the paragraph", 
            ["node1", "node2"], 
            {'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(
            "HTMLNode(p, text inside the paragraph, children: ['node1', 'node2'], {'href': 'https://www.google.com', 'target': '_blank'})", repr(node)
        )

    def test_prop_to_html(self):
        node = HTMLNode(
            "p", 
            "text inside the paragraph", 
            ["node1", "node2"], 
            {'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )

if __name__ == "__main__":
    unittest.main()
