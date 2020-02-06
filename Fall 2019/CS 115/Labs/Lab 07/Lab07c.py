"""
Program: CS 115 Lab 7c
Author: Ryan Ristine
Description: This program computes geometric quantities.
"""
import sys
import math


def get_numeric_val():
    '''Prompts the user for a number. Exits if the user does not
    enter a positive value; otherwise, returns the value they entered.

    Returns:
        float: The number entered by the user.
    '''
    num = float(input('Enter a positive numeric value: '))
    if num <= 0:
        sys.exit('Error: that number was not positive.')
    return num

def get_menu_choice():
    menu_choice = input("Would you like to\na. Calculate the area of a square?\nb. Calculate the area of a circle?\nc. Calculate the volume of a cube?\nd. Calculate the volume of a sphere?\ne. Calculate the area of an equilateral triangle?\nq. Quit?\n")
    menu_choice = menu_choice.lower()
    return menu_choice

def compute_square_area(side):
    return side**2


def compute_circle_area(radius):
    return math.pi * radius**2


def compute_cube_volume(edge):
    return edge**3

def compute_sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def compute_tri_area(side):
    return(side**2 * math.sqrt(3))/4

def main():
    menu_choice = get_menu_choice()  # Get the user's first choice

    while menu_choice != 'q':
        user_num = get_numeric_val()  # Get the side length (etc.)

        if (menu_choice == 'a'):
            print('The area of a square with side length ', user_num,
                  ' is ', round(compute_square_area(user_num), 5), '.', sep="")
        elif (menu_choice == 'b'):
            print('The area of a circle with radius length ', user_num,
                  ' is ', round(compute_circle_area(user_num), 5), '.', sep="")
        elif (menu_choice == 'c'):
            print('The volume of a cube with edge length ', user_num,
                  ' is ', round(compute_cube_volume(user_num), 5), '.', sep="")
        elif (menu_choice == 'd'):
            print('The volume of a sphere with radius length ', user_num,
                    ' is ', round(compute_sphere_volume(user_num), 5), '.', sep="")
        elif (menu_choice == 'e'):
            print('The area of an equilateral triangle with side length ', user_num,
                    ' is ', round(compute_tri_area(user_num), 5), '.', sep="")

        menu_choice = get_menu_choice()  # Get user's next choice


main()
