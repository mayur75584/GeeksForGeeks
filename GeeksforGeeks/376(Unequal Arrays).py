
'''
Unequal Arrays

You are given two arrays A and B each of length N.
You can perform the following operation on array A zero or more times.

    Select any two indices i and j, 1 <= i , j <= N and i != j
    Set A[i] = A[i] + 2 and A[j] = A[j]-2

Find the minimum number of operations required to make A and B equal.

Note :

    Two arrays are said to be equal if the frequency of each element is equal in both of them.
    Arrays may contain duplicate elements.

Example 1:

Input:
N = 3
A[] = {2, 5, 6}
B[] = {1, 2, 10}
Output: 2
Explanation:
Select i = 3, j = 2, A[3] = 6 + 2 = 8 and A[2] = 5 - 2 = 3
Select i = 3, j = 2, A[3] = 8 + 2 = 10 and A[2] = 3 - 2 = 1
Now A = {2, 1, 10} and B = {1, 2, 10}

Example 2:

Input:
N = 2
A[] = {3, 3}
B[] = {9, 8}
Output: -1
Explanation:
It can be shown that A cannot be made equal to B.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function solve() which takes the 2 arrays
A[], B[] and their size N as input parameters and
returns the minimum number of moves to make A and B equal
if possible else return -1.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
-109 <= A[i] <= 109
-109 <= B[i] <= 109


View Bookmarked Problems
Topic Tags
ArraysAlgorithmslogical-thinking
'''

'''
Note -> Before and After addition and subtraction by 2 , the sum of array will be same.
        if we add or subtract 2 in even number then result will be even and same for odd.
        if number of odd and even numbers are not same in both arrays then conversion is not possible.
        
'''
'''
Diving by 4 because in one operation 4 changes are there 
'''
from typing import List
class Solution:
    def solve(self,N,A,B):
        if sum(A)!=sum(B):
            return -1
        A=sorted(A)
        B=sorted(B)

        s1,s2=0,0

        Aodd=[]
        Aeven=[]
        Bodd=[]
        Beven=[]

        for i in range(N):
            s1+=A[i]
            s2+=B[i]

            if(A[i]%2==0):
                Aeven.append(A[i])
            else:
                Aodd.append(A[i])

            if(B[i]%2==0):
                Beven.append(B[i])
            else:
                Bodd.append(B[i])

        if(s1!=s2 or len(Aeven)!=len(Beven)):
            return -1

        res=0

        for i in range(len(Aeven)):
            res += abs(Aeven[i]-Beven[i])
        for i in range(len(Bodd)):
            res += abs(Aodd[i] - Bodd[i])

        return res//4

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # A=[int(i) for i in input().split()]
        # B=[int(j) for j in input().split()]
        # N=3
        # A=[2,5,6]
        # B=[1,2,10]
        N=2
        A=[3,3]
        B=[9,8]

        obj=Solution()
        res=obj.solve(N,A,B)

        print(res)
