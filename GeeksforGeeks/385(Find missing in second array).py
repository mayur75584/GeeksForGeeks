'''
Find missing in second array

Given two integer arrays a of size n and b of size m, the task is to find the numbers which are present in the first array a, but not present in the second array b.

Note: Numbers to be returned should in order as they appear in array a.

Example 1:

Input:
n = 6, m = 5
a[] = {1, 2, 3, 4, 5, 10}
b[] = {2, 3, 1, 0, 5}
Output:
4 10
Explanation:
4 and 10 are present in first array, but not in second array.
Example 2:

Input:
n = 5, m = 5
a[] = {4, 3, 5, 9, 11}
b[] = {4, 9, 3, 11, 10}
Output:
5
Explanation:
Second array does not contain element 5.
Your Task:
You don't need to take any input, as it is already accomplished by the driver code.
You just need to complete the function findMissing() that takes an integer array a, an integer array b, an integer n, and an integer m as input parameters and returns an array that contains the missing elements and the order of the elements should be the same as they are in array a.

Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(m).

Constraints:
1 ≤ n, m ≤ 105
-109 ≤ A[i], B[i] ≤ 109
'''

class Solution:
    def findMissing(self,a,b,n,m):
        dict1={}
        ans=[]
        for i in b:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        print(dict1)
        for j in a:
            if j not in dict1:
                ans.append(j)
        return ans


if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # l=list(map(int,input().split()))
        # n=l[0]
        # m=l[1]
        # a=list(map(int,input().split()))
        # b=list(map(int,input().split()))
        n,m=6,5
        a=[1,2,3,4,5,10]
        b=[2,3,1,0,5]

        ob=Solution()
        ans=ob.findMissing(a,b,n,m)
        for each in ans:
            print(each,end=" ")
        print()