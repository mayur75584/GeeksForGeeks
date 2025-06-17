'''
Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.


'''

class Solution:
    def dfs(self,grid,i,j):
        grid[i][j]="0"
        lst=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        for row,col in lst:
            if(row>=0 and col>=0 and row<len(grid) and col<len(grid[row]) and grid[row][col]=="1"):
                self.dfs(grid,row,col)

    def numIsland(self,grid):
        islands=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    self.dfs(grid,i,j)
                    islands+=1
        return islands

if __name__ == '__main__':
    # m,n=map(int,input().split())
    # grid=[]
    # for i in range(m):
    #     grid.append(list(map(int,input().split())))
    # m,n=4,5
    # grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    m,n=4,5
    grid=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    ob=Solution()
    print(ob.numIsland(grid))