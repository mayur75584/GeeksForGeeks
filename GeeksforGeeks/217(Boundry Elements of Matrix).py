'''
Boundary Elements of Matrix
Given an nxn matrix .In the given matrix,
you have to find the boundary elements of the matrix.


Example 1:
Input: {{1, 2, 3}, {4, 5, 6},
{7, 8, 9}}
Output: 1 2 3 4 6 7 8 9

Example 2:
Input: {{1, 2}, {3, 4}}
Output: 1 2 3 4

Your Task:
You don't need to read or print anything.
Your task is to complete the function BoundaryElements() which takes matrix
as input parameter and returns a list containing the boundary elements
of the matrix in the same order in which they appear in the input matrix.

Expected Time Complexity: O(n2)
Expected Space Complexity: O(1)

Constraints:
1 <= n <= 100
'''

class Solution:
    def BoundryElements(self,matrix):
        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i==0 or i==len(matrix)-1:
                    res.append(matrix[i][j])
                else:
                    if j==0 or j==len(matrix[i])-1:
                        res.append(matrix[i][j])
        print(res)
        return res

if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # n=int(input())
        # matrix=[]
        # for _ in range(n):
        #     matrix.append(list(map(int,input().split())))
        # n=3
        # matrix=[[1,2,3],[4,5,6],[7,8,9]]
        n=2
        matrix=[[1,2],[3,4]]
        ob=Solution()
        ans=ob.BoundryElements(matrix)
        for _ in ans:
            print(_,end=' ')
        print()