"""
Program: CS 115 Lab 4d
Author: Ryan Ristine
Description: This program draws a graph and draws peaks in red and valleys in blue
also prints the y value of a point and if it is a valley or peak
"""
from graphics import *


def main():
    window_height = 600
    window = GraphWin('Graph', 800, window_height)

    # Open the input file and read the number of points
    pointsfile = open("points.txt", "r")
    num_points = int(pointsfile.readline())

    x = 20
    first_y = int(pointsfile.readline())   # get the first y-coordinate
    first_point = Point(x, window_height - first_y)
    x += 10
    second_y = int(pointsfile.readline())
    second_point = Point(x, window_height - second_y)

    line = Line(first_point, second_point)
    line.setOutline('Orange')
    line.draw(window)

    # TODO: Fix this if-statement
    if (second_y > first_y):
        increasing = True
    else:
        increasing = False  # in other words, we're decreasing

    if(not increasing):
        print(first_y, " is a peak", sep = "")
        circle = Circle(first_point, 3)
        circle.setFill("red")
        circle.draw(window)
    else:
        print(first_y, " is a valley", sep ="")
        circle = Circle(first_point, 3)
        circle.setFill("Blue")
        circle.draw(window)


    # Update first_y and first_point
    orig_y = first_y
    first_y = second_y
    first_point = second_point

    for i in range(2, num_points):  # since we already did first 2
       # Read the next point and update x
        x += 10
        second_y = int(pointsfile.readline())
        second_point = Point(x, window_height - second_y)

        line = Line(first_point, second_point)
        line.setOutline('Orange')
        line.draw(window)

        circle = Circle(first_point, 1)
        circle.draw(window)

        if(second_y < first_y < orig_y or orig_y < first_y < second_y):
            print('', sep = "", end = "")
        elif(increasing):
            print(first_y, " is a peak", sep = "")
            circle = Circle(first_point, 3)
            circle.setFill("red")
            circle.draw(window)
        else:
            print(first_y, " is a valley", sep ="")
            circle = Circle(first_point, 3)
            circle.setFill("Blue")
            circle.draw(window)


       # Determine if its increasing or not
        increasing = second_y > first_y  # Think about why this works!

       # second_point becomes the first point of the next line
        orig_y = first_y
        first_y = second_y
        first_point = second_point

    if (second_y < first_y):
        increasing = True
    else:
        increasing = False  # in other words, we're decreasing

    if(increasing):
        print(first_y, " is a peak", sep = "")
        circle = Circle(first_point, 3)
        circle.setFill("red")
        circle.draw(window)
    elif(not increasing):
        print(first_y, " is a valley", sep ="")
        circle = Circle(first_point, 3)
        circle.setFill("Blue")
        circle.draw(window)


    window.getMouse()
    window.close()


main()
