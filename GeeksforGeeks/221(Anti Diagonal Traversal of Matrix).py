'''
Anti Diagonal Traversal of Matrix

Give a N*N square matrix, return an array of its anti-diagonals.
Look at the example for more details.

Example 1:
Input:
N = 2
matrix[][] = {{1,2},
              {3,4}}
Output:
1 2 3 4
Explanation:
Matrix is as below:
1 2
3 4
Printing it in anti-diagonal form will lead
to the output as 1 2 3 4


Example 2:
Input:
N = 3
matrix[][] = {{1,2,3},

              {4,5,6},

              {7,8,9}}
Output:
1 2 4 3 5 7 6 8 9
Explanation:
Matrix is as below:
1 2 3
4 5 6
7 8 9
Printing it in anti-diagonal form will lead
to the output as 1 2 4 3 5 7 6 8 9

Your Task:
You dont need to read input or print anything.
Complete the function antiDiagonalPattern() that takes matrix as input
parameter and returns a list of integers in order of the values visited
in the anti-Diagonal pattern.

Expected Time Complexity: O(N * N)
Expected Auxiliary Space: O(N * N) for the resultant list only.

Constraints:
1 <= N <= 100
1 <= mat[i][j] <= 100
'''

class Solution:
    def antiDiagonalPattern(self,matrix):
        N=2*len(matrix)-1

        res=[]
        for i in range(N):
            res.append([])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res[i+j].append(matrix[i][j])
        ans=[]
        for i in res:
            ans.extend(i)
        return ans
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # matrix=[]
        # for i in range(n):
        #     matrix.append(list(map(int,input().split())))
        n=3
        matrix=[[1,2,3],[4,5,6],[7,8,9]]

        ob=Solution()
        ans=ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=' ')
        print()