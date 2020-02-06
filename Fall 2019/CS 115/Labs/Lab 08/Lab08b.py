"""
Program: CS 115 Lab 8b
Author: Ryan Ristine
Description: This program will create a magic square
   whose size is specified by the user, then read a matrix contained in
   a text file selected by the user and determine if the matrix is a magic
   square
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

def sum_row_values(matrix, row_number):
    '''Sums the values of all entries in the row given by 'row_number'.

    Args:
        matrix (list): A square, 2D array.
        row_number (int): A value in the range 0 and len(matrix)-1.

    Returns
        int: The sum of all values of the row indicated by 'row_number'.
    '''
    sum_row = 0
    for i in range(len(matrix[row_number])):
        sum_row += matrix[row_number][i]
    return sum_row

def sum_col_values(matrix, col_number):
    '''Sums the values of all entries in the column given by 'col_number'.

    Args:
        matrix (list): A 2D, square array.
        col_number (int): A value in the range 0 and len(matrix)-1.

    Returns:
        int: The sum of all values in the column indicated by 'col_number'.
    '''
    sum_col = 0
    for i in range(len(matrix)):
        sum_col += matrix[i][col_number]
    return sum_col

def sum_top_left_bottom_right_diagonal(matrix):
    '''Calculates the sum of the values at matrix[0][0],
    matrix[1][1], etc.

    Args:
        matrix (list): A square, 2D array.

    Returns:
        int: The sum of values of the top-left to bottom-right diagonal.
    '''
    sum_diag = 0
    for i in range(len(matrix)):
        sum_diag += matrix[i][i]
    return sum_diag

def sum_top_right_bottom_left_diagonal(matrix):
    '''Calculates the sum of the values at matrix[0][len(matrix)-1],
    matrix[1][len(matrix)-2], etc.

    Args:
        matrix (list): A square, 2D array.

    Returns:
        int: The sum of values of the top-right to bottom-left diagonal
    '''
    sum_diag = 0
    for i in range(len(matrix)):
        sum_diag += matrix[i][len(matrix)-1-i]
    return sum_diag
def is_magic_square(matrix):
    '''Returns True if the two dimensional array 'matrix' is a magic square;
    otherwise, returns False.

    Args:
        matrix (list): A square, 2D array.

    Returns:
        bool: True or False.
    '''
    # TODO: Complete the below code

    tlbr_sum = sum_top_left_bottom_right_diagonal(matrix)


    trbl_sum = sum_top_right_bottom_left_diagonal(matrix)

    for i in range(len(matrix)):
        sumR = 0
        sumR = sum_row_values(matrix, i)
        if sumR != tlbr_sum:
            return False
            exit()
    for j in range(len(matrix)):
        sumC = 0
        sumC = sum_col_values(matrix, j)
        if sumC != tlbr_sum:
            return False
            exit()
    return True

def read_magic_square(filename):
    '''Reads values from a file into a 2D list.

    Args:
        filename (str): The name of the file.

    Returns:
        list: A 2D list of integer values.
    '''
    infile = open(filename, 'rt')
    square = []  # start with an empty list

    for line in infile:  # read text from file
        row = []
        numbers = line.split()

        # Loop through the list of numbers.
        # Append each number to the row.
        for num in numbers:
            row.append(int(num))

        if len(row) > 0:  # Don't count blank lines
            square.append(row)  # Append the row to the 2D list

    return square

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
        print()
        if is_magic_square(list_d):
            print("The above square is a magic square")
        else:
            print("The above square is NOT a magic square ")
    file_name = input("Enter the name of a file containing a matrix of numbers: ")
    print()
    file_square = read_magic_square(file_name)
    print_2d_list(file_square)
    print()
    if is_magic_square(file_square):
        print("The above square is a magic square")
    else:
        print("The above square is NOT a magic square")
main()
