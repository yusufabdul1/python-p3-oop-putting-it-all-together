#!/usr/bin/env python3

class Book:
    def __init__(self, title, pages, author="Unknown", genre="Unknown"):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    @property
    def page_count(self):
        return self.pages

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        self.pages = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages, Genre: {self.genre}"

    def is_long(self):
        return self.pages > 300
