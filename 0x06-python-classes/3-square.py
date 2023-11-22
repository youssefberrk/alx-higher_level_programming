#!/usr/bin/python3

"""Defines a Square class representing a geometric square."""


class Square:
    """Represents a square shape.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size
