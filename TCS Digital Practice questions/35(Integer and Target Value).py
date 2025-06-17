'''
Problem Statement:-   You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.

For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: 2-1 = 1, 3-2 = 1, and 4-3 = 1.

Function Description

Write a function pairs. It must return an integer representing the number of element pairs having the required difference.

pairs has the following parameter(s):

    k: an integer, the target difference
    arr: an array of integers

Input Format

    The first line contains two space-separated integers n and k, the size of arr and the target value.
    The second line contains n space-separated integers of the array arr.

Sample Input

     5 2

     1 5 3 4 2

Sample Output

     3
'''


if __name__ == '__main__':
    # n,k=map(int,input().split())
    # arr=list(map(int,input().split()))
    # n,k=5,2
    # arr=[1,5,3,4,2]
    n,k=4,1
    arr=[1,2,3,4]
    z=[]
    for i in arr:
        x=[]
        if i+k in arr:
            x.append(i)
            x.append(i+k)
            m=tuple(x)
            if m not in z and m[::-1] not in z:
                z.append(m)
        elif i-k in arr:
            x.append(i)
            x.append(i-k)
            m=tuple(x)
            if m not in z and m[::-1] not in z:
                z.append(m)
    print(z)
    print(len(z))

'''
PrepInsta Solution

def pairs(k, arr):
    q = 0
    n = len(arr)
    arr = set(arr)
    h = len(arr) - n
    for i in arr:
        if i+k in arr:
            q+=1
    return q+h
nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().rstrip().split()))
result = pairs(k, arr)
print(result)
'''


