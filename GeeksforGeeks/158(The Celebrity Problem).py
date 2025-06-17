'''
The Celebrity Problem

A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people,
find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j
is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.

Example 1:
Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0},
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity.

Example 2:
Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The two people at the party both
know each other. None of them is a celebrity.


Your Task:
You don't need to read input or print anything.
Complete the function celebrity() which takes the matrix M and its size N as input parameters
and returns the index of the celebrity. If no such celebrity is present, return -1.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
2 <= N <= 3000
0 <= M[][] <= 1

Hidden test case - If we get two celebrity then their will be no celebrity as two celebrity will know
each other so answer will be in that case is -1.
'''

class Solution:
    'Below is the logic with Time complexity of O(N) and Space complexity of O(1)'
    def celebrity(self,m,n):
        stack=[]
        for i in range(n):
            stack.append(i)
        while(len(stack)>=2):#when in stack there will be 1 element remain then while loop will terminate
            t1=stack.pop(-1)
            t2=stack.pop(-1)
            if m[t1][t2]==1: #then t1 cant be celebrity
                stack.append(t2)
            else:
                stack.append(t1) #then t2 cant be celebrity
        #Now since we have 1 element in stack we will check whether than 1
        #element is known by others means that celebrity is known by others
        #if so then it is not celebrity and if not knwon then it is celebrity
        k=stack[-1]
        for i in range(n):
            if i!=k:
                if(m[i][k]==0 or m[k][i]==1):
                    return -1
        return k

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # m=[]
        # for i in range(n):
        #     z=[]
        #     for j in range(n):
        #         z.append(int(input()))
        #     m.append(z)
        n=3
        m=[[0,1,0],[0,0,0],[0,1,0]]
        ob=Solution()
        print(ob.celebrity(m,n))

