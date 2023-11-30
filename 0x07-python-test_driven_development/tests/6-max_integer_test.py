#!/usr/bin/python3
"""Module to find the maximum integer in a list."""


def max_integer(list=[]):
    """Find and return the maximum integer in a list of integers.

    Args:
        list (list): A list of integers.

    Returns:
        int or None: max integer in list. Returns None if list is empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
