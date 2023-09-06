#!/usr/bin/python3



def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = "".join(["{}\n\n".format(char) if char in ['.','?',':'] 
                      else "{}".format(char) for char in text])
    print(result.lstrip())
