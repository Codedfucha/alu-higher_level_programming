#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

def main():
    # Create a rectangle with width 2 and height 4
    my_rectangle = Rectangle(2, 4)
    
    # Test string representation (__str__)
    print("String representation:")
    print(str(my_rectangle))
    print("--")
    
    # Test regular print (__str__)
    print("Regular print:")
    print(my_rectangle)
    print("--")
    
    # Test representation (__repr__)
    print("Representation:")
    print(repr(my_rectangle))
    print("--")
    
    # Test object address (hex(id()))
    print("Object address:")
    print(hex(id(my_rectangle)))
    print("--")
    
    # Create a new instance based on representation
    print("Creating new instance from representation:")
    new_rectangle = eval(repr(my_rectangle))
    
    # Test string representation of the new instance (__str__)
    print("String representation of new instance:")
    print(str(new_rectangle))
    print("--")
    
    # Test regular print of the new instance (__str__)
    print("Regular print of new instance:")
    print(new_rectangle)
    print("--")
    
    # Test representation of the new instance (__repr__)
    print("Representation of new instance:")
    print(repr(new_rectangle))
    print("--")
    
    # Test object address of the new instance (hex(id()))
    print("Object address of new instance:")
    print(hex(id(new_rectangle)))
    print("--")
    
    # Test if the new instance is not the same as the original instance
    print("Are they the same instance?")
    print(new_rectangle is my_rectangle)
    
    # Test if the type of the new instance is the same as the original instance
    print("Are they the same type?")
    print(type(new_rectangle) is type(my_rectangle))

if __name__ == "__main__":
    main()
