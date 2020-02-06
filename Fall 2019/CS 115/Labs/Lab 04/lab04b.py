from graphics import *

def main():
    window_height = 600
    window = GraphWin('Graph', 800, window_height)

    # Open the input file and read the number of points
    pointsfile = open("E:\\School Stuff\\CS 115\\lab 4\\points-test.txt", "r")
    num_points = int(pointsfile.readline())

    x = 20
    first_y = int(pointsfile.readline())   # get the first y-coordinate
    first_point = Point(x, window_height - first_y)

    # We already have the first point, so start with 1.
    for i in range(1, num_points):
        # Read the next point and update x
        second_y = int(pointsfile.readline())
        x += 10
        second_point = Point(x, window_height - second_y)

        line = Line(first_point, second_point)
        line.setOutline('Orange')
        line.draw(window)

        circle = Circle(first_point, 1)
        circle.draw(window)

        # use the second point of this line as the first point for the next
        first_point = second_point

    circle = Circle(first_point, 1)
    circle.draw(window)

    window.getMouse()
    window.close()
main()
