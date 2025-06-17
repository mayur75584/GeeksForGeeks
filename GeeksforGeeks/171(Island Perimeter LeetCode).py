'''
Refer the link of question for the diagram

https://leetcode.com/problems/island-perimeter/
'''
'''
Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, 
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4

Constraints:
    row == grid.length
    col == grid[i].length
    1 <= row, col <= 100
    grid[i][j] is 0 or 1.
    There is exactly one island in grid.
'''
class Solution:
    def islandPerimeter(self,grid):
        #grid[i][j]==1, then its a land
        #7 separate lands, 7*4 , 2*6(boundries are shared with another land).
        #28-12=16
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        neigh=0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]==1):
                    islands+=1

                    if(i+1<rows and grid[i+1][j]==1):
                        neigh+=1
                    if(j+1<cols and grid[i][j+1]==1):
                        neigh+=1
        return (islands*4)-(neigh*2)
if __name__ == '__main__':
    # r,c=map(int,input().split())
    # grid=[]
    # for i in range(r):
    #     x=list(map(int,input().split()))
    #     grid.append(x)
    r,c=4,4
    grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

    ob=Solution()
    print(ob.islandPerimeter(grid))