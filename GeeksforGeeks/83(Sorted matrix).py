'https://practice.geeksforgeeks.org/problems/sorted-matrix2333/1/?problemStatus=unsolved&page=2&category[]=Matrix&query=problemStatusunsolvedpage2category[]Matrix'
'''
Sorted matrix

Given an NxN matrix Mat. Sort all elements of the matrix.

Example 1:

Input:
N=4
Mat=[[10,20,30,40],
[15,25,35,45]
[27,29,37,48]
[32,33,39,50]]
Output:
10 15 20 25
27 29 30 32
33 35 37 39
40 45 48 50
Explanation:
Sorting the matrix gives this result.

Example 2:

Input:
N=3
Mat=[[1,5,3],[2,8,7],[4,6,9]]
Output:
1 2 3
4 5 6
7 8 9
Explanation:
Sorting the matrix gives this result.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sortedMatrix() which takes the integer N and the matrix Mat as input parameters and returns the sorted matrix.


Expected Time Complexity:O(N2LogN)
Expected Auxillary Space:O(N2)


Constraints:
1<=N<=1000
1<=Mat[i][j]<=105
'''
import numpy as np
class Solution:
    def sortedMatrix(self,N,Mat):
        arr=np.concatenate(Mat)
        # print(arr)
        x=sorted(arr)
        # print(x)
        matrix=[[0 for i in range(N)]for j in range(N)]
        count=0
        for i in range(N):
            for j in range(N):
                matrix[i][j]=int(x[count])
                count+=1
        return matrix


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        N=4
        # v=[]
        # for i in range(N):
        #     a=list(map(int,input().strip().split()))
        #     v.append(a)
        v=[[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
        ob=Solution()
        # ob.sortedMatrix(N,v)
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=' ')
            print()
