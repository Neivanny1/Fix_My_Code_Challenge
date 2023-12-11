#!/usr/bin/python3
"""
Defines a square class
"""


class square():
    """
    Module that declares class square
    """

    """ class attribute: width of Square """
    width = 0

    """ class attribute: height of Square """
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Intializes class square
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Representation format"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ tests initialization of Square instance """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
