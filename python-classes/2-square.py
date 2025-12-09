#!/usr/bin/python3
"""This module will intrduce a square class with size attribute

Attribute should have an positive integer private size attr"""


class Square():
    """This class will have a private + integer size attr

    It will validate the size and calculate the area"""
    def __init__(self, size=0):
        """Initialize instance with + integer size"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2
