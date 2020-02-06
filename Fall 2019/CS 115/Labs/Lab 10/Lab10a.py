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

def find_index_of_min(L):
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
        minEl = L[0]
        minIn = 0
        for i in range(len(L)):
            if L[i] < minEl:
                minEl = L[i]
                minIn = i
        return minIn

def main():
    text = readfile(input("Name of Input File:"))
    print_list(text)
    print(find_index_of_min([]))
    print(find_index_of_min([3, 2, 1, 0]))
    print(find_index_of_min(['A', 'Z', 'Y', 'B']))
    print(find_index_of_min(['B', 'A', 'Z', 'Y']))
main()
