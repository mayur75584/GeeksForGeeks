'Photos of full question is in your mobile'
'''
Input -
5
Sunita
Faculty
23000
2
Jan
4
March
6
Arun
Admin
30000
3
Feb
4
March
12
June
10
Dipak
Admin
25000
3
Jan
12
July
5
Aug
3
Balen
HR
12000
3
Jan
12
July
5
Aug
3
Tarun
HR
78000
3
Jan
12
July
5
Aug
3
18
100

Output-
Sunita False
Arun True
Dipak True
Balen True
Tarun True
8600

Input-2
5
Sunita
Faculty
23000
4
jan
4
March
6
apr
6
June
3
Arun
Admin
30000
3
jan
4
March
6
apr
6
Dipak
Admin
25000
3
jan
4
March
6
apr
6
Balen
HR
12000
3
jan
4
March
6
apr
6
Tarun
HR
78000
3
jan
4
March
6
apr
6
30
100

Output-
Sunita False
Arun False
Dipak False
Balen False
Tarun False
0

Input-
5
Amrita
Faculty
23000
4
jan
4
March
2
apr
4
june
10
Arun
Admin
30000
3
jan
4
March
6
apr
10
Dipak
Admin
25000
3
jan
4
March
6
apr
10
Balen
HR
12000
3
jan
4
March
6
apr
10
Tarun
HR
78000
3
jan
4
March
6
apr
10
15
200

Output-
Amrita True
Arun True
Dipak True
Balen True
Tarun True
20000

Input-
5
Amrita
Faculty
23000
4
jan
4
March
2
apr
4
June
10
Arun
Admin
30000
3
jan
4
March
6
apr
10
Dipak
Admin
25000
3
jan
4
March
6
apr
10
Balen
HR
12000
3
jan
4
March
6
apr
10
Tarun
HR
78000
3
jan
4
March
6
apr
10
20
0

Output-
Amrita True
Arun True
Dipak True
Balen True
Tarun True
0

class Employee:
    def __init__(self,emp_name,desgi,salary,overTimeContribution,overTimeStatus="False"):
        self.emp_name=emp_name
        self.desgi=desgi
        self.salary=salary
        self.overTimeContribution=overTimeContribution
        self.overTimeStatus=overTimeStatus

class Organization(Employee):
    def __init__(self,employee_list):
        self.employee_list = employee_list
    def overtimestatus(self,overtimethreshold):
        for i in self.employee_list:
            if(int(sum(i.overTimeContribution.values()))>=int(overtimethreshold)):
                i.overTimeStatus="True"
        return self.employee_list
    def totalamount(self,overtimehour):
        total=0
        for i in self.employee_list:
            if(i.overTimeStatus=="True"):
                total+=int(sum(i.overTimeContribution.values()))*overtimehour
        return total
a=int(input())
lst=[]
for i in range(a):
    emp_name = input()
    desgi = input()
    salary = int(input())
    b=int(input())
    dct={}
    for j in range(b):
        mon=input()
        bon=int(input())
        dct=[mon.lower()]=bon
    obj=Employee(emp_name,desgi,salary,dct)
    lst.append(obj)
obj=Organization(lst)
overtimethreshold=int(input())
rateperhour=int(input())
lst=obj.overtimestatus(overtimethreshold)

for i in lst:
    print(i.emp_name,i.overTimeStatus)
total=obj.totalamount(rateperhour)
print(total)
'''

class Employee:

    def __init__(self,employee_name,designation,salary,overTimeContribution,overTimeStatus="False"):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = overTimeStatus


class Organization:

    def __init__(self,employee_list):
        self.employee_list = employee_list

    def overTimeStatus(self,overtime_threshold):
        for i in self.employee_list:
            sum1=sum(i.overTimeContribution.values())
            if sum1>=overtime_threshold:
                i.overTimeStatus="True"
        return self.employee_list
    def totalBonus(self,rate_per_hour):
        total=0
        for i in self.employee_list:
            if i.overTimeStatus=='True':
                total+=(sum(i.overTimeContribution.values())*rate_per_hour)
        return total



n=int(input())
list_obj=[]
for i in range(n):
    employee_name = input()
    designation = input()
    salary = int(input())
    overTimeContribution = {}
    c=int(input())
    for j in range(c):
        month = input()
        overtime = int(input())
        overTimeContribution[month.lower()]=overtime
    e=Employee(employee_name,designation,salary,overTimeContribution)
    list_obj.append(e)
o=Organization(list_obj)
overtime_threshold = int(input())
rate_per_hour = int(input())
list_obj=o.overTimeStatus(overtime_threshold) #this syntax will append overTimeStatus into list of objects as we have set overTimeStatus in employee class as False by default
answer=o.totalBonus(rate_per_hour)
for i in list_obj:
    print(i.employee_name,i.overTimeStatus)
print(answer)

'Practice'

# class Employees:
#     def __init__(self,employee_name,designation,salary,overTimeContribution,overTimeStatus="False"):
#         self.employee_name = employee_name
#         self.designation = designation
#         self.salary = salary
#         self.overTimeContribution = overTimeContribution
#         self.overTimeStatus = overTimeStatus
#
# class Organization:
#     def __init__(self,employee_list):
#         self.employee_list = employee_list
#
#     def overTimeStatus(self,overTimeThreshold):
#         for i in self.employee_list:
#             z=sum(i.overTimeContribution.values())
#             if z>=overTimeThreshold:
#                 i.overTimeStatus="True"
#         return self.employee_list
#
#     def totalBonus(self,rateperhour):
#         sum1=0
#         for i in self.employee_list:
#             if i.overTimeStatus=="True":
#                 for j,k in i.overTimeContribution.items():
#                     sum1+=(k*rateperhour)
#         return sum1
#
# if __name__ == '__main__':
#     n=int(input())
#     lst_obj=[]
#     for i in range(n):
#         employee_name = input()
#         designation = input()
#         salary = int(input())
#         overTimeContribution={}
#         c=int(input())
#         for j in range(c):
#             name = input()
#             hours = int(input())
#             overTimeContribution[name]=hours
#         e=Employees(employee_name,designation,salary,overTimeContribution)
#         lst_obj.append(e)
#     o=Organization(lst_obj)
#     overTimeThreshold=int(input())
#     rateperhour=int(input())
#     lst_obj=o.overTimeStatus(overTimeThreshold)
#     ans1=o.totalBonus(rateperhour)
#     for i in lst_obj:
#         print(i.employee_name,i.overTimeStatus)
#     print(ans1)






