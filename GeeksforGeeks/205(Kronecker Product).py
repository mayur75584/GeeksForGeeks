'''
Kronecker Product
Given a n*m matrix A and a p*q matrix B,
their Kronecker product C = A tensor B, also called their matrix direct product,
is an (np)*(mq) matrix.
A tensor B
=
|a11B    a12B|
|a21B    a22B|
=
|a11b11    a11b12    a12b11    a12b12|
|a11b21    a11b22    a12b21    a12b22|
|a11b31    a11b32    a12b31    a12b32|
|a21b11    a21b12    a22b11    a22b12|
|a21b21    a21b22    a22b21    a22b22|
|a21b31    a21b32    a22b31    a22b32|



Example 1:

Input:
n = 2, m = 2
p = 2, q = 2
A = {{1, 2},
     {3, 4}}
B = {{0, 5},
     {6, 7}}
Output: {{0, 5, 0, 10},
         {6, 7, 12, 14},
         {0, 15, 0, 20},
         {18, 21, 24, 28}}
Explaination: If the multiplication process
is followed then this will be the answer.



Your Task:
You do not need to read input or print anything. Your task is to complete the function kroneckerProduct() which takes n, m, p, q and A and B as input parameters and returns the resultant matrix.



Expected Time Complexity: O(n*m*p*q)
Expected Auxiliary Space: O(n*m*p*q)



Constraints:
1 ≤ n, m, p, q ≤ 20
1 ≤ A[i][j], B[i][j] ≤ 100
'''
class Solution:
    def kroneckerProduct(self,n,m,p,q,A,b):
        c=[[0 for j in range(m*q)]for i in range(n*p)]
        matrix=[]

        for i in range(0,n):
            for k in range(0,p):
                x=[]
                for j in range(0,m):
                    for l in range(0,q):
                        c[i+l+1][j+k+1]=A[i][j]*B[k][l]
                        # print(c[i+l+1][j+k+1],end=' ')
                        z=c[i+l+1][j+k+1]
                        x.append(z)
                matrix.append(x)
        # print(c)
        # print(matrix)
        # print(matrix)
        return matrix
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n,m,p,q=map(int,input().split())
        # A=[]
        # for i in range(n):
        #     A.append(list(map(int,input().split())))
        # B=[]
        # for j in range(p):
        #     B.append(list(map(int,input().split())))
        n,m,p,q=2,2,2,2
        A=[[1,2],[3,4]]
        B=[[0,5],[6,7]]

        ob=Solution()
        ans=ob.kroneckerProduct(n,m,p,q,A,B)
        for i in range(n*p):
            for j in range(m*q):
                print(ans[i][j],end=' ')
            print()

