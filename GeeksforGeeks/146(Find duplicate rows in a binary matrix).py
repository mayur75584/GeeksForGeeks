'''
Find duplicate rows in a binary matrix

Given a boolean matrix of size RxC where each cell contains either 0 or 1, find the row numbers of row (0-based) which already exists or are repeated.

Example 1:

Input:
R = 2, C = 2
matrix[][] = {{1, 0},
              {1, 0}}
Output:
1
Explanation:
Row 1 is duplicate of Row 0.


Example 2:

Input:
R = 4, C = 3
matrix[][] = {{ 1, 0, 0},
              { 1, 0, 0},
              { 1, 0, 0},
              { 0, 0, 0}}
Output:
1 2
Explanation:
Row 1 and Row 2 are duplicates of Row 0.


Your Task:
You dont need to read input or print anything. Complete the function repeatedRows() that takes the matrix as input parameter and returns a list of row numbers which are duplicate rows.


Expected Time Complexity: O(R * C)
Expected Auxiliary Space: O(R*C)


Constraints:
1 ≤ R ≤ 1000
1 ≤ C ≤ 20
0 ≤ matrix[i][j] ≤ 1
'''

class Solution:
    def repeatedRows(self,arr,n,m):
        z=[]
        f=[]
        for i in range(len(arr)):
            if arr[i] not in z:
                z.append(arr[i])
            else:
                f.append(i)
        return f


if __name__ == '__main__':
    # t=int(input())
    t=1
    while t>0:
        # n,m = map(int,input().split())
        # arr=[]
        # for i in range(n):
        #     z=list(map(int,input().split()))
        #     arr.append(z)
        # n,m=4,3
        # arr=[[1,0,0],[1,0,0],[1,0,0],[0,0,0]]
        n,m=2,2
        arr=[[1,0],[1,0]]
        ob=Solution()
        ans = ob.repeatedRows(arr,n,m)
        for x in ans:
            print(x,end=' ')
        print()
        t-=1