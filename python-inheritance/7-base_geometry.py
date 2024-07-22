#!/usr/bin/python3
"""
This module defines the class BaseGeometry with methods for area and integer validation.
"""

class BaseGeometry:
    """
    A class representing BaseGeometry with methods for area and integer validation.
    """
    def area(self):
        """
        Raises an exception with the message 'area() is not implemented'.
        
        Raises:
            Exception: Always raised to indicate that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value of an integer attribute.
        
        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
