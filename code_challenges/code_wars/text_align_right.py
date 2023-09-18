import re


def align_right(text,width):
    # aligned_text = ""
    # for words in text:
        

    #     print(words)
    print(re.split(r'(\W+)', text))




if __name__ == "__main__":
    text = "Two lines, I am"
    width = 10
    print(align_right(text, width))