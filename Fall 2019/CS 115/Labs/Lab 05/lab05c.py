"""
Program: CS 115 Lab 5c
Author: Ryan Ristine
Description: This program will read a positive integer and
    express it as the sum of powers of 2 with a '+' between each.
"""


def main():
    i_num = int(input("Enter a number: "))

    while(i_num > 0):
        n = 0
        two_to_n = 2**n

        while(two_to_n < i_num):
            n = n + 1
            two_to_n = two_to_n * 2

        if(two_to_n > i_num):
            n = n - 1
            two_to_n = two_to_n / 2

        print("2**", n, sep="", end="")

        if(two_to_n < i_num):
            print(' + ', sep="", end="")

        i_num = i_num - two_to_n



main()
