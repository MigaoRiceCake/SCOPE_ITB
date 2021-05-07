'''
Student class 

Created on Apr 20 2021

@author: Michael Tsao
'''
class Student(object):
    '''
    Student class to represent each student object
    '''
    numStudent = 0 # class variable to record number of student
    
    def __init__(self,studID,name):
        '''
        constructor method
        
        Parameters:
        - studID: student ID
        - name: name of student

        NOTE: Cannot create object of class Student."""
        '''
        
        if self.__class__ == Student:
            raise NotImplementedError("Cannot create object of class Student")
        
        Student.numStudent += 1
        
        self.__studID = studID
        self.__name = name

    def getStudID(self):
        '''
        accessor method to get student ID
        '''
        return self.__studID
    
    def getName(self):
        '''
        accessor method to get student name
        '''
        return self.__name
    
    def overall(self):
        """Abstract method; derived classes must override"""

        raise NotImplementedError("Cannot call abstract method")
           
    def __str__(self):
        '''
        String representation of student object
        '''
        return '%-10s%-15s'%(self.getStudID(),self.getName())
            
