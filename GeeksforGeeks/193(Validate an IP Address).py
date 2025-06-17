'''
Validate an IP Address

Write a program to Validate an IPv4 Address. According to Wikipedia,
IPv4 addresses are canonically represented in dot-decimal notation,
which consists of four decimal numbers, each ranging from 0 to 255,
separated by dots, e.g., 172.16.254.1 .
The generalized form of an IPv4 address is (0-255).(0-255).(0-255).(0-255).
Here we are considering numbers only from 0 to 255 and
any additional leading zeroes will be considered invalid.

Your task is  to complete the function isValid which returns 1 if the ip address is valid else returns 0.
The function takes a string s as its only argument .

Example 1:

Input:
ip = 222.111.111.111
Output: 1

Example 2:

Input:
ip = 5555..555
Output: 0
Explanation: 5555..555 is not a valid
ip address, as the middle two portions
are missing.

Your Task:
Complete the function isValid() which takes the string s as an input parameter and returns 1 if this is a valid ip address otherwise returns 0.

Expected Time Complexity: O(N), N = length of string.
Expected Auxiliary Space: O(1)

Constraints:
1<=length of string <=50

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only.
As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.
'''
'Note-> All input given in comment or taken as input are very important for this problem'
import re
def isValid(s):
    z=s.split('.')
    print(z)
    regex='^0+(?!$)'
    if len(z)==4:
        for i in range(len(z)):
            s=re.sub(regex,"",z[i])
            if s==z[i]:
                if z[i]=='':
                    return 0
                elif z[i].isalpha():
                    return 0
                elif 0<=int(z[i])<=255:
                    continue
                else:
                    return 0
            else:
                return 0
            # if list(set(z[i]))==['0']:
            #
            # elif '0'<=z[i]<='255':
            #     continue
            # elif z[i]=='':
            #     return 0
    else:
        return 0
    return 1

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # s=input()
        # s='222.111.111.111'
        # s='5555..555'
        # s='111111111111'
        # s='0000.0000.0000.0000'
        # s='1...1'
        # s='256.256.256.256'
        # s='67.53.56.29'
        # s='1...1'
        s='a.b.c.e'
        if(isValid(s)):
            print(1)
        else:
            print(0)