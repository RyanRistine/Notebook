"""
Program: CS 115 Lab 7a
Author: Your name
Description: This program displays national flags.
"""

from graphics import *

def draw_stripe(window, top_left, bottom_right, color):
    '''Draws a rectangle in the graphics window.

    Args:
        window (GraphWin): The window used for drawing.
        top_left (Point): The coordinates of the top left corner.
        bottom_right (Point): The coordinates of the bottom right corner.
        color (str): The color to make the rectangle.

    Returns:
        None
    '''
    stripe = Rectangle(top_left, bottom_right)
    stripe.setFill(color)
    stripe.setOutline(color)
    stripe.draw(window)

def draw_sudan_flag(flag_width):
    '''Draws a Sudan flag in the graphics window.

    Args:
        flag_width (int): The width of the window.

    Returns:
        None
    '''
    flag_height = 1 / 2 * flag_width
    stripe_colors = ['red', 'white', 'black']
    stripe_height = flag_height / len(stripe_colors)

    # Open a new graphics window with the title 'Sudan flag', the
    #   width provided by the user, and the calculated height
    window = GraphWin('Sudan flag', flag_width, flag_height)
    for i in range(3):
        stripe_top_left = Point(0, i * stripe_height)
        stripe_bottom_right = Point(flag_width, (i +1) * stripe_height)
        draw_stripe(window, stripe_top_left, stripe_bottom_right, stripe_colors[i])
    triangle = Polygon(Point(0,0), Point((flag_width/3), (flag_height/2)), Point(0, flag_height))
    triangle.setFill('DarkGreen')
    triangle.setOutline('DarkGreen')
    triangle.draw(window)
    # Wait for keyboard, to close the window
    input('Press ENTER to close the flag window.')
    window.close()



def draw_russia_flag(flag_width):
    '''Draws a Russian flag in the graphics window.

    Args:
        flag_width (int): The width of the window.

    Returns:
        None
    '''
    flag_height = 2 / 3 * flag_width
    stripe_colors = ['white', 'blue', 'red']
    stripe_height = flag_height / len(stripe_colors)

    # Open a new graphics window with the title 'Russia flag', the
    #   width provided by the user, and the calculated height
    window = GraphWin('Russia flag', flag_width, flag_height)
    for i in range(3):
        stripe_top_left = Point(0, i * stripe_height)
        stripe_bottom_right = Point(flag_width, (i +1) * stripe_height)
        draw_stripe(window, stripe_top_left, stripe_bottom_right, stripe_colors[i])
    # Wait for keyboard, to close the window
    input('Press ENTER to close the flag window.')
    window.close()


def draw_france_flag(flag_width):
    '''Draws a French flag in the graphics window.

    Args:
        flag_width (int): The width of the window.

    Returns:
        None
    '''
    flag_height = 2 / 3 * flag_width
    stripe_colors = ['DarkBlue', 'white', 'red']
    stripe_width = flag_width / len(stripe_colors)

    # Open a new graphics window with the title 'French flag', the
    #   width provided by the user, and the calculated height
    window = GraphWin('French flag', flag_width, flag_height)
    for i in range(3):
        stripe_top_left = Point(i * stripe_width, 0)
        stripe_bottom_right = Point((i + 1) * stripe_width, flag_height)
        draw_stripe(window, stripe_top_left, stripe_bottom_right, stripe_colors[i])
    # Wait for keyboard, to close the window
    input('Press ENTER to close the flag window.')
    window.close()

def draw_bangladesh_flag(flag_width):
    '''Draws the national flag of Bangladesh in a graphics window.

    Args:
        flag_width (int): The width of the window.

    Returns:
        None
    '''
    flag_height = 3 / 5 * flag_width
    circle_diameter = 2 / 5 * flag_width

    # Open a new graphics window with the title 'Bangladesh flag',
    # the width passed by the caller, and the calculated height
    win = GraphWin('Bangladesh flag', flag_width, flag_height)

    # Set the window background to white
    win.setBackground('DarkGreen')

    # Set up the red circle.
    flag_center = Point(flag_width * 9/20, flag_height * 9/20)
    circle_radius = circle_diameter / 2

    # Create a circle that is centered in the middle of the flag
    # and has the specified radius
    circ = Circle(flag_center, circle_radius)

    # Turn that circle red
    circ.setFill('red')     # the inside of the circle
    circ.setOutline('red')  # the line around the circle

    # Actually draw the circle
    circ.draw(win)

    # Close?
    input('Press ENTER to close the flag window.')
    win.close()


def draw_japan_flag(flag_width):
    '''Draws the national flag of Japan in a graphics window.

    Args:
        flag_width (int): The width of the window.

    Returns:
        None
    '''
    flag_height = 2 / 3 * flag_width
    circle_diameter = 3 / 5 * flag_height

    # Open a new graphics window with the title 'Japanese flag',
    # the width passed by the caller, and the calculated height
    win = GraphWin('Japanese flag', flag_width, flag_height)

    # Set the window background to white
    win.setBackground('white')

    # Set up the red circle.
    flag_center = Point(flag_width / 2, flag_height / 2)
    circle_radius = circle_diameter / 2

    # Create a circle that is centered in the middle of the flag
    # and has the specified radius
    circ = Circle(flag_center, circle_radius)

    # Turn that circle red
    circ.setFill('red')     # the inside of the circle
    circ.setOutline('red')  # the line around the circle

    # Actually draw the circle
    circ.draw(win)

    # Close?
    input('Press ENTER to close the flag window.')
    win.close()


# --- Our main function ---
def main():
    #draw_japan_flag(600)  # Draw a Japanese flag with a width of 600 pixels
    #draw_bangladesh_flag(600)
    #draw_france_flag(600)
    #draw_russia_flag(600)
    draw_sudan_flag(600)

main()
