#!/usr/bin/python3
"""
6-main.py
Tests for the Square class defined in 6-square.py.
"""

Square = __import__('6-square').Square

def main():
    # Test case 1: Square of size 3 with default position
    print("Test case 1:")
    my_square_1 = Square(3)
    my_square_1.my_print()
    print("--")

    # Test case 2: Square of size 3 with position (1, 1)
    print("Test case 2:")
    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()
    print("--")

    # Test case 3: Square of size 3 with position (3, 0)
    print("Test case 3:")
    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()
    print("--")

    # Additional tests: Edge cases
    print("Additional tests:")
    # Test case 4: Square of size 0
    my_square_4 = Square(0, (1, 1))
    my_square_4.my_print()
    print("--")

    # Test case 5: Square of size 5 with position (0, 0)
    my_square_5 = Square(5, (0, 0))
    my_square_5.my_print()
    print("--")

    # Test case 6: Square of size 5 with invalid position (-1, 1)
    try:
        my_square_6 = Square(5, (-1, 1))
        my_square_6.my_print()
    except Exception as e:
        print("Error:", e)
    print("--")

if __name__ == "__main__":
    main()
