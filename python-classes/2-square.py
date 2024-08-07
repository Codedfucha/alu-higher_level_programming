#!/usr/bin/python3
"""
2-square.py
Module to define the Square class with size validation.
"""


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
