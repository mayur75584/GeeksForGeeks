'''
Question is in IPA sample questions pdf
Question number - 4

Sample Input-
3
1
Rajesh
5
10
20
2
Venkat
5
20
30
3
Brahma
10
10
10

3
EL
10

Sample Output-
10
Granted
'''

class Employee:

    def __init__(self,empno,empname,leaves):
        self.empno = empno
        self.empname = empname
        self.leaves = leaves

class Company:

    def __init__(self,cname,emps):
        self.cname = cname
        self.emps = emps

    def display_leave(self,empnumber,leavetype):

        for i in self.emps:
            if i.empno==empnumber:
                return i.leaves[leavetype]

    def leave_application(self,empnumber,leavetype,noOfleaves):
        check=False
        for i in self.emps:
            if i.empno == empnumber:
                for lt,nl in i.leaves.items():
                    if lt==leavetype and nl>=noOfleaves:
                        check=True
        if check==True:
            return 'Granted'
        else:
            return 'Rejected'


n=int(input())
# list_obj = [] #Here if you use list you will get error because all the objects you have to store in emps list of class Company and if you append all objects in list_obj and you append list_obj in emps list of Comapny class this will give error that list object dont have attribute empno,empname,leaves as it will become list of list
c=Company("ABC",emps=[])
for i in range(n):
    empno=int(input())
    empname=input()
    leaves={}
    leaves["CL"]=int(input())
    leaves["EL"]=int(input())
    leaves["SL"]=int(input())
    # list_obj.append(Employee(empno,empname,leaves)) #this will give error
    z=Employee(empno,empname,leaves)

c.emps.append(z)
empnumber=int(input())
leavetype=input()
noOfleaves=int(input())

answer1=c.display_leave(empnumber,leavetype)
answer2=c.leave_application(empnumber,leavetype,noOfleaves)
print(answer1)
print(answer2)

'Practice'

# class Employee:
#     def __init__(self,empno,empname,leaves):
#         self.empno = empno
#         self.empname = empname
#         self.leaves = leaves
# class Company:
#     def __init__(self,cname,emps):
#         self.cname = cname
#         self.emps = emps
#
#     def display_leave(self,employee_number,leave_type):
#         res=0
#         for i in self.emps:
#             if i.empno==employee_number:
#                 res=i.leaves[leave_type]
#                 return res
#
#
#     def leave_application(self,employee_number,leave_type,noOfLeaves):
#         check=False
#         for i in self.emps:
#             if i.empno==employee_number:
#                 x=i.leaves[leave_type]
#                 if x>=noOfLeaves:
#                     check=True
#         if check==True:
#             return 'Granted'
#         else:
#             return 'Rejected'
#
#
# if __name__ == '__main__':
#     n=int(input())
#     c=Company("XYZ",emps=[])
#     for i in range(n):
#         leaves={}
#         empno=int(input())
#         empname=input()
#         leaves["EL"]=int(input())
#         leaves["SL"]=int(input())
#         leaves["CL"]=int(input())
#         e=Employee(empno,empname,leaves)
#     # c=Company("XYZ",emps=[]) #If you mention here it will not get run properly
#     c.emps.append(e)
#
#     employee_number = int(input())
#     leave_type = input()
#     noOfLeaves = int(input())
#
#     ans1=c.display_leave(employee_number,leave_type)
#     ans2=c.leave_application(employee_number,leave_type,noOfLeaves)
#     print(ans1)
#     print(ans2)


