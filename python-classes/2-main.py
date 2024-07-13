#!/usr/bin/python3
"""
2-main.py
Script to demonstrate the usage of the Square class with size validation.
"""

Square = __import__('2-square').Square

# Test cases
my_square_1 = Square(3)
print(type(my_square_1))  # Output: <class '2-square.Square'>
print(my_square_1.__dict__)  # Output: {'_Square__size': 3}

my_square_2 = Square()
print(type(my_square_2))  # Output: <class '2-square.Square'>
print(my_square_2.__dict__)  # Output: {'_Square__size': 0}

# Accessing private attribute should raise AttributeError
try:
    print(my_square_1.size)  # Output: AttributeError: 'Square' object has no attribute 'size'
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)  # Output: AttributeError: 'Square' object has no attribute '__size'
except Exception as e:
    print(e)

# Testing TypeError for non-integer size
try:
    my_square_3 = Square("3")
    print(type(my_square_3))  # This line won't execute due to TypeError raised
    print(my_square_3.__dict__)
except Exception as e:
    print(e)  # Output: size must be an integer

# Testing ValueError for negative size
try:
    my_square_4 = Square(-89)
    print(type(my_square_4))  # This line won't execute due to ValueError raised
    print(my_square_4.__dict__)
except Exception as e:
    print(e)  # Output: size must be >= 0

