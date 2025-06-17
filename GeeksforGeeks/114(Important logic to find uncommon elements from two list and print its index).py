'''
Index Of an Extra Element

Given two sorted arrays of distinct elements. There is only 1 difference between the arrays. First array has one element extra added in between. Find the index of the extra element.

Example 1:

Input:
N = 7
A[] = {2,4,6,8,9,10,12}
B[] = {2,4,6,8,10,12}
Output: 4
Explanation: In the second array, 9 is
missing and it's index in the first array
is 4.

Example 2:

Input:
N = 6
A[] = {3,5,7,9,11,13}
B[] = {3,5,7,11,13}
Output: 3

Your Task:
You don't have to take any input. Just complete the provided function findExtra() that takes array A[], B[] and size of A[] and return the valid index (0 based indexing).

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
2<=N<=104
1<=Ai<=105
'''


class Solution:
    def findExtra(self,a,b,n):
        #Important logic to find uncommon elements from two list/array
        x=set(a)^set(b)
        x1=list(x)
        z=x1[0]
        return a.index(z)



if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # a=list(map(int,input().split()))
        # b=list(map(int,input().split()))
        n=7
        a=[2,4,6,8,9,10,12]
        b=[2,4,6,8,10,12]
        print(Solution().findExtra(a,b,n))
