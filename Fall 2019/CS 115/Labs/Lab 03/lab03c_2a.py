"""
Program: CS 115 Lab 3c_1
Author: Your name here.
Description: This program draws a grid of squares of random colors based on user input,
             it also tells the user which column and row of the grid of squares they click in, or it
             tells the user they clicked outside of the grid of squares
"""
from graphics import *
from random import seed, randint


def random_color():
    '''Produces a random color.

    Returns:
        str: a string representing a color.
    '''

    colors = ['blue', 'blue2', 'blue3', 'green', 'green2', 'green3',
              'orange', 'orange2', 'orange3', 'red', 'red2', 'red3',
              'purple', 'purple2', 'purple3', 'yellow', 'yellow2', 'yellow3',
              'gray', 'gray2', 'gray3', 'pink', 'pink1', 'pink2', 'pink3']
    return colors[randint(0, len(colors)-1)]


def main():
    seed()  # Initialize random number generator

    top_left_x = 100
    top_left_y = 100
    width = 60
    height = 60
    num_rows = int(input('Number of rows: '))
    num_columns = int(input('Number of columns: '))

    window = GraphWin('Lab 3B', 800, 800)
    # draws the grid of squares
    for r in range(num_rows):
        y = top_left_y + height * r
        for j in range(num_columns):
            x = top_left_x + width * j
            top_left_point = Point(x, y)
            bottom_right_point = Point(x + width, y + height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
            enclosing_rectangle.setFill(random_color())
            enclosing_rectangle.draw(window)


# This does all the click stuff, gets location of click then figures out the column/row (or lack there-of) and prints it
    for i in range(10):
        c_point = window.getMouse()
        x_c_point = c_point.getX()
        y_c_point = c_point.getY()
        nx_c_point = x_c_point - top_left_x
        ny_c_point = y_c_point - top_left_y
        colNum = (nx_c_point // width) + 1
        rowNum = (ny_c_point // height) + 1
        if (colNum <= num_columns and rowNum <= num_rows and
         top_left_x <= x_c_point <= bottom_right_point.getX() and
           top_left_y <= y_c_point <= bottom_right_point.getY()):
            print("The click at (", int(x_c_point), ", ", int(y_c_point), ") is in row ", int(rowNum), ", column ", int(colNum), ".", sep="")
        else:
            print("The click at (", int(x_c_point), ", ", int(y_c_point), ") is outside of the grid.")




    window.getMouse()
    window.close()

main()
