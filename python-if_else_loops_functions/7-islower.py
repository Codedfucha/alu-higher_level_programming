#!/usr/bin/python3
def islower(c):
    """Check if character c is lowercase"""
    # Check if the character is between 'a' and 'z' in ASCII
    return ord('a') <= ord(c) <= ord('z')
