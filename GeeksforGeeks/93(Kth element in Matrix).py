'''

Kth element in Matrix
Medium Accuracy: 49.98% Submissions: 18966 Points: 4

Given a N x N matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.
Example 1:

Input:
N = 4
mat[][] =     {{16, 28, 60, 64},
                   {22, 41, 63, 91},
                   {27, 50, 87, 93},
                   {36, 78, 87, 94 }}
K = 3
Output: 27
Explanation: 27 is the 3rd smallest element.


Example 2:

Input:
N = 4
mat[][] =     {{10, 20, 30, 40}
                   {15, 25, 35, 45}
                   {24, 29, 37, 48}
                   {32, 33, 39, 50}}
K = 7
Output: 30
Explanation: 30 is the 7th smallest element.



Your Task:
You don't need to read input or print anything. Complete the function kthsmallest() which takes the mat, N and K as input parameters and returns the kth smallest element in the matrix.



Expected Time Complexity: O(N*Log(N))
Expected Auxiliary Space: O(N)



Constraints:
1 <= N <= 50
1 <= mat[][] <= 10000
1 <= K <= N*N

'''

import numpy as np


def kthSmallest(mat, n, k):
    z = []
    for i in mat:
        z += i
    x = sorted(z)
    return x[k - 1]


# T=int(input())
T = 1
while (T > 0):
    # n=int(input())
    # mat=[[0 for j in range(n)] for i in range(n)]
    # line1=[int(x) for x in input().strip().split()]
    # k=int(input())
    #
    # temp=0
    # for i in range(n):
    #     for j in range(n):
    #         mat[i][j]=line1[temp]
    #         temp+=1
    n = 4
    mat = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]]
    k = 7
    print(kthSmallest(mat, n, k))
    T -= 1