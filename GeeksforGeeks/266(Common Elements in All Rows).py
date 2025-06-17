'''
Common Elements in All Rows

You are given a matrix Mat of N rows and M columns.
You have to find and print all the elements in a sorted order
that are common in all rows of the given matrix.

Example 1:

Input:
N = 3
M = 3
Mat[][] = {{3,2 4},{5,2,3},{9,3,4}}
Output:
{3}
Explanation:
We can clearly see that the element 3 is present
in all three rows. So, the answer will be {3}.

Example 2:

Input:
N = 2
M = 5
Mat[][] = {{3,2,6,2,1},{6,2,5,9,9}}
Output:
{2,6}
Explanation:
Here the elements 2 and 6 are present in both rows.
So, the answer will be {2,6}.



Your Task:

You don't need to read input or print anything.
Your task is to complete the function commonElements()
which takes the matrix Mat[][] and its dimensions N and M as inputs
and returns the common elements in all the rows in sorted order.


Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O()


Constraints:
1 <= N,M <= 105
-109 <= Mat[i][j] <= 109
Sum of M*N over all test cases doesn't exceed 106
'''
class Solution:
    def commonElements(self,N,M,Mat):
        if N == 1:
            return []
        res = []
        dict1 = {}
        for i in range(N):
            z = []
            for j in range(M):
                if Mat[i][j] not in z:
                    z.append(Mat[i][j])
                    if Mat[i][j] not in dict1:
                        dict1[Mat[i][j]] = 1
                    else:
                        dict1[Mat[i][j]] += 1
            z = []
        for i in Mat[-1]:
            if dict1[i] == N and i not in res:
                res.append(i)
        return res

class IntMatrix:
    def __init__(self):
        pass
    def Input(self,n,m):
        matrix=[]
        # for _ in range(n):
        #     matrix.append([int(i) for i in input().split()])
        # matrix=[[3,2,4],[5,2,3],[9,3,4]]
        # matrix=[[3,2,6,2,1],[6,2,5,9,9]]
        # matrix=[[2,-4,-5,-2,4,-5,3],[3,0,-3,1,-2,-4,-2]]
        # matrix=[[3,2,6,2,1],[6,2,5,9,9]]
        matrix=[[-1,-1,5,4,1,2,-2]]
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=' ')
class IntArray:
    def __init__(self):
        pass
    def Input(self,n):
        arr=[int(i) for i in input().split()]
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=' ')
        print()

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # M=int(input())
        # N=3
        # M=3

        # N=2
        # M=5

        # N=2
        # M=7

        # N=2
        # M=5

        N=1
        M=7
        Mat=IntMatrix().Input(N,M)

        obj=Solution()
        res=obj.commonElements(N,M,Mat)
        IntArray().Print(res)