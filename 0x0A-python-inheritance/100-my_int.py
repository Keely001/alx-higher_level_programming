100-my_int.py
#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """inverts functionality"""

    def __eq__(self, value):
        """change == opeartor to != ."""
        return self.real != value

    def __ne__(self, value):
        """change != operator to ==."""
        return self.real == value
