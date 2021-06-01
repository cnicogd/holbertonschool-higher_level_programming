#!/usr/bin/python3
"""Module that read a file"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)  """

    with open(filename, "w", encoding='utf-8') as f:
        data = f.write(text)
        return data
