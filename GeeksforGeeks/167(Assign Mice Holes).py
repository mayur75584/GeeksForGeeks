'''
Assign Mice Holes

Given, N Mice and N holes are placed in a straight line.
Each hole can accommodate only 1 mouse. A mouse can stay at his position,
move one step right from x to x + 1, or move one step left from x to x -1. Any of these moves consumes 1 minute.
Write a program to assign mice to holes so that the time when the last mouse gets inside a hole is minimized.
Note: Arrays M and H are the positions of the N mice and holes.

Example 1:
Input:
N = 3
M = {4, -4, 2}
H = {4, 0, 5}
Output:
4
Explanation:
If we assign mouse at 1st index to
the hole at 1st, mouse at 2nd index
to the hole at 2nd and the third to
the hole at third. Then, the maximum
time taken will be by the 2nd mouse,
i.e. 4-0 = 4 minutes.

Example 2:

Input:
N = 2
M = {4, 2}
H = {1, 7}
Output:
3
Explanation:
If we assign mouse at 1st index to
the hole at 2nd, and mouse at 2nd index
to the hole at 1st, the maximum
time taken will be by the 2nd mouse,
i.e. 7-4 = 3 minutes.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function assignMiceHoles() which takes an Integer N  and arrays M and H as input and returns the answer.

Expected Time Complexity: O(N*log(N))
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
-105 <= M[i] , H[i] <= 105

Input -
M=[-4,2,3]
H=[0,-2,4]
Output-
2

Input-
M=[-2]
H=[-6]
Output-
4
'''

class Solution:
    def assignMiceHoles(self,N,M,H):
        if len(M)!=len(H):
            return -1
        m=sorted(M)
        h=sorted(H)
        max1=0
        for i in range(len(m)):
            if(max1<abs(m[i]-h[i])):
                max1=abs(m[i]-h[i])
        return max1
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # M=list(map(int,input().split()))
        # H=list(map(int,input().split()))
        # N=3
        # M=[4,-4,2]
        # H=[4,0,5]
        N=2
        M=[4,2]
        H=[1,7]
        ob=Solution()
        print(ob.assignMiceHoles(N,M,H))


