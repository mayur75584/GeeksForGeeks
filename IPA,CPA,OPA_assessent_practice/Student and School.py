'''
Create a class Student with the below attributes
name of type String
sub1 of type float
sub2 of type float
sub3 of type float
Create the __init__ method which takes all parameters in the above sequence

Create a method calculateResult in the Student class
It checks if the student has scored greater than 40 in all the individual 3 subjects.
If so, it further calculates the average and returns average.

Create another class School with the below attributes
name of type String
studentDict of type dictionary Where key is a Student object and value refers to the result pass or fail
Create the __init__ method which takes all parameters in the above sequence

Define the two methods ( getStudentResult and findStudentWithHighestMarks ) in this School class

getStudentResult : This method internally calls calculateResult method of Student class to get average.
This method checks if the student average greater than 60 then it updates the student dictionary value as pass.
Displays the names of students who passed.If o student passed print 'No student passed'

findStudentWithHighestMarks This method accept the list of passed.Display the name of the highest scored student

Input - 1
3
a
45
55
65
b
65
55
65
c
25
34
43
TTC

Output1-
b
b

Input-2
3
a
95
85
65
b
65
55
65
c
25
34
43
TTC

Output-2
a
b
a

'''
class Student:

    def __init__(self,name,sub1,sub2,sub3):

        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def calculateResult(self):
        average=0
        if self.sub1>40 and self.sub2>40 and self.sub3>40:
            average=(self.sub1+self.sub2+self.sub3)/3
        return average

class School:

    def __init__(self,sch_name,studentDict):
        self.sch_name = sch_name
        self.studentDict = studentDict

    def getStudentResult(self):
        result=[]
        for i in self.studentDict:
            if i.calculateResult()>60:
                self.studentDict[i]="pass"
                result.append(i.name)
        return result

    def findStudentWithHighestMarks(self):
        max1=0
        topper=''
        for i in self.studentDict:
            average = i.calculateResult()
            if average>max1:
                max1=average
                topper=i.name
        return topper

if __name__ == '__main__':
    n=int(input())
    list_obj = {} # used dictionary to store values and by default assign with fail
    for i in range(n):
        name = input()
        sub1 = float(input())
        sub2 = float(input())
        sub3 = float(input())
        list_obj[Student(name,sub1,sub2,sub3)]='fail' #new syntax as here used dictionary
    sch_name=input()
    s=School(sch_name,list_obj)
    answer1=s.getStudentResult()
    if len(answer1)==0:
        print("No Student Passed")
    else:
        for i in answer1:
            print(i)
    print(s.findStudentWithHighestMarks())


