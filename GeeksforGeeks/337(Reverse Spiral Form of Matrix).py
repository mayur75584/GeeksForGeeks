'''
Reverse Spiral Form of Matrix

Given a matrix as 2D array. Find the reverse spiral traversal of the matrix.

Example 1:

Input: R = 3, C = 3
  a = {{9, 8, 7},
       {6, 5, 4},
       {3, 2, 1}}
Output: 5 6 3 2 1 4 7 8 9
Explanation: Spiral form of the matrix
in reverse order starts from the centre
and goes outward.


Example 2:

Input: R = 4, C = 4
  a = {{1, 2, 3, 4},
       {5, 6, 7, 8},
       {9, 10, 11, 12},
       {13, 14, 15, 16}}
Output: 10 11 7 6 5 9 13 14 15 16 12 8 4 3 2 1
Explanation:


Your Task:
You dont need to read input or print anything.
Complete the function reverseSpiral() which takes R, C
and a as input parameters and returns the matrix in reverse spiral form.

Expected Time Complexity: O(R*C)
Expected Auxiliary Space: O(R*C)

Constraints:
1 <= R,C <=100
1 <= a[R][C] <=100

'''
class Solution:
    def reverseSpiral(self,R,C,a):
        z=[]
        row=0
        col=0
        while row<R and col<C:
            for i in range(col,C):
                z.append(a[row][i])
            row=row+1
            for i in range(row,R):
                z.append(a[i][C-1])
            C=C-1
            if(row<R):
                for i in range(C-1,col-1,-1):
                    z.append(a[R-1][i])
                R=R-1
            if(col<C):
                for i in range(R-1,row-1,-1):
                    z.append(a[i][col])
                col=col+1
        return z[::-1]

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # R,C=map(int,input().split())
        # a=[]
        # for i in range(R):
        #     a.append(list(map(int,input().split())))
        # R,C=3,3
        # a=[[9,8,7],[6,5,4],[3,2,1]]
        R,C=4,4
        a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        ob=Solution()
        ans=ob.reverseSpiral(R,C,a)
        for i in range(len(ans)):
            print(ans[i],end=' ')
        print()
