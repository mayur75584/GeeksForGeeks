'* #'
'''
Given a string S(input consisting) of ‘*’ and ‘#’. The length of the string is variable. The task is to find the minimum number of ‘*’ or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.

Note : The output will be a positive or negative integer based on number of ‘*’ and ‘#’ in the input string.

(*>#): positive integer

(#>*): negative integer

(#=*): 0

Example 1:

Input 1:

###***   -> Value of S

Output :

0           → number of * and # are equal


'''

def func(s):

    x=s.count('*')
    x1=s.count('#')
    if x>x1:
        return x-x1
    elif x1>x:
        return x-x1
    elif x==x1:
        return 0



if __name__ == '__main__':
    s=input()
    result=func(s)
    print(result)


'Prepinsta solution'

# s=input()
#
# a=0
#
# b=0
#
# for i in s:
#
#     if i=='*':
#
#         a+=1
#
#     elif i=='#':
#
#         b+=1
#
# print(a-b)