from textnode import TextNode, TextType

def main(text, text_type, url):
    node = TextNode(text, TextType.LINK, url)
    print(node)

node = main('This is some anchor text', 'link', 'https://www.boot.dev')
