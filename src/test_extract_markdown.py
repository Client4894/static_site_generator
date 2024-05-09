
import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtraction(unittest.TestCase):
    def test_extract_images(self):
        imagetext = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        extracted = extract_markdown_images(imagetext)
        self.assertListEqual(
            [
                ('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), 
                ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')
            ],
            extracted
        )

    def test_extract_links(self):
        linktext = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        extracted = extract_markdown_links(linktext)
        self.assertListEqual( 
            [
                ('link', 'https://www.example.com'), 
                ('another', 'https://www.example.com/another')
            ],
            extracted
        )

if __name__ == "__main__":
    unittest.main()
