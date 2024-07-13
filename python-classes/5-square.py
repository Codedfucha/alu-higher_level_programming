#!/usr/bin/python3
"""
5-square.py
Defines a Square class with private attribute, getter, setter, area calculation,
and printing functionality.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square instance with a given size.

        Args:
            size (int): Size of the square. Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (int): Size to set for the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: Area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' character.

        Prints a square of size __size x __size using '#' characters.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
