#!/usr/bin/python3
"""
3-square.py
Defines a Square class with private size attribute and area calculation method.
"""


class Square:
    """
    Square class with private size attribute and area calculation method.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Args:
            size (int): Optional size of the square. Defaults to 0.
                         Must be an integer >= 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: Area of the square (size * size).
        """
        return self.__size ** 2

# This code is for testing purposes
if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
