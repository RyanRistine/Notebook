"""
Program: CS 115 Lab 4a
Author: Your name
Description: This program reads a bunch of y-values from a file.
"""

def main():
    # Opens the input file - you don't have to understand this line yet
    pointsfile = open("E:\\School Stuff\\CS 115\\lab 4\\points-test.txt", "r")

    # Reads and prints the first line of the input file
    num_points = int(pointsfile.readline())
    print('Number of points:', num_points)

    # Reads and prints the points
    for i in range(0, num_points):
        y = int(pointsfile.readline())
        print('Point ', i + 1, ': ', y, sep="")

    pointsfile.close() # Closes the input file after reading it


main()
