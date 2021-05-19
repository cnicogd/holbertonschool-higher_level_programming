#!/usr/bin/python3

"""Square class"""


class Square:
    """Square class init, assign a value to
            Args:
                size (int): The private arg size of the square.
            Raise:
                ValueError: If size is less than Zero
                TypeError: If size is not an integer
            """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
