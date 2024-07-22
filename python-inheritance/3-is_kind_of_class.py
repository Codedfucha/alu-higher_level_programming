#!/usr/bin/python3
"""
This module defines the function is_kind_of_class.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class ; otherwise False.
    
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    
    Returns:
        bool: True if obj is an instance of or inherits from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
