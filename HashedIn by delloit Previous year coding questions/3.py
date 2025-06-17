'Below problem is similar to find the number of islands of geeksforgeeks'
'''
: Given a 2D matrix of 0s and 1s, you have to find number of potholes in that. 
Potholes are defined as all neighbouring 1s(including diagonals).
Input :
1 1 0 0 0
0 1 0 0 1
1 0 0 0 1
0 0 0 0 0
1 0 1 0 1
Output : 5
Explanation: follow the bold 1s, there are 5 such potholes.
1 1 0 0 0
0 1 0 0 1
1 0 0 0 1
0 0 0 0 0
1 0 1 0 1
'''

class Solution:
    def isSafe(self,grid,i,j,vis,n,m):
        return(i>=0 and i<n and j>=0 and j<m and not vis[i][j] and grid[i][j])
    def dfs(self,grid,i,j,vis):
        # grid[i][j]=0
        # #Here in gfg question we need to traverse diagonally also
        # lst=[(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
        # for row,col in lst:
        #     if(row>=0 and col>=0 and row<len(grid) and col<len(grid[row]) and grid[row][col]==1):
        #         self.dfs(grid,row,col)
        # if(i<0 or j<0 or i>=n or j>=m):
        #     return
        # if(grid[i][j]==0):
        #     return
        # #make it as visited
        # if(vis[i][j]==False):
        #     vis[i][j]=True
        #     self.dfs(grid,vis,i+1,j,n,m)
        #     self.dfs(grid,vis,i-1,j,n,m)
        #     self.dfs(grid,vis,i,j+1,n,m)
        #     self.dfs(grid,vis,i,j-1,n,m)
        #     self.dfs(grid,vis,i+1,j+1,n,m)
        #     self.dfs(grid,vis,i+1,j-1,n,m)
        #     self.dfs(grid,vis,i-1,j+1,n,m)
        #     self.dfs(grid,vis,i-1,j-1,n,m)
        rowNbr=[-1,-1,-1,0,0,1,1,1]
        colNbr=[-1,0,1,-1,1,-1,0,1]
        vis[i][j]=True
        for k in range(8):
            if(self.isSafe(grid,i+rowNbr[k],j+colNbr[k],vis,len(grid),len(grid[0]))):
                self.dfs(grid,i+rowNbr[k],j+colNbr[k],vis)

    def numIslands(self,grid):
        islands=0
        vis=[[False for j in range(len(grid[0]))]for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (vis[i][j]==False and grid[i][j]==1):
                    self.dfs(grid,i,j,vis)
                    islands+=1
        return islands

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n,m=map(int,input().split())
        # grid=[]
        # for i in range(n):
        #     grid.append(list(map(int,input().split())))
        # n,m=4,2
        # grid=[[0,1],[1,0],[1,1],[1,0]]
        # n,m=2,7
        # grid=[[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
        n,m=5,5
        grid=[[1,1,0,0,0],[0,1,0,0,1],[1,0,0,0,1],[0,0,0,0,0],[1,0,1,0,1]]
        obj=Solution()
        print(obj.numIslands(grid))