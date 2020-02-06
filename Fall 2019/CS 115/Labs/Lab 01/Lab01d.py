"""
Program: CS 115 Lab 01
Author: Ryan Ristine
Decription: This program will compute the area of a square, volume of a cube,
            volume of a sphere, and the area of an equilateral triangle
            when given a length.
"""
import math

def main():
    # Get the length
    length = float(input('Enter a numeric value: '))

    # Compute the area of a square
    square_area = round(length * length, 3)
    # Compute volume of a cube
    cube_volume = round(length ** 3, 3)
    # Compute volume of a sphere
    sphere_volume = round(4/3*math.pi*length**3, 3)
    # Compute area of an equilateral triangle
    equilateral_triangle_area = round(length**2*(math.sqrt(3)/4), 3)

    print("The area of a square with side length ", length, " is ", square_area, ".", sep="")
    print("The volume of a cube with edge length ", length, " is ", cube_volume, ".", sep="")
    print("The volume of a sphere with radius ", length, " is ", sphere_volume, ".", sep="")
    print("The area of an equilateral triangle with side length ", length, " is ", equilateral_triangle_area, ".", sep="")
main()
