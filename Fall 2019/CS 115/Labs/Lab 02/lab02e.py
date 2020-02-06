"""
Program: CS 115 Lab 2 Part E
Author: Ryan Ristine
Description: Using the graphics package, this program will draw a square of circles, based on user input.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    num_circles = int(input("How many circles would you like the edges of the square to be?: "))
    radius = int(input("What would you like the radius of the circles to be?: "))
    x = 5
    y = 5

        # Draws Left Vertical Circles
    for i in range(num_circles):
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        y = y + 2*radius
        y1 = y
        # Draws Top Horizontal circles
    y = 5
    for i in range(num_circles):
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        x = x + 2*radius
        x1 = x

    # Draws Bottom Horizontal Circles
    x = 5
    for i in range(num_circles):
        center = Point(x, y1 - 2*radius)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        x = x + 2*radius

    # Draws Right Vertical Circles
    for i in range(num_circles):
        center = Point(x1 - 2*radius, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        y = y + 2*radius
        y1 = y

    # Draws Top to Bottom Left to Right Diagonal Circles
    x = 5
    y = 5
    for i in range(num_circles):
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)

        y = y + 2*radius
        x = x + 2*radius
        y1 = y
        x1 = x
    # Draws Top to Bottom Right to Left Diagonal Circles
    y = 5
    for i in range(num_circles):
        center = Point(x1 - 2*radius, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)

        y = y + 2*radius
        x1 = x1 - 2*radius

    window.getMouse()
    window.close()


main()
