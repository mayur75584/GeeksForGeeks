'''
You are given a matrix A representing a chessboard with N rows and M columns. Each square of the chessboard contains an integer
representing a points-based score. You have to place two rooks on the chessboard in such a way that they cannot attack each other and the sum of
points on their squares is maximal. Rooks in chess can attack each other only if they are in the same row or column.
'''

'''
You are given a chess board (2D array) where each square is assigned a non negative integer.
Two rooks are to be placed on the chess board such that they don't kill each other
and sum of the values of the squares they are placed in should be maximim.
Return the maximum sum.

Example:

Input:
0 1 5
3 0 5
1 4 1

Output:
9
'''
def helper(A, startRow, startCol, moveRow, moveCol, endRow, endCol):
    n = len(A)
    m = len(A[0])
    quad = [[0] * m for _ in range(n)]

    for i in range(startRow, endRow, moveRow):
        for j in range(startCol, endCol, moveCol):
            prevMax1 = float('-inf')
            if 0 <= i - moveRow < n:
                prevMax1 = quad[i - moveRow][j]
            prevMax2 = float('-inf')
            if 0 <= j - moveCol < m:
                prevMax2 = quad[i][j - moveCol]
            quad[i][j] = max(prevMax1, prevMax2, A[i][j])

    return quad
def solution(A):
    n = len(A)
    m = len(A[0])

    topLeft = helper(A, 0, 0, 1, 1, n, m)
    topRight = helper(A, 0, m - 1, 1, -1, n, -1)
    botLeft = helper(A, n - 1, 0, -1, 1, -1, m)
    botRight = helper(A, n - 1, m - 1, -1, -1, -1, -1)
    quad = [topLeft, topRight, botLeft, botRight]

    currMax = float('-inf') #float values can be used to generate an infinite integer
    for i in range(0, n):
        for j in range(0, m):
            maxR2=float('-inf')
            diagonals=((-1, -1), (-1, 1), (1, -1), (1, 1))
            for qd,dg in enumerate(diagonals):
                k,l =i+dg[0], j+dg[1]
                if 0<=k<n and 0<=l<m:
                    maxR2 = max(maxR2, quad[qd][k][l])
            currMax = max(currMax,A[i][j]+maxR2)

    return currMax

if __name__ == '__main__':
    # A=[[15,1,5],[16,3,8],[2,6,4]]
    A=[[12,12],[12,12],[0,7]]
    # A=[[1,2,14],[8,3,15]]
    print(solution(A))