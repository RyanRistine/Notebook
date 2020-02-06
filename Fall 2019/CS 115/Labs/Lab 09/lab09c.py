"""
Program: CS 115 Lab 09
Author: Ryan Ristine
Description: This program will open a file containing a list of cities and then
    search for a city taken from a user input using linear and binary search.
    It will then print the location of the user input and the number of binary
    search iterations

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

def binary_search(search_list, value_to_find):
    first = 0
    last = len(search_list) - 1
    count = 0
    while first <= last:
        count += 1
        middle = (last + first)//2
        print(search_list[middle])
        if value_to_find == search_list[middle]:
            print("**Binary search iteration: ", count, sep="")
            return middle
        if value_to_find < search_list[middle]:
            last = middle - 1
        if value_to_find > search_list[middle]:
            first = middle + 1
    print("**Binary search iterations: ", count, sep="")
    return None


def main():
    '''Reads and prints a file's contents.
    '''
    filename = input("Name of input file: ")
    filetext = readfile(filename)
    #print("Number of lines in file: ", len(filetext), sep="")
    print("The original list of cities is:")
    print_list(filetext)
    print()
    print("After sorting, the new list is: ")
    filetext.sort()
    print_list(filetext)
    print("")
    cityinput = 0
    while True:
        cityinput = input("Enter the name of a city: ")
        if cityinput == "quit":
            exit()
        else:
            print("The position of ", cityinput, " is:", sep ="")
            posLi = linear_search(filetext, cityinput)
            print("Linear Search: ", posLi, sep="")
            posBi = binary_search(filetext, cityinput)
            print("Binary Search: ", posBi, sep="", end="\n\n" )
main()
