#!/usr/bin/python3
"""
Defines Square class
"""


class Square():
    """ attributes and methods for Square objects """

    """ class attribute: width of Square """
    width = 0

    """ class attribute: height of Square """
    height = 0

    def __init__(self, *args, **kwargs):
        """ initializes Square object """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string representation of the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ tests initialization of Square instance """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
