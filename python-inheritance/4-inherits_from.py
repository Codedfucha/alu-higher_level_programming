#!/usr/bin/python3
"""
This module defines the function inherits_from.
"""

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    
    Returns:
        bool: True if obj is an instance of a class that inherits from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
