'''
Rotate by 90 degree

Given a square matrix[][] of size N x N. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space.

Example 1:

Input:
N = 3
matrix[][] = [[1 2 3],
              [4 5 6],
              [7 8 9]]
Output:
3 6 9
2 5 8
1 4 7

Your Task:
You only need to implement the given function rotate(). Do not read input, instead use the arguments given in the function.

Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 50
1 <= matrix[][] <= 100
'''
def rotate(matrix):
    N = len(matrix)
    matrix1 = []
    matrix2 = []
    for j in range(N - 1, -1, -1):
        for i in range(N):
            # print(matrix[i][j],end=" ")
            matrix1.append(matrix[i][j])
        matrix2.append(matrix1)
        matrix1 = []
        # print()
    # print(matrix2)
    return matrix2
    # for i in range(N):
    #     for j in range(N):
    #         print(matrix2[i][j], end=' ')
    #     print()
    # exit()

if __name__=='__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        N=int(input())
        arr=[int(x) for x in input().split()]
        matrix=[]

        for i in range(0,N*N,N):
            matrix.append(arr[i:i+N])
        z=rotate(matrix)

        for i in range(N):
            for j in range(N):
                print(z[i][j],end=' ')
            print()