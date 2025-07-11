'''
Row with max 1s


Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:

Input:
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).


Example 2:

Input:
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).


Your Task:
You don't need to read input or print anything. Your task is to complete the function rowWithMax1s() which takes the array of booleans arr[][], n and m as input parameters and returns the 0-based index of the first row that has the most number of 1s. If no such row exists, return -1.


Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N, M ≤ 103
0 ≤ Arr[i][j] ≤ 1
'''


class Solution:
    def rowWithMax1s(self, arr, n, m):
        z = []
        for i in range(len(arr)):
            x = arr[i].count(1)
            z.append(x)
        print(z)

        if max(z) != 0:
            y = z.index(max(z))
            print(y)
            return y
        else:
            return -1


if __name__ == '__main__':
    # tc=int(input())
    tc = 1
    while (tc > 0):
        # n,m=list(map(int,input().strip().split()))
        #
        # inputLine = list(map(int,input().strip().split()))
        # arr=[[0 for j in range(m)] for i in range(n)]
        #
        # for i in range(n):
        #     for j in range(m):
        #         arr[i][j] = inputLine[i*m+j]

        n,m=4,4
        arr=[[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]

        # n,m=2,2
        # arr=[[0,0],[1,1]]

        # n, m = 2, 2
        # arr = [[0, 0], [0, 0]]

        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1