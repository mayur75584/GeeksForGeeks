'''
Chocolate Distribution Problem
Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet.
Each packet can have a variable number of chocolates. There are M students,
the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a
student is minimum.

Example 1:
Input:
N = 8, M = 5
A = {3, 4, 1, 9, 56, 7, 9, 12}
Output: 6
Explanation: The minimum difference between
maximum chocolates and minimum chocolates
is 9 - 3 = 6 by choosing following M packets :
{3, 4, 9, 7, 9}.

Example 2:
Input:
N = 7, M = 3
A = {7, 3, 2, 4, 9, 12, 56}
Output: 2
Explanation: The minimum difference between
maximum chocolates and minimum chocolates
is 4 - 2 = 2 by choosing following M packets :
{3, 2, 4}.

Your Task:
You don't need to take any input or print anything. Your task is to complete the function findMinDiff() which
takes array A[ ], N and M as input parameters and returns the minimum possible difference between maximum number
of chocolates given to a student and minimum number of chocolates given to a student.

Expected Time Complexity: O(N*Log(N))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 105
1 ≤ Ai ≤ 109
1 ≤ M ≤ N
'''

#Note-> While using itertools.combinations for this question you get MemoryError in GFG
class Solution:
    def findMinDiff(self,A,N,M):
        'Getting TLE for below solution'
        # A.sort()
        # print(A)
        # n=len(A)-1
        # i=0
        # j=M-1
        # min1=99999
        # while(j<=n):
        #     z=A[i:j+1]
        #     print(z)
        #     x=min(z)
        #     y=max(z)
        #     if y-x<min1:
        #         min1=y-x
        #     i+=1
        #     j+=1
        # return min1

        'Below is Optimized Solution'
        A.sort()
        j=0
        min1=999999
        for i in range(M-1,N):
            k=A[i]-A[j]
            if k<min1:
                min1=k
            j+=1
        return min1


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # A=[]
        # for i in range(N):
        #     A.append(int(input()))
        # M=int(input())
        N=8
        A=[3,4,1,9,56,7,9,12]
        M=5

        # N=7
        # A=[7,3,2,4,9,12,56]
        # M=3
        solObj=Solution()
        print(solObj.findMinDiff(A,N,M))

