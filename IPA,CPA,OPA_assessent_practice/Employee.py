'''
IPA Sample questions pdf - question number 2


Sample Input-
4
100
Rajesh
Developer
40000
101
Ayesha
Developer
41000
102
Hari
Analyst
45000
103
Aman
Manager
60000

Developer
5

Sample Output-
Rajesh 	 42000.0
Ayesha 	 43050.0
'''

class Employee:

    def __init__(self,emp_id,emp_name,emp_role,emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_role = emp_role
        self.emp_salary = emp_salary

    def increase_salary(self,percent):
        self.emp_salary+=self.emp_salary*percent*0.01

class Organisation:

    def __init__(self,org_name,emp_list):
        self.org_name = org_name
        self.emp_list = emp_list

    def calculate_increment(self,emp_role,emp_incprecentage):
        res=[]
        for i in self.emp_list:
            if i.emp_role==emp_role:
                i.increase_salary(emp_incprecentage) #calling Employee class increase_salary method
                res.append(i)
        return res


if __name__ == '__main__':
    n=int(input())
    list_obj=[]
    for i in range(n):
        emp_id=int(input())
        emp_name=input()
        emp_role=input()
        emp_salary=int(input())

        list_obj.append(Employee(emp_id,emp_name,emp_role,emp_salary))

    o=Organisation("XYZ Corp",list_obj)
    inp_role=input()
    inp_percent=int(input())
    result=o.calculate_increment(inp_role,inp_percent)
    if len(result)!=0:
        for i in result:
            print(i.emp_name," ",i.emp_salary)
    else:
        print('No employee found with given role')


'Practice'

# class Employee:
#     def __init__(self,emp_id,emp_name,emp_role,emp_salary):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_role = emp_role
#         self.emp_salary = emp_salary
#
#     def increase_salary(self,percentage):
#         self.emp_salary+=(self.emp_salary*(percentage/100))
#
#
# class Organization:
#     def __init__(self,org_name,emp_list):
#         self.org_name = org_name
#         self.emp_list = emp_list
#
#     def calculate_increment(self,employee_role,percentage):
#         z=[]
#         for i in self.emp_list:
#             if i.emp_role==employee_role:
#                 i.increase_salary(percentage)
#                 z.append(i)
#         return z
#
# if __name__ == '__main__':
#     n=int(input())
#     lst_obj=[]
#     for i in range(n):
#         emp_id=int(input())
#         emp_name=input()
#         emp_role=input()
#         emp_salary=int(input())
#         e=Employee(emp_id,emp_name,emp_role,emp_salary)
#         lst_obj.append(e)
#     o=Organization("XYZ",lst_obj)
#     employee_role=input()
#     percentage=int(input())
#     ans1=o.calculate_increment(employee_role,percentage)
#     if len(ans1)==0:
#         print("No employee found with given role")
#     else:
#         for i in ans1:
#             print(i.emp_name," ",i.emp_salary)



