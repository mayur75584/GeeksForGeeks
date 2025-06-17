'''
Spirally traversing a matrix

Given a matrix of size r*c. Traverse the matrix in spiral form.

Example 1:

Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Explanation:

Example 2:

Input:
r = 3, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12}}
Output:
1 2 3 4 8 12 11 10 9 5 6 7
Explanation:
Applying same technique as shown above,
output for the 2nd testcase will be
1 2 3 4 8 12 11 10 9 5 6 7.


Your Task:
You dont need to read input or print anything. Complete the function spirallyTraverse() that takes matrix, r and c as input parameters and returns a list of integers denoting the spiral traversal of matrix.

Expected Time Complexity: O(r*c)
Expected Auxiliary Space: O(r*c), for returning the answer only.

Constraints:
1 <= r, c <= 100
0 <= matrixi <= 100
'''
class Solution:
    def spirallyTraverse(self,matrix,r,c):
        for i in matrix:
            for j in i:
                print(j,end=' ')
            print()
        z=[]
        row=0
        col=0
        while row<r and col<c:
            for i in range(col,c):
                # print(matrix[row][i],end=' ')
                z.append(matrix[row][i])
            row=row+1
            for i in range(row,r):
                # print(matrix[i][c-1],end=' ')
                z.append(matrix[i][c-1])
            c=c-1
            if row<r:
                for i in range(c-1,(col-1),-1):
                    # print(matrix[r-1][i],end=' ')
                    z.append(matrix[r-1][i])
                r=r-1
            if col<c:
                for i in range(r-1,row-1,-1):
                    # print(matrix[i][col],end=' ')
                    z.append(matrix[i][col])
                col=col+1
        return z







if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # r,c=map(int,input().split())
        # matrix=[]
        # for i in range(r):
        #     z=[]
        #     for j in range(c):
        #         z.append(int(input()))
        #     matrix.append(z)
        r,c=4,4
        matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        # r,c=3,4
        # matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=' ')
        print()

