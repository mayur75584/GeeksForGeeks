'LeetCode Question'
'https://leetcode.com/problems/set-matrix-zeroes/submissions/'
'''
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

1 1 1     1 0 1
1 0 1  => 0 0 0
1 1 1     1 0 1

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

0 1 2 0     0 0 0 0
3 4 5 2  => 0 4 5 0
1 3 1 5     0 3 1 0


Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1



Follow up:

    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?


'''
class Solution:
    def setZeroes(self,matrix):
        col=1
        for i in range(len(matrix)):
            if(matrix[i][0]==0):
                col=0
            for j in range(1,len(matrix[0])):
                if(matrix[i][j]==0):
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,0,-1):
                if(matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0
            if(col==0):
                matrix[i][0]=0

if __name__ == '__main__':
    # r,c=map(int,input())
    # matrix=[]
    # for i in range(r):
    #     z=list(map(int,input().split()))
    #     matrix.append(z)
    # matrix=[[1,1,1],[1,0,1],[1,1,1]]
    # matrix=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]] #o/p- [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    matrix=[[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]] #o/p - [[0,0,0,0,0],[0,0,0,0,0],[2147483647,2,-9,-6,0]]
    ob=Solution()
    ob.setZeroes(matrix)
    for i in matrix:
        for j in i:
            print(j,end=' ')
        print()