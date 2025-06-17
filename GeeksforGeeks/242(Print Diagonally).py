'''
Print Diagonally

Give a N * N square matrix, return all the elements of its anti-diagonals
from top to bottom.

Example 1:

Input:
N = 2
A = [[1, 2],
     [3, 4]]
Output:
1 2 3 4
Explanation: Topmost anti-diagonal is [[1, ],
                                       [ , ]]
Next anti-diagonal is [[ , 2],
â€‹                       [3,  ]]
and the last anti-diagonal is [[ ,  ],
â€‹                               [ , 4]]
Hence, elements will be returned in the
order {1, 2, 3, 4}.

Example 2:

Input:
N = 3
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
Output:
1 2 4 3 5 7 6 8 9

Your Task:
You don't need to read input or print anything. Your task is to
complete the function downwardDigonal() which takes an integer N and
a 2D matrix A[ ][ ] as input parameters and returns the list of all
elements of its anti-diagonals from top to bottom.

Expected Time Complexity: O(N*N)
Expected Auxillary Space: O(N*N)

Constraints:
1 ≤ N, M ≤ 103
0 ≤ A[i][j] ≤ 106
'''

def downwardDigonal(n,A):
    dict1={}
    for i in range(n):
        for j in range(n):
            sum1=i+j
            if sum1 not in dict1:
                dict1[sum1]=[A[i][j]]
            else:
                dict1[sum1].append(A[i][j])
    # print(dict1)
    res=[]
    for i,j in dict1.items():
        res.extend(j)
    return res


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # matrix=[]
        # for i in range(n):
        #     row=list(map(int,input().split()))
        #     matrix.append(row)
        # n=3
        # matrix=[[1,2,3],[4,5,6],[7,8,9]]
        n=2
        matrix=[[1,2],[3,4]]
        ans=downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=' ')
        print()