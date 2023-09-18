def kebabize(text):
    kebab_case = ""
    for character in text:
        if kebab_case == "" and character.isupper():
            kebab_case += character.lower()
        elif character.isupper():
            kebab_case += "-" + character.lower()
        elif character.isdigit():
            continue
        else:
            kebab_case += character
    return kebab_case
