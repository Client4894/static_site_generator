import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "www.google.de")
        node2 = TextNode("This is a text node", "bold", "www.google.de")
        self.assertEqual(node, node2)
        
    def test_eq_url_none(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)
        
    def test_neq_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is different", "bold")
        self.assertNotEqual(node, node2)      

    def test_neq_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)    

    def test_neq_url(self):
        node = TextNode("This is a text node", "bold", "www.google.de")
        node2 = TextNode("This is a text node", "bold", "www.facebook.de")
        self.assertNotEqual(node, node2)    

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, bold, https://www.boot.dev)", repr(node)
        )        

if __name__ == "__main__":
    unittest.main()
