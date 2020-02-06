"""
Program: CS 115 Lab 6a
Author: Your name
Description: This program finds $1.00 words.
"""


def main():
    word = ""
    while(word != "quit"):
        word = input("Enter a word: ")
        word = word.lower()
        if(word == "quit"):
            print()
        else:
            y = 0
            for i in range(len(word)):
                y = y + int(ord(str(word[i:i+1])))-96
            print("Your word is worth $", "{0:.2f}".format(y/100), sep="")
            if(y >= 100):
                print("Congratulations!")


main()
