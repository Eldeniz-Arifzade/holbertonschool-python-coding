#!/usr/bin/python3
"""This module will introduce a square class with size attribute

Attribute should have an positive integer private size attr"""


class Square:
    """This class will have a private + integer size attr

    It will validate the size and calculate the area"""
    def __init__(self, size=0):
        """Initialize instance with size"""
        self.size = size

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, new_size):
        """Assign new_size to size"""
        if not isinstance(new_size, int):
            raise TypeError('size must be an integer')
        elif new_size < 0:
            raise ValueError('size must be >= 0')
        self.__size = new_size

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2
