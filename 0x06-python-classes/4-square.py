#!/usr/bin/python3
class Square:
    """4-square
    a class Square that defines a square by: (based on 3-square.py)"""

    def __init__(self, size=0):
        """Square class init, assign a value to
        Args:
            value (int): The private arg size of the square.
        Raise:
            ValueError: If value is less than Zero
            TypeError: If value is not an integer
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """Method to calc the area of a square.
        Returns:
            The area of a square.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Method getter.
        Returns:
            The size of a square.
        """
        return self.__size

    @size.setter
    def size(self, sizze):
        """Method setter: set the size
        Args:
            size (int): The private arg size of the square.
        Raise:
            ValueError: If size is less than Zero
            TypeError: If size is not an integer
        """
        if not isinstance(sizze, int):
            raise TypeError("size must be an integer")
        if sizze < 0:
            raise ValueError("size must be >= 0")
        self.__size = sizze
