#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Parameters:
    my_list (list): The list from which to delete an item.
    idx (int): The index of the item to delete.

    Returns:
    list: The modified list with the item removed,
    or the same list if idx is out of range.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
