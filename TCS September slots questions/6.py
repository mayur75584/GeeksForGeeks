'Joseph'
'''
Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment problems before the lecture. Today he got one tricky question. The problem statement is “A positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits”.

Constraints :

1<=N<=100

Example 1:

Input :

10  -> Integer

Output :

5    -> result- Integer

Explanation:

Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output will print “5”.
'''

def func(n):
    z=bin(n).replace('0b','')
    # print(z)
    x1=''
    for i in z:
        if i=='0':
            x1+='1'
        elif i=='1':
            x1+='0'
    # print(x1)
    # print(int(x1,2))
    return int(x1,2)


if __name__ == '__main__':
    n=int(input())
    result=func(n)
    print(result)

'Prepinsta solution'

# import math
#
# n=int(input())
#
# k=(1<<int(math.log2(n))+1)-1
#
# print(n^k)