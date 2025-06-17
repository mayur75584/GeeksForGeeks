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
    z=matrix
    x=[]
    # matrix.clear()
    n=len(z[0])-1
    for i in range(len(z)):
        lst=[]
        for j in range(len(z)):
            lst.append(z[j][n])
        n-=1
        x.append(lst)
        # matrix[i],x[i]=x[i],matrix[i]
    print(x)
    matrix.clear()
    matrix+=x





if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # matrix=[]
        # for i in range(N):
        #     lst=list(map(int,input().split()))
        #     matrix.append(lst)
        N=3
        matrix=[[1,2,3],[4,5,6],[7,8,9]]
        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j],end=' ')
            print()
