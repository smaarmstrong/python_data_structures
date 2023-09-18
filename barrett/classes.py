#!/usr/bin/env python3

# classes are basically defining your own data types

class Cookie:
    # __init__ constructor
    def __init__(self, color):
        self.color = color
    
    # returns color value for cookies
    def get_color(self):
        return self.color

    # use this on existing cookies
    def set_color(self, color):
        self.color = color

# initializing two cookie objects
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

# set cookie_one's color to yellow
cookie_one.set_color('yellow')
