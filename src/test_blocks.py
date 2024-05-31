import unittest
from blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_quote,
    block_type_ordered_list,
    block_type_heading,
    block_type_unordered_list,
    block_type_code,
    block_type_paragraph,
    markdown_to_html_node,
    block_to_html_node,
    quote_to_html_node,
    unorderedlist_to_html_node
)


class testblocks(unittest.TestCase):
    def test1(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n*This is a list\n* with items"
        expected_outcome = ["This is **bolded** paragraph","This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "*This is a list\n* with items" ]
        self.assertEqual(markdown_to_blocks(markdown), expected_outcome)
        #print(markdown_to_blocks(markdown))

    def test2(self):
        block = ">ihatethis\n>joebama"
        expected_outcome = block_type_quote
        self.assertEqual(block_to_block_type(block), expected_outcome)

    
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_quote_to_html_node(self):
        block = '>This is a\n >blockquote block'
        try:
            node = quote_to_html_node(block)
            html = node.TO_HTML()
            print(html)  # Should print <blockquote>This is a blockquote block</blockquote>
        except ValueError as e:
            print(str(e))

    def test_unordered_list_to_html_node(self):
        block = "* Item 1\n* Item 2\n* Item 3"
        try:
            node = unorderedlist_to_html_node(block)
            html = node.TO_HTML()
            print(html)  # Should print <ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>
        except ValueError as e:
            print(str(e))



    


if __name__ == "__main__":
     unittest.main()
            