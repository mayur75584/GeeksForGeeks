'''
Addition of submatrix

Given a matrix Arr of size N x M. You are given position of submatrix as X1, Y1 and X2, Y2 inside the matrix.
Find the sum of all elements inside that submatrix. Here X1, Y1, X2, Y2 are 1-based.

Example 1:

Input:
N = 5 , M = 6
Arr[][] = {{1, 2, 3, 4, 5, 6},
           {7, 8, 9, 10, 11, 12},
           {13, 14, 15, 16, 17, 18},
           {19, 20, 21, 22, 23, 24},
           {25, 26, 27, 28, 29, 30}}
X1=3, Y1=4, X2=4, Y2=5
Output: 78
Explanation: Sum from cell starting at
position (3, 4) (1-based indexing) and
ending at (4, 5) is 78.

Example 2:

Input:
N = 3, M = 3
Arr[][] = {{9, 8, 7},{4, 2, 1},{6, 5, 3}}
X1=1, Y1=2, X2=3, Y2=3
Output: 1
Explanation: Sum from cell starting at
position (1, 2) (1-based indexing) and
ending at (3, 3) is 26.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function subMatrixSum() which takes the array of booleans arr[][], n, m, x1, y1, x2 and y2 as parameters and returns an integer denoting the answer.

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N, M ≤ 103
1 ≤ Arr[N][M] ≤ 106
1 <= X1, X2 <= N
1 <= Y1, Y2 <= M
'''
class Solution:
    def subMatrixSum(self,arr,n,m,x1,y1,x2,y2):
        x1-=1
        y1-=1
        x2-=1
        y2-=1
        sum1=0
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                sum1+=arr[i][j]
        return sum1

if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n,m=map(int,input().split())
        # arr=[]
        # for i in range(n):
        #     z=list(map(int,input().split()))
        #     arr.append(z)
        # x1,y1,x2,y2=map(int,input().split())
        # n,m=5,6
        # arr=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30]]
        # x1,y1,x2,y2,=3,4,4,5
        n,m=3,3
        arr=[[9,8,7],[4,2,1],[6,5,3]]
        x1,y1,x2,y2=1,2,3,3
        ob=Solution()
        ans=ob.subMatrixSum(arr,n,m,x1,y1,x2,y2)
        print(ans)
        t-=1




