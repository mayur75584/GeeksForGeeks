'O(N) Complexity'
'''
Given two non-negative integers n1 and n2, where n1<n2.
The task is to find the total number of integers in the range
interval[n1,n2](both inclusive) which have no repeated digits.

For example:
Suppose n1=11 and n2=15.
There is the number 11, which has repeated digits, but 12,13,14 and 15 have
no repeated digits. So, the output is 4.

Example1:
Input:
11 value of n1
15 value of n2
Output:
4

Example2:
Input:
101
200
Output:
72

Constratinst:
1<=n1<n2
n2<=1000

Print "INVALID INPUT", if n1>=n2
'''
def repeated_digits(n):
    a=[]
    while n!=0:
        d=n%10

        if d in a:
            return 0
        a.append(d)
        n=n//10

    return 1


def func(n1,n2):
    if n1>=n2:
        return 'INVALID INPUT'
    else:
        answer=0
        for i in range(n1,n2+1):
            answer=answer+repeated_digits(i)
        return answer


if __name__ == '__main__':
    # n1=int(input())
    # n2=int(input())
    # n1=101
    # n2=200
    n1=1
    n2=100
    result=func(n1,n2)
    print(result)