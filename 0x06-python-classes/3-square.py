#!/usr/bin/python3
"""3-square
a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """Square class init, assign a value to
        Args:
            size (int): The private arg size of the square.
        Raise:
            ValueError: If size is less than Zero
            TypeError: If size is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method to calc the area of a square.
        Returns:
            The area of a square.
        """
        return (self.__size ** 2)
