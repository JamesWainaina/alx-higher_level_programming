#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    
    para = 0
    
    for i in text:
        if para == 0:
            if i == ' ':
                continue
            else:
                para = 1
        if para == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                para = 0

            else:
                print(i, end="")

