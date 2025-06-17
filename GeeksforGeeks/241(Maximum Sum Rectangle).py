'''
Link of Question->https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1#

Understand Solution
Solution Link->https://www.geeksforgeeks.org/maximum-sum-rectangle-in-a-2d-matrix-dp-27/
'''

'''
Maximum sum Rectangle

Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.

Example 1:

Input:
R=4
C=5
M=[[1,2,-1,-4,-20],
[-8,-3,4,2,1],
[3,8,10,1,3],
[-4,-1,1,7,-6]]
Output:
29
Explanation:
The matrix is as follows and the
blue rectangle denotes the maximum sum
rectangle.
Thumbnail

Example 2:

Input:
R=2
C=2
M=[[-1,-2],[-3,-4]]
Output:
-1
Explanation:
Taking only the first cell is the 
optimal choice.


Your Task:
You don't need to read input or print anything. Your task is to complete the 
function maximumSumRectangle() which takes the number R, C, and the 2D matrix M as input parameters 
and returns the maximum sum submatrix.


Expected Time Complexity:O(R*R*C)
Expected Auxillary Space:O(R*C)
 

Constraints:
1<=R,C<=500
-1000<=M[i][j]<=1000
'''

class Solution:
    def kadane(self,arr,start,finish,n):
        Sum1=0
        maxSum= -999999999999
        i=None

        finish[0]= -1
        local_start=0

        for i in range(n):
            Sum1+=arr[i]
            if Sum1<0:
                Sum1=0
                local_start=i+1
            elif Sum1>maxSum:
                maxSum=Sum1
                start[0]=local_start
                finish[0]=i

        if finish[0]!=-1:
            return maxSum

        maxSum=arr[0]
        start[0]=finish[0]=0

        for i in range(1,n):
            if(arr[i]>maxSum):
                maxSum=arr[i]
                start[0]=finish[0]=i
        return maxSum

    def maximumSumRectangle(self,R,C,M):
        ROW=R
        COL=C
        maxSum,finalLeft= -999999999999,None
        finalRight,finalTop,finalBottom=None,None,None
        left,right,i=None,None,None

        temp=[None]*ROW
        Sum1=0
        start=[0]
        finish=[0]

        for left in range(COL):
            temp=[0]*ROW
            for right in range(left,COL):

                for i in range(ROW):
                    temp[i]+=M[i][right]

                Sum1=self.kadane(temp,start,finish,ROW)

                if Sum1>maxSum:
                    maxSum=Sum1
                    finalLeft=left
                    finalRight=right
                    finalTop=start[0]
                    finalBottom=finish[0]
        return maxSum

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N,M=map(int,input().split())
        # a=[]
        # for i in range(N):
        #     a.append(list(map(int,input().split())))
        # N,M=4,5
        # a=[[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]
        N,M=2,2
        a=[[-1,-2],[-3,-4]]
        ob=Solution()
        print(ob.maximumSumRectangle(N,M,a))
