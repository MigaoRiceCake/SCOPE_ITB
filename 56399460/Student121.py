'''
Student121 class 

Created on Apr 20 2021

@author: Michael Tsao
'''

from Student import Student

class Student121(Student):
    '''
    Student121 class to represent each 121COM student object
    '''
    CW1weight = 0.2 # class variable for weights for the coursework 1
    CW2weight = 0.2 # class variable for weights for the coursework 2
    CW3weight = 0.6 # class variable for weights for the coursework 3
    
    CWweight = 0.7 # class variable for weights for the coursework
    EXweight = 0.3 # class variable for weights for the exam
       
    def __init__(self,dataLine):
        '''
        constructor method
        
        Parameters:
        - dataLine with following data fields
            - studID: student ID
            - name: name of student
            - test: test mark
            - iAsgn: individual assignment mark
            - gAsgn: group assignment mark
            - exam: exam mark
        '''
        studentRec=dataLine.split('_')
        
        Student.__init__(self,studentRec[0],studentRec[1])
        
        self.__test  = float(studentRec[2])
        self.__iAsgn = float(studentRec[3])
        self.__gAsgn = float(studentRec[4])
        self.__exam  = float(studentRec[5])

        if len(studentRec) != 6:
            raise ValueError('incorrect number of items')
        elif studentRec[0] == '':
            raise ValueError('invalid student ID "%s"' % studentRec[0])
        elif studentRec[1] == '':
            raise ValueError('invalid student name "%s"' % studentRec[1])
        elif float(studentRec[2]) < 0 or float(studentRec[2]) > 100:
            raise ValueError('invalid mark value "%s"' % studentRec[2])
        elif float(studentRec[3]) < 0 or float(studentRec[3]) > 100:
            raise ValueError('invalid mark value "%s"' % studentRec[3])
        elif float(studentRec[4]) < 0 or float(studentRec[4]) > 100:
            raise ValueError('invalid mark value "%s"' % studentRec[4])
        elif float(studentRec[5]) < 0 or float(studentRec[5]) > 100:
            raise ValueError('invalid mark value "%s"' % studentRec[5])
    
    def getTest(self):
        '''
        accessor method to get student test mark
        '''
        return self.__test
    
    def getIAsgmt(self):
        '''
        accessor method to get student nindividual assignment mark
        '''
        return self.__iAsgn
            
    def getGAsgmt(self):
        '''
        accessor method to get student group assignment mark
        '''
        return self.__gAsgn
    
    def getExam(self):
        '''
        accessor method to get student examination mark
        '''        
        return self.__exam    
    
    def getCoursework(self):
        '''
        accessor method to get student coursework mark
        '''        
        return Student121.CW1weight * self.getTest() + \
               Student121.CW2weight * self.getIAsgmt() + \
               Student121.CW3weight * self.getGAsgmt()
                   
    def getOverall(self):
        '''
        service method to calculate overall mark from the weighted sum of the coursework mark and the the exam mark
        '''
        return Student121.CWweight * self.getCoursework() + \
               Student121.EXweight * self.getExam()
            
    def CWOmarks(self):
        '''
        String representation of CouseWork and Overall marks
        '''
        return '%10.2f%10.2f'%(self.getCoursework(),self.getOverall())
    
    def grade(self):
        if self.getOverall() >= 0 and self.getOverall() <= 39.99:
            return "F"
        elif self.getOverall() >= 40 and self.getOverall() <= 49.99:
            return "D"
        elif self.getOverall() >= 50 and self.getOverall() <= 64.99:
            return "C"
        elif self.getOverall() >= 65 and self.getOverall() <= 74.99:
            return "B"
        elif self.getOverall() >= 75 and self.getOverall() <= 100:
            return "A"
        else:
            raise ValueError('invalid overall mark value %s in calculation:' % self.getOverall())
        
    def __str__(self):
        '''
        String representation of student object
        '''
        return '%25s%10.2f%10.2f%10.2f%10.2f'%(Student.__str__(self),self.getTest(),self.getIAsgmt(),self.getGAsgmt(),self.getExam())