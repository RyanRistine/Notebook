"""
Program: CS 115 Lab 11c
Author: Ryan Ristine
Description: This program will read in a list of students
    and grades from a text file, calculate the students' averages, and
    print the list of students. As well as the overall average score.
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

def readfile(file):
    infile = open(file, 'r')
    text = infile.read().splitlines()
    infile.close()
    return text

def main():
    studentlines = readfile("E:\\School Stuff\\CS 115\\Labs\\Lab 11\\students.txt")
    #   Loop over the list of lines from the file and
    #   break each line down into a name and scores
    averages = []
    for line in studentlines:
        # TODO 1.
        # Split line into a list. If list is empty, break out of the loop.
        nameScore = line.split()
        if len(nameScore) == 0:
            break
        # TODO 2.
        # The first item in the list is the student's name
        name = nameScore[0]
        # TODO 3.
        # Convert the remaining items in the list into integers
        newScores = []
        for item in nameScore[1:]:
            newScores.append(int(item))
        # TODO 4.
        # Create a new Student variable with that name and scores
        studentInfo = Student(name, newScores)
        # TODO 5.
        # Call the Student print method to print that student's information
        averages.append(studentInfo.get_average())
        studentInfo.print()
    overallAvg = 0
    for num in averages:
        overallAvg += num
    overallAvg = round(overallAvg/len(averages), 5)
    print("\n Overall average = ", overallAvg, sep ="")

main()
