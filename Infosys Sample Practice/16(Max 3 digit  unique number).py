'''
Consider a non-empty array. Arr containing non-zero +ve single digit integers
separated by (";").
1) Form all possible unique three number combinations with the elements of Arr.
2) Identify the maximum number(maxnum) among the three digits combinations formed.
3) Print maxnum by the total number of unique three digit combinations formed, separating them with a (';')

Assumptions:
1) Arr will contain at least 3 elements.

Note: An element present at a particular index should not be considered
more than once while forming a combination.

#1
Sample Input: 1,2,1
Sample Output: 211,3

Explanation: For input Arr all possible unique 3 digit number combinations are:
121,112,211
The maximum 3 digit number is 211. The total number of unique combinations of 3 digit numbers that can be formed is 3.
Printing 211 followed by 3 separated by (";") the output is 211,3
'''
from itertools import permutations

def convert_to_int(value):
    temp=''
    for i in value:
        temp+=str(i)
    return int(temp)


a=[1,2,1]

x=set(permutations(a,3))

# print(x)
unique_value = len(x)


max1=-1
for i in x:
    # print(i)
    new_element = convert_to_int(i)
    # print(new_element)
    if max1<=new_element:
        max1=new_element
print(str(max1)+','+str(unique_value))