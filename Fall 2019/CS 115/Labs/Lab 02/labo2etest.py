"""
Program: CS 115 Lab 2 Part # -*- coding: utf-8 -*-
Author: Ryan Ristine
Description: Using the graphics package, this program wil ldraw a square of
             circles, based on user input
"""
from graphics import *

def main():
    window = GraphWin("Circles", 800, 800)

    num_circles = int(input("How many cirlces would you like the edges of the square to be?: "))
    radius = int(input("What would you liike the radius (in pixels) of the circles to be?: "))
    x = 5
    y = 5
    tl = Point(x,y)
    tr = Point(5 - radius + 2 * num_circles * radius, y)
    bL = Point(x, 5 - radius + 2 *num_circles * radius)
    br = Point(5 - radius + 2 * num_circles * radius, 5 - radius + 2 * num_circles * radius)

    def topLeft():
        for i in range(num_circles):
            x = 5
            y = 5
            center = tl
            circle = Circle(center, radius)
            circle.setOutline('red')
            circle.draw(window)
            y += 2*radius
    topLeft()

    def topRight():
        for i  in range(num_circles):
            x = 5
            y = 5
            center = tr
            circle = Circle(center, radius)
            circle.setOutline('red')
            circle.draw(window)
            x += 2*radius
    topRight()

    window.getMouse()
    window.close()

main()
