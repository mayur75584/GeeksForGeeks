'''
A string of comma separated numbers are given such that the numbers
4 and 7 are already present in list. Assume that 7 always comes after 4
in the given string.

Case1: num1 = add all numbers which do not lie between 4 and 7
in the input(excluding 4 and 7).

Case2: num2 = numbers formed by concatenating all numbers
from 4 to 7(including 4 and 7).

Output: Sum of num1 and num2.

Example:
    3,1,6,4,2,3,7,2
    Num1- 3+1+6+2=12
    Num2- '4'+'2'+'3'+'7'='4237'
    Output = 4237+12 = 4249

Example2:

8,6,5,3,2,4,1,2,3,7,6,4
Num1=8+6+5+3+2+6+4=34
Num2='4'+'1'+'2'+'3'+'7'='41237'
Output = 41237+34 = 41271

'''

s1=input()

s2=s1[:s1.index(str(4))]

# print(type(s2))

s3=s1[s1.index(str(7))+2:]
# print(type(s3))

s2=s2.split(',')
s3=s3.split(',')
# print(s3)
s4=s2[:len(s2)-1]
# print(s4)
a=0
for i in s4:
    a+=int(str(i))
# print(a)
b=0
for j in s3:
    b+=int(str(j))
# print(b)
num1=a+b
# print(num1)

num=s1[s1.index(str(4)):s1.index(str(7))+1]
# print(type(num))
# print(num)
num=num.split(',')
# print(num)
num2=''
for i in num:
    num2+=str(i)
# print(num2)

print(int(num2)+num1)

##################################################################################






