#!/usr/bin/python3
"""Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): size of Square
            x (int): x coordinate
            y (int): y coordinate
            id (int): identity
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """set size of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ class update """
        if args != 0 and len(args) is not None:
            list = ['id', 'size', 'x', 'y']
            for a in range(len(args)):
                if list[a] == 'size':
                    setattr(self, 'width', args[a])
                    setattr(self, 'height', args[a])
                else:
                    setattr(self, list[a], args[a])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of square."""
        return {
            "id": self.id, "size": self.width,
            "x": self.x, "y": self.y
        }
