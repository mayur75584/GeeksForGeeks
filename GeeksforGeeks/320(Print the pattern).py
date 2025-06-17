# import ast
#
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# '''
# Write the function list_oper that takes two list as input.
#
# Function should return a string after performing the operations specified below
#  - Check for the squares and cubes of elements in list1 is present in list2
#  - Return "Squares and Cubes are present" if squares and cubes of all elements in list1 are present in list2.
#  - Return "Squares are only present" if squares of all elements in list1 are only present in list2.
#  - Return "Cubes are only present" if cubes of all the elements in list1 are only present in list2.
#  - Return "No such pattern is present" if there are squares and cubes of any element in list1 is not present in list2
# '''
#
# def list_oper(list1,list2):
#     l=[]
#     for i in list1:
#         if( (i**2 in list2) and (i**3 in list2)):
#             l.append(0)
#         elif((i**2 in list2) and (i**3 not in list2)):
#             l.append(1)
#         elif((i**2 not in list2) and (i**3 in list2)):
#             l.append(2)
#         else:
#             l.append(3)
#     # print(set(l))
#     if set(l)=={0}:
#         return "Squares and Cubes are present"
#     elif set(l)=={1}:
#         return "Squares are only present"
#     elif set(l)=={2}:
#         return "Cubes are only present"
#     else:
#         return "No such pattern is present"
#
#
#
# '''
# Write the function amstrong which takes two numbers(num1,num2) as input. Function should return the list of amstrong numbers between num1 and num2
#
# Example : [0,1,..]
# '''
# def amstrong(num1,num2):
#     lst=[]
#     for i in range(num1,num2+1):
#         order=len(str(i))
#         sum1=0
#         original=i
#         while(i>0):
#             digit=i%10
#             sum1+=digit**order
#             i=i//10
#         if sum1==original:
#             lst.append(original)
#     return lst
#
#
#
#
#
#
# '''
# Write the function string_oper which takes a string as input and return another string after removing words that have characters repeated
#
# Input : "This is an example"
# Output : "This is an"
# '''
#
# def string_oper(string1):
#     s1=string1.split()
#     x=[]
#     for i in s1:
#         a=[]
#         b=[]
#         for j in i:
#             a.append(j)
#             if j not in b:
#                 b.append(j)
#         if a==b:
#             x.append(i)
#     return ' '.join(x)
#
#
#
#
# '''
# Write a function string_reverse which takes a string as input and return another string with each word in reversed order.
#
# Example : "START OF THE PROJECT"
# Output :  "TRATS FO EHT TCEJORP"
# '''
#
# def string_reverse(string2):
#     n=len(string2)-1
#     s1=''
#     for i in range(n,-1,-1):
#         s1+=string2[i]
#     s=s1.split()
#     s=s[::-1]
#     return " ".join(s)
#
#
#
#
# if __name__=='__main__':
#     # list1 = ast.literal_eval(input())
#     # list2 = ast.literal_eval(input())
#     # num1 = ast.literal_eval(input())
#     # num2 = ast.literal_eval(input())
#     # string1 = input()
#     # string2 = input()
#     list1=[1,2,3,4]
#     list2=[12,13,20,1,8,16,9,2,4,27,10,64]
#     num1=10
#     num2=200
#     string1='HAMMER AND TONGS'
#     string2='Here is a characteristic letter'
#     print(list_oper(list1,list2))
#     print(amstrong(num1,num2))
#     print(string_oper(string1))
#     print(string_reverse(string2))


# import ast
#
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# '''
# Create class Person
# Initialize the class with first_name,last_name
# Create a member function "Name" that returns the Full name of the person
# Type of first_name - str
# Type of last_name - str
# '''
#
#
# class Person:
#     def __init__(self):
#         self.first_name=""
#         self.last_name=""
#     def Name(self):
#         return self.first_name+' '+self.last_name
#
#
# '''
# Create another class Student that inherits the proporties of class Person
# Initialize the class variable "count" with value 0
# Initialize the class with fist_name,last_name,rollno,mark1,mark2
# class variable count should have the number of students
# Create a member function "GetStudent" that returns the fullname,rollno,total marks seperated by commas
# Type of first_name - str
# Type of last_name -str
# Type of rollno - int
# Type of mark1 - int
# Type of mark2 - int
# '''
#
#
# class Student(Person):
#     count=0
#     def __init__(self,first_name,last_name,rollno,mark1,mark2):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.rollno=rollno
#         self.mark1=mark1
#         self.mark2=mark2
#
#     def GetStudent(self):
#         Student.count+=1
#         # x=[]
#         # x.append(self.first_name+' '+self.last_name)
#         # x.append(self.rollno)
#         # x.append(self.mark1+self.mark2)
#         # self.l.append(x)
#         return self.first_name+' '+self.last_name+','+str(self.rollno)+','+str(self.mark1+self.mark2)
#
#
# '''
# Create another class Staff that inherits the proporties of class Person
# Initialize the class variable "count" with value 0
# Initialize the class with fist_name,last_name,staffnum
# class variable count should have the number of staffs
# Create a member function "GetStaff" that returns the fullname and staffnumber seperated by comma
# Type of first_name - str
# Type of last_name -str
# Type of staffnum - int
# '''
#
#
# class Staff(Person):
#         count=0
#         def __init__(self,first_name,last_name,staffnum):
#             self.first_name=first_name
#             self.last_name=last_name
#             self.staffnum=staffnum
#         def GetStaff(self):
#             Staff.count+=1
#             return (self.first_name+' '+self.last_name+','+str(self.staffnum))
#
#
#
# if __name__ == '__main__':
#     # students = ast.literal_eval(input())
#     students=[["Joseph", "Paul",1, 100,30],["Mathew","John",2,100,0]]
#     # staff = ast.literal_eval(input())
#     staff=[["Abin", "Joy", 1832],["Liza","Clare",1003]]
#     t = []
#     s = []
#     for i in staff:
#         t.append(Staff(i[0], i[1], i[2]))
#     for i in students:
#         s.append(Student(i[0], i[1], i[2], i[3], i[4]))
#
#     for i in t:
#         print(i.GetStaff())
#     print(Staff.count)
#
#     for i in s:
#         print(i.GetStudent())
#     print(Student.count)


