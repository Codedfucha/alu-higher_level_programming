#!/usr/bin/python3
"""
6-square.py
Defines a Square class with private attributes for size and position, getters,
setters, area calculation, and printing functionality.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): Private attribute representing the size of the square.
        __position (tuple): Private attribute representing the position of
                            the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance with a given size and position.

        Args:
            size (int): Size of the square. Default is 0.
            position (tuple): Position of the square as a tuple of two
                              positive integers. Default is (0, 0).
        Raises:
            TypeError: If size is not an integer or if position is not a
                       tuple of two positive integers.
            ValueError: If size is less than 0 or if position contains
                        non-positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.

        Returns:
            tuple: Position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square.

        Args:
            value (tuple): Position to set for the square as a tuple of two
                           positive integers.
        Raises:
            TypeError: If value is not a tuple or if elements are not
                       integers.
            ValueError: If tuple does not contain exactly two positive
                        integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(num >= 0 for num in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: Area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' character with given position.

        Prints a square of size __size x __size using '#' characters,
        positioned as specified. If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
