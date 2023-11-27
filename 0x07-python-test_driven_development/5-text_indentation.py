#!/usr/bin/python3

def text_indentation(text):
    """ 
    a function that prints a text with 2 new lines after each of these characters
    Args:
        text: The text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    no_space = True
    size = 0
    text = text.strip()
    new_text = ""
    for x in text:
        if x == " " and no_space:
            pass
        elif x == "." or x == "?" or x == ":":
            new_text += x + "\n\n"
            no_space = True
        else:
            new_text += x
            no_space = False
    print(new_text, end='')
