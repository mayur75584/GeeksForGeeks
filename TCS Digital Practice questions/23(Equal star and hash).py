'''
Given a string S(input consisting) of '*' and '#'. The length of the string
is variable. The task is to find the minimum number of '*' or '#' to make
it a valid string. The string is considered valid if the number of '*' and
'#' are equal. The '*' and '#' can be at any position in the string.

Note: The output will be a positive or negative integer base on number of
'*' and '#' in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0

Example 1:
Input1:
###*** -> Value of S
Output1:
0 -> number of * and # are equal

'''

def ValidString(S):
    s=S.count('*')
    h=S.count('#')
    return s-h

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        S=input()
        # S='###***'
        print(ValidString(S))