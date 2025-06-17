'''
Boundary traversal of matrix
You are given a matrix of dimensions n x m.
The task is to perform boundary traversal on the matrix in a clockwise manner.

Example 1:
Input:
n = 4, m = 4
matrix[][] = {{1, 2, 3, 4},
         {5, 6, 7, 8},
         {9, 10, 11, 12},
         {13, 14, 15,16}}
Output: 1 2 3 4 8 12 16 15 14 13 9 5
Explanation:
The matrix is:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
The boundary traversal is:
1 2 3 4 8 12 16 15 14 13 9 5

Example 2:
Input:
n = 3, m = 4
matrrix[][] = {{12, 11, 10, 9},
         {8, 7, 6, 5},
         {4, 3, 2, 1}}
Output: 12 11 10 9 5 1 2 3 4 8

Your Task:
Complete the function boundaryTraversal() that takes matrix,
n and m as input parameters and returns the list of integers
that form the boundary traversal of the matrix in a clockwise manner.

Expected Time Complexity: O(N + M)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n, m<= 100
0 <= matrixi <= 1000
'''

class Solution:
    def BoundryTraversal(self,matrix,n,m):
        ans=[]
        ans.extend(matrix[0])
        if n==1:
            return ans
        if m==1:
            for i in range(1,n):
                ans.extend(matrix[i])
            return ans
        z=[]
        if n>1:
            for i in range(1,n-1):
                ans.append(matrix[i][-1])
                z.append(matrix[i][0])
            ans.extend(matrix[-1][::-1])
            print(z)
            ans.extend(z[::-1])
            print(ans)
            return ans
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n,m=map(int,input().split())
        # values=list(map(int,input().split()))
        # k=0
        # matrix=[]
        # for i in range(n):
        #     row=[]
        #     for j in range(m):
        #         row.append(values[k])
        #         k+=1
        #     matrix.append(row)
        # n,m=4,4
        # matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        # n,m=3,4
        # matrix=[[12,11,10,9],[8,7,6,5],[4,3,2,1]]
        # n,m=1,2
        # matrix=[[5,7]]
        n,m=4,1
        matrix=[[22],[3],[21],[2]]
        obj=Solution()
        ans=obj.BoundryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=' ')
        print()