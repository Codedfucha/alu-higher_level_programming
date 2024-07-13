#!/usr/bin/python3
"""
3-main.py
Tests the Square class with area calculation and attribute access.
"""
from square import Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except AttributeError as e:
    print(e)

try:
    print(my_square_1.__size)
except AttributeError as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
