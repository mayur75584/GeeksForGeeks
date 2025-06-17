
'''
Binary matrix having maximum number of 1s

Given a binary matrix (containing only 0 and 1) of order NxN.
All rows are sorted already, We need to find the row number with the maximum number of 1s.
Also, find the number of 1s in that row.
Note:

1. In case of a tie, print the smaller row number.
2. Row number should start from 0th index.

Example 1

Input:
N=3
mat[3][3] = {0, 0, 1,
              0, 1, 1,
              0, 0, 0}
Output:
Row number = 1
MaxCount = 2
Explanation:
Here, max number of 1s is in row number 1
and its count is 2.

Example 2

Input:
N=3
mat[3][3] = {1, 1, 1,
              1, 1, 1,
              0, 0, 0}
Output:
Row number = 0
MaxCount = 3

Your Task:
You don't need to read input or print anything.
The task is to complete the function findMaxRow() which takes mat[][] as the 2D matrix and N as the size of matrix.
Your task is to find the row number with the maximum number of 1s and find the number of 1s in that row
and return the answer in a vector of size 2 where at 0th index will be the row number and at 1th index will be MaxCount.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 103
0 <= mat[][]<= 1

'''
class Solution:
    def findMaxRow(self,mat,N):
        # ind=99999999
        # max1=0
        # s=''
        # n=''
        # for i in range(N):
        #     a=mat[i]
        #     j=None
        #     if 1 in a:
        #         j=a.index(1)
        #     if j!=None:
        #         # if a.count(1)>max1:
        #         #     max1=a.count(1)
        #         #     if s=='' and n=='':
        #         #         s+=str(i)
        #         #         n+=str(a.count(1))
        #         #         ind=i
        #         #     else:
        #         #         if str(a.count(1)) in n:
        #         #             z=n.index(str(a.count(1)))
        #         #             ind=int(s[z])
        #         #         else:
        #         #             s+=str(i)
        #         #             ind=i
        #         #             n+=str(a.count(1))
        #         if a.count(1)>max1:
        #             max1=a.count(1)
        #             # s+=str(i)
        #             n+=str(a.count(1))
        #
        #     else:
        #         continue
        # return [ind,max1]
        # ind=999999
        # max1=0
        # s=''
        # for i in range(N):
        #     a=mat[i]
        #     ind1=0
        #     if 1 in a:
        #         ind1=a.index(1)
        #         c=a.count(1)
        #         if c==max1 and (str(ind1) in s):
        #             ind=s.index(str(ind1))
        #         elif c>max1:
        #             ind=i
        #             max1=c
        #         else:
        #             continue
        #         # s+=str(ind1)
        #     else:
        #         continue
        #     s+=str(ind1)
        # if ind==999999:
        #     ind=0
        # return [ind,max1]
        dict1={}
        max1=0
        for i in range(N):
            a=mat[i]
            if 1 in a:
                c=a.count(1)
                if c>max1:
                    max1=c
                    if max1 not in dict1:
                        dict1[max1]=[i]
                    else:
                        dict1[max1].append(i)
                else:
                    if c not in dict1:
                        dict1[c]=[i]
                    else:
                        dict1[c].append(i)
            else:
                continue
        if len(dict1)==0:
            return [0,0]
        max2=0
        for i in dict1.keys():
            if i>max2:
                max2=i
        ind=min(dict1[max2])
        return [ind,max2]


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # mat=[]
        # for i in range(n):
        #     A = [int(x) for x in input().split()]
        #     mat.append(A)
        # n=3
        # mat=[[0,0,1],[0,1,1],[0,0,0]]
        # n=3
        # mat=[[1,1,1],[1,1,1],[0,0,0]]
        n=3
        mat=[[0,0,0],[0,0,0],[0,0,0]]
        ob=Solution()
        ans=[]
        ans=ob.findMaxRow(mat,n)
        for i in range(2):
            print(ans[i],end=' ')
        print()