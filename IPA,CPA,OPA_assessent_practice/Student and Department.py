'''

Screenshots is taken in mobile

Input-

5
69
12
25
John
10
82
32
Bob
46
14
76
Elisa
25
3
95
Megan
0
91
19
Dwayne

Output:
0
91
19
Dwayne
19
25
32
76
95
'''

class Student:

    def __init__(self,studentID,year,Percentage,Name):
        self.studentID = studentID
        self.year = year
        self.Percentage = Percentage
        self.Name = Name

class Department:

    def __init__(self,departmentName,studentList):
        self.departmentName = departmentName
        self.studentList = studentList

    def findMinimumStudentByPercentage(self):
        min1=9999
        name=''
        for i in self.studentList:
            if min1>i.Percentage:
                min1=i.Percentage
                name=i.Name
        result=[]
        for i in self.studentList:
            if i.Name.lower()==name.lower() and min1==i.Percentage:
                result.append(i.studentID)
                result.append(i.year)
                result.append(i.Percentage)
                result.append(i.Name)
                break

        if len(result)==0:
            return None
        else:
            return result

    def sortStudentByPercentage(self):
        result=[]
        for i in self.studentList:
            result.append(i.Percentage)
        return sorted(result)


if __name__ == '__main__':
    n=int(input())
    list_obj = []
    for i in range(n):
        studentID = int(input())
        year = int(input())
        Percentage = int(input())
        Name = input()
        s=Student(studentID,year,Percentage,Name)
        list_obj.append(s)
    d=Department("xyz",list_obj)
    answer1=d.findMinimumStudentByPercentage()
    answer2=d.sortStudentByPercentage()
    if answer1==None:
        print("No Student found")
    else:
        for i in answer1:
            print(i)
    if answer2==None:
        print("No Data Found")
    else:
        for i in answer2:
            print(i)






