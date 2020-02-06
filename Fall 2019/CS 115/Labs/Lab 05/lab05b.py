"""
Program: CS 115 Lab 5b
Author: Your name
Description: This program will read a positive integer and
    find the largest power of two that is less than or equal to it.
"""


def main():

    # TODO: Complete this code

    i_num = int(input("Enter a Number: "))

    n = 0
    two_to_n = 2**n

    # complete the while-loop
    while(two_to_n < i_num):
        n = n + 1
        two_to_n = two_to_n * 2

    if(two_to_n > i_num):
        n = n - 1
        two_to_n = two_to_n // 2

    print("2**", n, sep="")


main()
