'''
Find difference between sums of two diagonals

    Difficulty Level : Basic
    Last Updated : 07 May, 2021

Given a matrix of n X n. The task is to calculate the absolute difference between the sums of its diagonal.
Examples:


Input : mat[][] = 11 2 4
                   4 5 6
                  10 8 -12
Output : 15
Sum of primary diagonal = 11 + 5 + (-12) = 4.
Sum of primary diagonal = 4 + 5 + 10 = 19.
Difference = |19 - 4| = 15.


Input : mat[][] = 10 2
                   4 5
Output : 7
'''

def func(arr):
    print(arr)
    dia1=0
    dia2=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                dia1+=arr[i][j]
            if i+j==len(arr)-1:
                dia2+=arr[i][j]
    print(dia1,dia2)
    return abs(dia1-dia2)

if __name__ == '__main__':
    n=int(input())
    arr=[]
    for i in range(n):
        z=[]
        for j in range(n):
            x=int(input())
            z.append(x)
        arr.append(z)
    res=func(arr)
    print(res)