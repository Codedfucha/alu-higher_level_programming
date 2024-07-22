#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
"""

class MyList(list):
    """
    A subclass of list with an additional method to print the list in ascending order.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
