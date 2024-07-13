#!/usr/bin/python3
"""
1-square.py
Module to define the Square class.
"""


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
