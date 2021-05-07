'''
Created on 20 Apr 2021

@author: Micahel Tsao
'''

from Student121 import Student121
import fileinput
import matplotlib.pyplot as plt
import sys

def menuItem1():
    print('')                                           # print('') for purely formatting purposes
    for i in fileinput.input(sys.argv[1]):
        sys.stdout.write(i)
    print('')                                           # print('') for purely formatting purposes

def menuItem2():        
    print('''
Stud ID   Name              CW1 mark Test mark  CW2 mark  Exam mark
====================================================================''')
    for i in studentList:
        print(i)
        
def menuItem3(): 
    print('''
Stud ID   Name              CW1 mark  Test mark  CW2 mark  Exam mark  CW mark  Overall 
======================================================================================''')
    for i in studentList:
        print(i, i.CWOmarks())
       
def menuItem4(): 
    print('''
Stud ID   Name              CW1 mark  Test mark  CW2 mark  Exam mark  CW mark  Overall 
======================================================================================''')
    for i in studentList:
        if i.getOverall() < 40:
            print(i, i.CWOmarks())

def menuItem5(): 
    gradeFreq = {'A':0,'B':0,'C':0,'D':0,'F':0}         # create 'gradeFreq' dictionary
    for i in studentList:
        if i.grade() == "F":
            gradeFreq['F'] += 1
        elif i.grade() == "D":
            gradeFreq['D'] += 1
        elif i.grade() == "C":
            gradeFreq['C'] += 1
        elif i.grade() == "B":
            gradeFreq['B'] += 1
        elif i.grade() == "A":
            gradeFreq['A'] += 1                         # append to 'gradeFreq' with grade data
        
    graph = plt.figure(figsize=(8,6))                   # define graph: figure size width x height in inches
    distPlot = graph.add_subplot(111)                   # define distPlot: 1 row 1 columns, column 1
    distPlot.bar(['A','B','C','D','F'],
            [gradeFreq['A'],
             gradeFreq['B'],
             gradeFreq['C'],
             gradeFreq['D'],
             gradeFreq['F']])                           # vertical bars to correspond with axis titles
    
    distPlot.set_xlabel('Grade')                        # x label name
    distPlot.set_ylabel('Number of Students')           # y label name
    distPlot.set_title('Grade Distribution')            # title name
    
    plt.show()

instructions = """\nEnter one of the following:
1 to print the contents of input data file
2 to print all valid input data
3 to print all students overall mark 
4 to print all students whose mark less than 40
5 to plot distribution of grade
Q to end \n"""

def main():
    while True:
        sys.stderr.flush()
        print(instructions)        
        choice = input( "Enter 1 to 5 " ) 
        sys.stdout.flush()
        
        if choice == "1":
            menuItem1()            
        elif choice == "2":
            menuItem2()
        elif choice == "3":
            menuItem3()
        elif choice == "4":
            menuItem4()
        elif choice == "5":
            menuItem5()
        elif choice == "Q":
            break

    print ("End Grade Processing App")

if __name__ == "__main__":
    studentList = []                                        # empty list to import valid input data into system
    studIDtrack = {}                                        # dictionary to track student ID duplicates

    try:
        for line in fileinput.input(sys.argv[1]):
            try:
                record = Student121(line)
                ID = record.getStudID()
                if ID in studIDtrack:                           # handling repeat entry error
                    sys.stderr.write('repeat student ID in input: '+line+'\n')
                else:
                    studIDtrack[ID] = True                      # append dictionary studIDtrack with unique values
                    studentList.append(record)                  # append list with valid input data
            except ValueError as err:
                sys.stderr.write(str(err)+' in input: '+line+'\n')
        studentList.sort(key=Student121.getName)
        main()
    
    except IndexError as error:
        sys.stderr.write('Type \"python grade.py filename\" to run program\n')