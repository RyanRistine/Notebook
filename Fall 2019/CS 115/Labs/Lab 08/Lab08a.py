"""
Program: CS 115 Lab 8a
Author: Your name
Description: This program will create a magic square
   whose size is specified by the user.
"""


def create_list(rows, cols):
    '''Creates a two-dimensional array.

    Args:
        rows (int): The numbers of rows.
        cols (int): The number of columns.

    Returns:
        list: A 2D array with all values set to zero.
    '''
    two_d = []  # create an empty list
    for i in range(rows):
        two_d.append([])  # append an empty list to two_d
        for j in range(cols):
            two_d[i].append(0)   # two_d[i] is the empty list that we just created.
                                 # here, we are adding elements to it.
    return two_d


def rjust_by_n(number, n):
    '''Formats a string containing 'number', right-justified.

    Args:
        number (int): A value.
        n (int): The width of the string into which 'number' is inserted.

    Returns:
        str: A string of length n.
    '''
    return str(number).rjust(n)


def print_list(numbers):
    '''Prints a 1D list of numbers, where each number is right-justified.

    Args:
        numbers (list): A list of numbers.
    '''
    for i in range(len(numbers)):
        print( rjust_by_n(numbers[i], 4), end='')
    print()


def print_2d_list(two_d_list):
    '''Prints a 2-dimensional list in a pretty format.

    Args:
        two_d_list (list): A 2D list of numbers.
    '''
    for i in range(len(two_d_list)):
        print_list(two_d_list[i])

def build_magic_square(square):
    '''Modifies 'square' to fill it with a magic square. Modifies
    the original list (has no return value).

    Args:
        square (list): a 2D array whose number of rows and columns
                are equal and len(square) is an odd number.
    '''
    magic_value = 1
    square_size = len(square)
    row = 0
    col = square_size // 2
    square_size_squared = square_size * square_size
    while magic_value <= square_size_squared:
        square[row][col] = magic_value
        row -= 1
        col += 1
        if row < 0 and col > square_size - 1:
            row += 2
            col -= 1
        elif row < 0:
            row = square_size - 1
        elif col > square_size - 1:
            col = 0
        elif square[row][col] != 0:
            row += 2
            col -= 1

        magic_value += 1

def main():
    # TODO: your code goes here
    square_size = int(input("Enter an odd integer to build a magic square: "))
    if square_size % 2 == 0:
        print(square_size, " is not an odd integer. Terminating...", sep="")
        exit(-1)
    else:
        print()
        list_d = create_list(square_size, square_size)
        build_magic_square(list_d)
        print_2d_list(list_d)

main()
