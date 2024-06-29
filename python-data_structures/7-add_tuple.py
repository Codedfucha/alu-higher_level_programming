#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples are at least of length 2 by adding zeros if necessary
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # Only consider the first two elements
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
