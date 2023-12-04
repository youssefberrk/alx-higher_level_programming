#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute will be added.
        att (str): The name of the attribute to add to `obj`.
        value (any): The value of the attribute `att`.

    Raises:
        TypeError: If the attribute cannot be added, typically due to
            the object not supporting attribute assignment.

    Examples:
        Adding an attribute to an object:
        >>> class Example:
        ...     pass
        >>> obj = Example()
        >>> add_attribute(obj, 'new_attr', 10)
        >>> print(obj.new_attr)
        10

    Note:
        This function uses `setattr()` to add attributes dynamically
        to an object. It checks if the object has a `__dict__`
        attribute to determine if new attributes can be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
