'''
Program: CS 115 Lab 06b
Author: Ryan Ristine
Description: This asks for text and waits until the user doesn't Enter
             any more text and when that occurs it prints the average
             number of characters per word
'''
def main():
    phrase = "placeholder"
    y = 0
    z = 0
    avg = 0
    while(phrase != ""):
        phrase = input("Enter some text: ")
        words = phrase.split()
        y = len(words) + y
        x = 0
        for i in range(len(words)):
            x = len(words[i]) + x
        z = x + z
        if(y == 0):
            print("You did not enter any words")
        else:
            avg = round(z/y, 5)
    if( avg > 0):
        print("The average word length is: ", avg, sep = "")
main()
