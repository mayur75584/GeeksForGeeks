'''
For explanation of output go to link of question
https://practice.geeksforgeeks.org/problems/diagonal-morning-assembly0028/1/?page=1&difficulty[]=-1&difficulty[]=0&difficulty[]=1&difficulty[]=2&status[]=unsolved&category[]=Matrix&sortBy=submissions#
'''
'''
Sort a 2D vector diagonally

Given an NxM 2D matrix, rearrange such that
Each diagonal in the lower left triangle of the rectangular grid is sorted in ascending order.
Each diagonal in the upper right triangle of the rectangular grid is sorted in descending order.
The major diagonal in the grid starting from the top-left corner is not rearranged.


Example 1:

Input:
N = 4, M = 5
matrix = {{3 6 3 8 2},
          {4 1 9 5 9},
          {5 7 2 4 8},
          {8 3 1 7 6}}
Output:
3 9 8 9 2
1 1 6 5 8
3 4 2 6 3
8 5 7 7 4

Your Task:
You don't need to read input or print anything.
Your task is to complete the function diagonalSort() which takes the matrix,
n and m as input parameter and rearranges the elements of the matrix.

Expected Time Complexity: O(NxM)
Expected Auxiliary Space: O(N+M)

Constraints:
1 <= N,M <= 104 , 1<=N*M<=105
1 <= matrix[i] <= 103
'''

class Solution:
    def diagonalSort(self,matrix,n,m):
        dict1={}
        for i in range(n):
            for j in range(m):
                if j-i not in dict1:
                    dict1[j-i]=[matrix[i][j]]
                else:
                    z=dict1[j-i]
                    z.append(matrix[i][j])
        print(dict1)
        for i in dict1:
            if i!=0:
                dict1[i]=sorted(dict1[i])
        print(dict1)
        # copy_matrix=matrix
        matrix.clear()
        for i in range(n):
            arr=[]
            for j in range(m):
                z=j-i
                if z==0:
                    arr.append(dict1[0].pop(0))
                elif z>0:
                    arr.append(dict1[z].pop(-1))
                elif z<0:
                    arr.append(dict1[z].pop(0))
            matrix.append(arr)
if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n,m=map(int,input().split())
        # matrix=[]
        # for i in range(n):
        #     a=[]
        #     for j in range(m):
        #        a.append(int(input()))
        #     matrix.append(a)
        n,m=4,5
        matrix=[[3,6,3,8,2],[4,1,9,5,9],[5,7,2,4,8],[8,3,1,7,6]]
        ob=Solution()
        ob.diagonalSort(matrix,n,m)
        for i in range(n):
            for j in range(m):
                print(matrix[i][j],end=' ')
            print()
        t-=1