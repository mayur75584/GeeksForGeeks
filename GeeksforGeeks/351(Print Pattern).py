'''
Print Pattern

Print a sequence of numbers starting with N where A[0] = N,
without using loop, in which  A[i+1] = A[i] - 5,  until A[i] > 0.
After that A[i+1] = A[i] + 5  repeat it until A[i] = N.

Example 1:

Input: N = 16
Output: 16 11 6 1 -4 1 6 11 16
Explaination: The value decreases until it
is greater than 0. After that it increases
and stops when it becomes 16 again.

Example 2:

Input: N = 10
Output: 10 5 0 5 10
Explaination: It follows the same logic as
per the above example.

Your Task:
You do not need to read input or print anything.
Your task is to complete the function pattern()
which takes N as input parameters and returns a list containing the pattern.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 104

'''

import sys
sys.setrecursionlimit(10000)
class Solution:

    def pattern(self,N):
        res=[]
        f=[False]
        res.append(N)

        def cal(N):

            if not f[0]:
                res.append(res[-1]-5)
                if(res[-1]<=0):
                    f[0]=True
                cal(N)
            else:
                res.append(res[-1]+5)
                if res[-1]==N:
                    return
                cal(N)
        cal(N)
        return res

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # N=16
        # N=10
        N=2501
        ob=Solution()
        ans=ob.pattern(N)
        for i in ans:
            print(i,end=' ')
        print()