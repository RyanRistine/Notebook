"""
Program: CS 115 Lab10d
Author: Ryan Ristine
Description: This program takes an input of a list and then sorts it into a
             using either a selection sort or a merge sort 
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

def find_index_of_min(L, start_index):
    '''Returns the index of the minumum element of L. (We assume L contains
    no duplicate elements, for simplicity).

    Args:
        L (list): A list of strings.

    Returns:
        int: The index of the minimum element of L.
    '''
    if L == []:
        return None
    else:
        minEl = L[start_index]
        minIn = 0
        for i in range(start_index, len(L)):
            if start_index >= len(L):
                return None
            elif L[i] < minEl:
                minEl = L[i]
                minIn = i
    return minIn
def selection_sort(L):
    '''Uses the selection sort algorithm to sort a list.
    Sorts the original list that was passed to it (has no return value).

    Args:
        L (list): The unsorted list.
    '''
    for i in range(len(L)-1):
        begin = i
        lMin = find_index_of_min(L, begin)
        store = L[begin]
        L[begin] = L[lMin]
        L[lMin] = store
        print('Swapped elements ', begin, ' and ', lMin, ' -- ', L[lMin], ' and ', L[begin], sep="" )

def merge(L, start_index, sublist_size):
    '''Merges two sublists, or two chunks of the larger list L.
    The left chunk is
      L[start_index] to L[start_index + sublist_size - 1]
    The right chunk is
      L[start_index + sublist_size] to L[start_index + 2 * sublist_size - 1]
    Modifies the original list that was passed to it (has no return value).

    Args:
        L (list): The list.
        start_index (int): The index of the first element to be merged.
        sublist_size (int): The size of the chunks to be merged.
    '''
    index_left = start_index
    left_stop_index = start_index + sublist_size
    index_right = start_index + sublist_size
    right_stop_index = min(start_index + 2 * sublist_size,
                           len(L))

    print('Merging sublists:', L[index_left:left_stop_index], 'and',
          L[index_right:right_stop_index]);

    L_tmp = []

    while (index_left < left_stop_index and
           index_right < right_stop_index):
        if L[index_left] < L[index_right]:
           L_tmp.append(L[index_left])
           index_left += 1
        else:
           L_tmp.append(L[index_right])
           index_right += 1

    if index_left < left_stop_index:
           L_tmp.extend(L[index_left : left_stop_index])
    if index_right < right_stop_index:
           L_tmp.extend(L[index_right : right_stop_index])

    L[start_index : right_stop_index] = L_tmp
    print('Merged sublist:', L_tmp, '\n')

def merge_sort(L):
    '''Sorts a list L using the merge sort algorithm.
    Sorts the original list that was passed to it (has no return value).

    Args:
        L (list): The list.
    '''
    chunksize = 1  # Start by dividing the list into N sub-lists of 1 element each
    while chunksize < len(L):
    # TODO: This starter code doesn't fully sort the list. You will finish it.

        print("\n*** Sorting sublists of size", chunksize)

        # Divide the list into pairs of chunks
        left_start_index = 0  # Start of left chunk in each pair

        # While we still have chunks to merge
        while left_start_index + chunksize < len(L):
            merge(L, left_start_index, chunksize)

            # Move to next pair of chunks
            left_start_index += 2 * chunksize

        chunksize = chunksize * 2
        print('List is now', L)

def main():
    text = readfile(input("Enter in file name: "))
    usrSort = input('Type S for selection sort and M for merge sort: ')
    usrSort = usrSort.lower()
    print("\nThe original list of cities is:")
    print_list(text)
    if usrSort == 's':
        selection_sort(text)
    elif usrSort == 'm':
        merge_sort(text)
    print("\nThe new list of cities: ")
    print_list(text)

main()
