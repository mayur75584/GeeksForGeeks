'Below is wrong solution, correct solution is in upasana Singh Competitve Coding Arrays'
'''
LeetCode

Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.



Example 1:

1 2 3    7 4 1
4 5 6 => 8 5 2
7 8 9    9 6 3

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

5 1 9 11     15 13 2 5
2 4 8 10  => 14 3 4 1
13 3 6 7     12 6 8 9
15 14 12 16  16 7 10 11

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]



Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000


'''

class Solution:
    def rotate(self,n,matrix):
        z=[]
        k=0
        for i in range(len(matrix)):
            x=[]
            for j in range(len(matrix[i])-1,-1,-1):
                x.append(matrix[j][k])
            z.append(x)
            k+=1
        # print(z)
        matrix.clear()
        for i in z:
            matrix.append(i)

if __name__ == '__main__':
    # n=int(input())
    # matrix=[]
    # for i in range(n):
    #     matrix.append(list(map(int,input().split())))
    n=4
    matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    ob=Solution()
    ob.rotate(n,matrix)
    for i in matrix:
        for j in i:
            print(j,end=' ')
        print()