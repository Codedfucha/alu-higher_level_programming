#!/usr/bin/python3
"""
This module defines the class BaseGeometry with an area method that raises an exception.
"""

class BaseGeometry:
    """
    A class representing BaseGeometry with a method area.
    """
    def area(self):
        """
        Raises an exception with the message 'area() is not implemented'.
        
        Raises:
            Exception: Always raised to indicate that the method is not implemented.
        """
        raise Exception("area() is not implemented")
