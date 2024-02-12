#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list of lists: A list containing lists representing each row of
        Pascal's triangle up to the nth row. Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    pascal = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        row.append(1)
        pascal.append(row)

    return pascal
