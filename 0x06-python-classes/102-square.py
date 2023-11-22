#!/usr/bin/python3

"""Define a Square class representing a geometric square."""


class Square:
    """Represents a square shape.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance with a given size.
        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to be set.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Define the equality comparison for a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the inequality comparison for a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the less-than comparison for a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the less-than-or-equal comparison for a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the greater-than comparison for a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the greater-than-or-equal comparison for a Square."""
        return self.area() >= other.area()
