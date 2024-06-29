#!/usr/bin/python3

def print_last_digit(number):
    """
    Prints the last digit of a number.

    Args:
        number: The number to get the last digit of.

    Returns:
        The value of the last digit.
    """
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
