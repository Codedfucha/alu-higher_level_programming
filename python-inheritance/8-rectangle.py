#!/usr/bin/python3
"""
This module defines the class Rectangle which inherits from BaseGeometry.
"""

from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
