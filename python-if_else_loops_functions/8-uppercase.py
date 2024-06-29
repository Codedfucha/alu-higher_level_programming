#!/usr/bin/python3


def uppercase(str):
    """
    Prints a string in uppercase followed by a new line.

    Args:
        str: The string to convert to uppercase.
    """
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
