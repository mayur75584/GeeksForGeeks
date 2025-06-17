'''

Predict the Column
Easy Accuracy: 47.57% Submissions: 22100 Points: 2

Given a matrix(2D array) M of size N*N consisting of 0s and 1s only. The task is to find the column with maximum number of 0s.

Example:

Input:
N = 3
M[][] = {{1, 1, 0},
         {1, 1, 0},
         {1, 1, 0}}
Output:
2
Explanation:
2nd column (0-based indexing) is having
3 zeros which is maximum among all columns.



Your Task:
Your task is to complete the function columnWithMaxZero() which should return the column number with maximum number of zeros. If more than one column exists, print the one which comes first.

Constraints:
1 <= N <= 102
0 <= A[i][j] <= 1
'''


class Solution:
    def columnWithMaxZeros(self,arr,N):
        n=0
        x=[]
        for i in range(len(arr)):
            z=[]
            for j in arr:
                z.append(j[n])
            x.append(z.count(0))
            n+=1
        x1=max(x)
        res=x.index(x1)
        return res




if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        arr=[]
        for i in range(N):
            line=[int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))