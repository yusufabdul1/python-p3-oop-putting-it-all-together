#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color="Unknown", price=0.0):
        self.brand = brand
        self._size = size
        self.color = color
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        self._size = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    def __str__(self):
        return f"{self.brand} Shoe, Size: {self.size}, Color: {self.color}, Price: ${self.price}"

    def is_expensive(self):
        return self.price > 100