#
# def handelExe():
#     #Write your code here
#     while(True):
#         A=[]
#         try:
#             A=list(map(int,input().split()))
#         except ValueError:
#             print("Enter a valid numbers")
#             continue
#         try:
#             if not len(A)>1:
#                 raise IndexError
#         except IndexError:
#             print("Number of Inputs should be more than one")
#             continue
#         sum1=sum(A)
#         try:
#             if sum1>100:
#                 raise Exception
#         except Exception:
#             print("Sum of the list should be less than 100")
#             print(sum1)
#             continue
#         try:
#             c=A[0]/A[1]
#             print(c)
#             break
#         except ZeroDivisionError:
#             print("Second value should not be zero")
#     try:
#         f=open("file.txt","r")
#     except OSError:
#         print("File not found")
#
#     print("Code has been executed")
#
# if __name__ == '__main__':
#     handelExe()


# def generator_sum():
#     def fib(limit):
#         a,b=0,1
#         count1=1
#         while(count1<limit+2):
#             count1+=1
#             yield a*a
#             a,b=b,a+b
#     limit=int(input())
#     sum1=0
#     for i in fib(limit):
#         sum1+=i
#     print(sum1)
#
#
#
# # Write your code here
#
# if __name__ == '__main__':
#     generator_sum()


# import collections
#
#
# # Enter your code here. Read input from STDIN. Print output to STDOUT
#
# def actionDic():
#     # print(old_dic)
#     # n=int(input())
#     keys=list(map(str,input().split()))
#     values=list(map(int,input().split()))
#     # for i in range(n):
#     #     keys.append(input())
#     #     values.append(int(input()))
#     dict1={}
#     for i in range(len(keys)):
#         dict1[keys[i]]=values[i]
#     chain=collections.ChainMap(dict1,old_dic)
#     # print(chain.maps)
#     # k=list(chain.keys())
#     # v=list(chain.values())
#     # print(k,v)
#     return printDic(chain.maps)
#
# def printDic(c):
#     for i in c:
#         for j,k in i.items():
#             print(str(k)+" is the value of the key "+str(j))
#     num1=int(input())
#     return getEven(num1)
#
# def getEven(n):
#     even=0
#     for i in range(n+1):
#         if i%2==0:
#             even+=i
#     print(even)
#
#
# if __name__ == '__main__':
#     old_dic = {'ram': 6, 'mouse': 4, 'monitor': 3}
#     actionDic()

'''
Print the pattern

Write a program that receives a number n as input and
prints it in the following format as shown below.
Like for n = 2 the pattern will be:
1*2*5*6
--3*4

Example 1:

Input: n = 3
Output:
1*2*3*10*11*12
--4*5*8*9
----6*7
Explaination: If the pattern shown in question
is followed, this will be the output.

Your Task:
You do not need to read input or print anything.
Your task is to complete the function pattern()
which takes n as input parameter and returns a list of string
where each string denotes a new line of the pattern.

Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(n2)

Constraints:
1 ≤ n ≤ 70
'''

class Solution:
    def pattern(self,n):
        lst=[]
        count1=1
        count2=2
        z=(n**2)+n
        z1=1
        c=0
        for i in range(n):
            if count1>1:
                l=''
                l+=('-'*count2)
                count2+=2
                l1=''
                for j in range(n-c):
                    l+=str(z1)+'*'
                    z1+=1
                for k in range(n-c):
                    l1+='*'+str(z)[::-1]
                    z-=1
                l=l[0:len(l)]
                l1=l1[1:len(l1)]
                l=l+l1[::-1]
                lst.append(l)
                count1+=1
            else:
                l = ''
                l1 = ''
                for j in range(n):
                    l += str(z1) + '*'
                    z1 += 1
                for k in range(n):
                    l1 += '*' + str(z)[::-1]
                    z -= 1
                l = l[0:len(l)]
                l1 = l1[1:len(l1)]
                l = l + l1[::-1]
                # print(l)
                lst.append(l)
                count1 += 1
            c+=1
        return lst


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # n=1
        # n=2
        # n=3
        # n=4
        n=5
        ob=Solution()
        ans=ob.pattern(n)
        for i in range(n):
            print(ans[i])
