'''
Union of two arrays

Given two arrays a[] and b[] of size n and m respectively.
The task is to find union between these two arrays.

Union of the two arrays can be defined as the set containing distinct
elements from both the arrays. If there are repetitions,
then only one occurrence of element should be printed in the union.

Example 1:
Input:
5 3
1 2 3 4 5
1 2 3
Output:
5
Explanation:
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.

Example 2:
Input:
6 2
85 25 1 32 54 6
85 2
Output:
7
Explanation:
85, 25, 1, 32, 54, 6, and
2 are the elements which comes in the
union set of both arrays. So count is 7.

Your Task:
Complete doUnion funciton that takes a, n, b, m as parameters
and returns the count of union elements of the two arrays.
The printing is done by the driver code.

Constraints:
1 ≤ n, m ≤ 105
0 ≤ a[i], b[i] < 105

Elements are not necessarily distinct.
Expected Time Complexity : O((n+m)log(n+m))
Expected Auxilliary Space : O(n+m)
'''
class Solution:
    def doUnion(self,a,n,b,m):
        dict1={}
        for i in a:
            if i not in dict1:
                dict1[i]=1
        for j in b:
            if j not in dict1:
                dict1[j]=1
        return len(dict1)
        'Getting TLE for below solution'
        # if m<=n:
        #     for i in range(m):
        #         if b[i] not in a:
        #             a.append(b[i])
        #     return len(a)
        # else:
        #     for i in range(n):
        #         if a[i] not in b:
        #             b.append(a[i])
        #     return len(b)


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n,m=map(int,input().split())
        # a=[]
        # for i in range(n):
        #     a.append(int(input()))
        # b=[]
        # for j in range(m):
        #     b.append(int(input()))
        n,m=5,3
        a=[1,2,3,4,5]
        b=[1,2,3]
        # n,m=6,2
        # a=[85,25,1,32,54,6]
        # b=[85,2]
        ob=Solution()
        print(ob.doUnion(a,n,b,m))