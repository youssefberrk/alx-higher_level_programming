#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for index, char in enumerate(text):
        if char == ' ':
            start += 1
        else:
            break

    while start < len(text):
        print(text[start], end="")
        if text[start] in ".?:":
            print("\n\n", end="")
            start += 1
            while start < len(text) and text[start] == ' ':
                start += 1
            continue
        start += 1


if __name__ == "__main__":
    try:
        text_indentation("Hello. How are you? I'm good.")
    except Exception as e:
        print(e)
