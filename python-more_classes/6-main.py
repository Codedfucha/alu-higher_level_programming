#!/usr/bin/python3
""" Test script for Rectangle class """

from importlib.machinery import SourceFileLoader
Rectangle = SourceFileLoader('Rectangle', './6-rectangle.py').load_module().Rectangle

def main():
    # Create two instances of Rectangle
    my_rectangle_1 = Rectangle(2, 4)
    my_rectangle_2 = Rectangle(3, 5)

    # Print number of instances
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

    # Test area and perimeter methods
    print("Area of my_rectangle_1:", my_rectangle_1.area())
    print("Perimeter of my_rectangle_1:", my_rectangle_1.perimeter())

    # Test string representation
    print("String representation of my_rectangle_1:")
    print(str(my_rectangle_1))

    # Test eval() to recreate instance
    new_rectangle = eval(repr(my_rectangle_1))
    print("Recreated instance using eval():", new_rectangle)

    # Test instance deletion
    del my_rectangle_1
    print("{:d} instances of Rectangle after deletion".format(Rectangle.number_of_instances))

    del my_rectangle_2
    print("{:d} instances of Rectangle after all deletions".format(Rectangle.number_of_instances))

if __name__ == "__main__":
    main()
