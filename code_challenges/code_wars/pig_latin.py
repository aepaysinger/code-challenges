def pig_it(text):
    text = text.split(" ")
    translated_text = ""
    punctuations = [" ", ".", "!", "?"]
    for word in text:
        if word in punctuations:
            translated_text += word
        else:
            translated_text += word[1:] + word[0] + "ay" + " "
    if translated_text[-1] == " ":
        return translated_text[:-1]
    else:
        return translated_text


if __name__ == "__main__":
    text = "Hello world !"
    print(pig_it(text))
