
from textnode import TextNode
from inline_markdown import split_nodes_image, split_nodes_link

def main():
    test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(test)

    node = TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        "text",
    )
    print(split_nodes_image([node]))
main()
