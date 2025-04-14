from enum import Enum

class TextType(Enum):
    NORMAL_TXT = "normal"
    BOLD_TXT = "bold"
    ITALIC_TXT = "italic"
    CODE_TXT = "code"
    LINK_TXT = "link"
    IMAGE_TXT = "image"
    
class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

def __eq__(TextNode1,TextNode2):
    pass

def __repr__(TextNode):
    return (str(TextNode))
