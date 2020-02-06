"""
Program: CS 115 Lab 4c
Author: Your name
Description: This program draws a graph and determines whether
   consecutive points are increasing or decreasing.
"""
from graphics import *


def main():
    window_height = 600
    window = GraphWin('Graph', 800, window_height)

    # Open the input file and read the number of points
    pointsfile = open("E:\\School Stuff\\CS 115\\lab 4\\points-test.txt", "r")
    num_points = int(pointsfile.readline())

    x = 20
    first_y = int(pointsfile.readline())  # get the first y-coordinate
    first_point = Point(x, window_height - first_y)

    for i in range(1, num_points): # we got the first point already
                                   #   so the range starts with 1
        # Read the next point and update x
        second_y = int(pointsfile.readline())
        x += 10
        second_point = Point(x, window_height - second_y)

        print("y of first point = ", first_y, ", y of second point = ", second_y, sep = "")

        # TODO: Complete this if-statement
        if (second_y > first_y):
            print("increasing")
        else:
            print("decreasing")

        line = Line(first_point, second_point)
        line.setOutline('Orange')
        line.draw(window)

        circle = Circle(first_point, 1)
        circle.draw(window)

        # use the second point of this line as the first point for the next
        first_point = second_point
        first_y = second_y

    circle = Circle(first_point, 1)
    circle.draw(window)

    window.getMouse()
    window.close()


main()
