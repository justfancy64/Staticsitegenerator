import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node

class textHTMLNode(unittest.TestCase):

    def test_PROPS_TO_HTML(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props)
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.PROPS_TO_HTML(),expected_output)
   
    def test_TO_HTML(self):
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        
        expected_result = "<p>This is a paragraph of text.</p>"
        actual_result = leaf1.TO_HTML()
        self.assertEqual(actual_result,expected_result)

    def test_TO_HTML_child(self):
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_result = '<a href="https://www.google.com">Click me!</a>'
        actual_result = leaf2.TO_HTML()
        self.assertEqual(actual_result,expected_result)

    def test_TO_HTML_manychildren(self):
        parent_Node = ParentNode("p",[LeafNode("b", "Bold text"), 
                                      LeafNode(None, " "), 
                                      LeafNode("i", "italic text"), 
                                      LeafNode(None, "Normal text"),]
                                      ,)
        expected_output = "<p><b>Bold text</b> <i>italic text</i>Normal text</p>"
        self.assertEqual(expected_output, parent_Node.TO_HTML())

    def test_TO_HTML_grandchildren(self):
        leaf1 = LeafNode("p", "I'm a text in a paragraph.")
        leaf2 = LeafNode("span", "I'm a sibling text.")
        parentNode = ParentNode("p", [leaf1])
        grandParentNode = ParentNode("div", [parentNode, leaf2])
        expected_output = "<div><p><p>I'm a text in a paragraph.</p></p><span>I'm a sibling text.</span></div>"

        self.assertEqual(grandParentNode.TO_HTML(),expected_output)


class test_text_node_to_html_node(unittest.TestCase):

    def test_text(self):
        text_node = TextNode(text_type="text",text="Hello, World!")
        HTMLNode = text_node_to_html_node(text_node)
        self.assertIsNone(HTMLNode.tag)
        self.assertEqual(HTMLNode.value, "Hello, World!")

    def test_text_bold(self):
        text_node = TextNode(text_type="bold",text="its gg")
        HTMLNode = text_node_to_html_node(text_node)
        self.assertEqual(HTMLNode.value,"its gg")
        self.assertEqual(HTMLNode.tag, "b")
    
    def test_text_link(self):
        text_node = TextNode(text_type="link",text="loggies",url="https://www.fflogs.com/reports/wTp29FaC6nfYZtc1#type=damage-done&fight=42&phase=6&source=431")
        HTMLNode = text_node_to_html_node(text_node)
        self.assertEqual(HTMLNode.value, "loggies")
        self.assertEqual(HTMLNode.props, {"href": "https://www.fflogs.com/reports/wTp29FaC6nfYZtc1#type=damage-done&fight=42&phase=6&source=431" })
        self.assertEqual(HTMLNode.tag, "a" )

    def test_text_img(self):
        text_node = TextNode(text_type="image",text="image text idk", url="image.gg")
        HTMLNode = text_node_to_html_node(text_node)
        self.assertEqual(HTMLNode.props, {'src': 'image.gg', 'alt': 'image text idk'})

if __name__== "__main__":
    unittest.main()