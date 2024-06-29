#!/usr/bin/python3


def fizzbuzz():
    """
    Prints the numbers from 1 to 100 separated by a space.
    For multiples of three prints Fizz instead of the number
    and for the multiples of five prints Buzz.
    For numbers which are multiples of both three and five prints FizzBuzz.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
