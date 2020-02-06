"""
Program: Lab 11
Author: Ryan Ristine
Description: This program will eventually read in a list of students
    and grades from a text file, calculate the students' averages, and
    print the list of students.
"""


class Student:
    '''A class that holds the data for an individual student.'''

    def __init__(self, name, scores):
        '''Inits the Student class.

        Args:
            name (str): The name of the student.
            scores (list): The scores for the student.
        '''
        self.name = name
        self.scores = scores

    def get_average(self):
        self.average = 0
        if self.scores == []:
            return none
        else:
            for score in self.scores:
                self.average += score
            self.average = round(self.average/len(self.scores), 5)
            return self.average

    def print(self):
        '''Prints the student info in the following format:
            name (12 characters), grades (separated by tabs),
            average (formatted to 5 decimal places).
        '''
        # Right now, just prints the student name padded out to 12 characters
        string_to_print = self.name.ljust(12)
        # Convert list of integers to strings for printing purposes
        # There are shorter ways to do this, but this is the clearest.
        for score in self.scores:
            string_to_print += '\t' + str(score)
        string_to_print += '\t' + str(self.get_average())
        print(string_to_print)


def main():
    '''A simple program to test our Student class.'''
    # Try to create and print a student with grades of 8, 9, and 10
    test_student = Student('Test', [8, 9, 10])
    test_student.print()


main()
