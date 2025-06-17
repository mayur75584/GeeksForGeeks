'''
First negative integer in every window of size k

Given an array A[] of size N and a positive integer K,
find the first negative integer for each and every window(contiguous subarray) of size K.

Example 1:

Input :
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output :
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6

Example 2:

Input :
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0

Your Task:
You don't need to read input or print anything.
Your task is to complete the function printFirstNegativeInteger()
which takes the array A[],
its size N and an integer K as inputs and returns the first negative number
in every window of size K starting from the first till the end.
If a window does not contain a negative integer , then return 0 for that window.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(K)

Constraints:
1 <= N <= 105
-105 <= A[i] <= 105
1 <= K <= N
'''
from collections import deque
def printFirstNegativeInteger(a,n,k):
    res=[]
    q=deque()
    for i in range(k):
        if(a[i]<0):
            q.append(i)
    for i in range(k,n):
        if len(q)==0:
            res.append(0)
        else:
            res.append(a[q[0]])

        while(len(q)!=0 and q[0]<=i-k):
            q.popleft()
        if(a[i]<0):
            q.append(i)
    if len(q)==0:
        res.append(0)
    else:
        res.append(a[q[0]])
    return res

if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # n=int(input())
        # a=list(map(int,input().split()))
        # k=int(input())
        # n=5
        # a=[-8,2,3,-6,10]
        # k=2
        n=8
        a=[12,-1,-7,8,-15,30,16,28]
        k=3
        answer=printFirstNegativeInteger(a,n,k)
        for i in answer:
            print(i,end=' ')
        print()

        T-=1