#!/usr/bin/python3
from rectangle import Rectangle

class Square(Rectangle):
    """A class representing a square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize the square with a size."""
        self.integer_validator("size", size)
        self.__size = size
        # Initialize Rectangle with width and height equal to size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Return the area of the square."""
        return super().area()
