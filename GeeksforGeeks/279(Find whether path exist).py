'''
Find whether path exist

Given a grid of size n*n filled with 0, 1, 2, 3.
Check whether there is a path possible from the source to destination.
You can traverse up, down, right and left.
The description of cells is as follows:

    A value of cell 1 means Source.
    A value of cell 2 means Destination.
    A value of cell 3 means Blank cell.
    A value of cell 0 means Wall.

Note: There are only a single source and a single destination.


Example 1:

Input: grid = {{3,0,3,0,0},{3,0,0,0,3}
,{3,3,3,3,3},{0,2,3,0,0},{3,0,0,1,3}}
Output: 0
Explanation: The grid is-
3 0 3 0 0
3 0 0 0 3
3 3 3 3 3
0 2 3 0 0
3 0 0 1 3
There is no path to reach at (3,1) i,e at
destination from (4,3) i,e source.

Example 2:

Input: grid = {{1,3},{3,2}}
Output: 1
Explanation: The grid is-
1 3
3 2
There is a path from (0,0) i,e source to (1,1)
i,e destination.



Your Task:
You don't need to read or print anything.
Your task is to complete the function is_Possible() which takes
the grid as input parameter and returns boolean value true
if there is a path otherwise returns false.


Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(n2)


Constraints:
1 ≤ n ≤ 500


Topic Tags
BFS
Graph
Matrix
DFS

'''

class Solution:
    def is_Possible(self,grid):
        n=len(grid)

        for i in range(n):
            for j in range(n):
                if(grid[i][j]==1):
                    return self.dfs(grid,i,j)
        return False
    def dfs(self,grid,i,j):
        #Boundry Condition
        if(i<0 or j>=len(grid[0]) or i>=len(grid) or j<0 or grid[i][j]==0):
            return False
        if(grid[i][j]==2):
            return True

        grid[i][j]=0

        return self.dfs(grid,i+1,j) or self.dfs(grid,i-1,j) or self.dfs(grid,i,j+1) or self.dfs(grid,i,j-1)

if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # n=int(input())
        # grid=[]
        # for _ in range(n):
        #     a=list(map(int,input().split()))
        #     grid.append(a)
        # n=2
        # grid=[[1,3],[3,2]]
        n=5
        grid=[[3,0,3,0,0],[3,0,0,0,3],[3,3,3,3,3],[0,2,3,0,0],[3,0,0,1,3]]
        obj=Solution()
        ans=obj.is_Possible(grid)
        if(ans):
            print("1")
        else:
            print("0")