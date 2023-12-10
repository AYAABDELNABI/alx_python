

"""This is a module-level documentation.

This module contains a class called Square, which defines a square by its size.

"""

class Square:
    """Represents a square.

    This class defines a square by its size.

    Attributes:
        __size (int): The size of the square.

    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2