"""
Program: CS 115 Lab 09
Author: Your name
Description: This program will open a file and then search its contents
    using linear and binary search.
"""


def readfile(filename):
    '''Reads the entire contents of a file into a single string using
    the read() method.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The text in the file as a large, possibly multi-line, string.
    '''
    infile = open(filename, 'r')  # opens file for reading

    filetext = infile.read().splitlines()  # reads the file contents into filetext

    infile.close()  # closes the file

    return filetext  # returns text of the file, as a long string

def print_list(list_to_print):
    '''Prints the contents of a list.

    Args:
        list_to_print (list): The list to print.
    '''
    for i, item in enumerate(list_to_print):
        print(i, ': ', item, sep="")

def linear_search(search_list, value_to_find):
    '''Uses linear search to find the position of an item in a list.

    Parameters:
        search_list (list): The list.
        value_to_find (str): The item to search for.

    Returns:
        int: The position of the item in the list, or None if not found.
    '''
    for i in range(len(search_list)):
        if str(search_list[i]) == str(value_to_find):
            return i
def main():
    '''Reads and prints a file's contents.
    '''
    filename = input("Name of input file: ")
    filetext = readfile(filename)
    #print("Number of lines in file: ", len(filetext), sep="")
    print_list(filetext)
    print("\n\n")
    cityinput = 0
    while True:
        cityinput = input("Enter the name of a city: ")
        if cityinput == "quit":
            exit()
        else:
            print("The position of ", cityinput, " is:", sep ="")
            pos = linear_search(filetext, cityinput)
            print("Linear Search: ", pos, sep="", end="\n\n")
main()
