import unittest

from textnode import(
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)
from inline_markdown import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

class Test_split_nodes_delimiter(unittest.TestCase):
    def test_1(self):
        old_node = TextNode("This is text with a `code block` word", text_type="text")
        new_node = split_nodes_delimiter([old_node], "`", text_type="code")
        expected_outcome = [
            TextNode("This is text with a ", text_type="text"),
            TextNode("code block", text_type="code"),
            TextNode(" word", text_type="text"),
            ]

        self.assertEqual(new_node, expected_outcome)

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )




if __name__ == "__main__":
    unittest.main()
