from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        if text_type not in TextType:
            raise ValueError(f"'{text_type}' is not a valid TextType.")
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
            )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
