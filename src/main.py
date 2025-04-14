from textnode import TextNode

print("hello world")

def main():
    tn_obj = TextNode("Word","link","url")
    print(tn_obj.text)
    print(tn_obj.text_type)
    print(tn_obj.url)

main()
