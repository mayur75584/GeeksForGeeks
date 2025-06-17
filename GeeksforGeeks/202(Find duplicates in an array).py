'''
Find duplicates in an array

Given an array a[] of size N which contains elements from 0 to N-1,
you need to find all the elements occurring more than once in the given array.

Example 1:
Input:
N = 4
a[] = {0,3,1,2}
Output: -1
Explanation: N=4 and all elements from 0
to (N-1 = 3) are present in the given
array. Therefore output is -1.

Example 2:
Input:
N = 5
a[] = {2,3,1,2,3}
Output: 2 3
Explanation: 2 and 3 occur more than once
in the given array.

Your Task:
Complete the function duplicates() which takes array a[] and n as input
as parameters and returns a list of elements that occur more than once in the
given array in sorted manner. If no such element is found, return list containing [-1].

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
Note : The extra space is only for the array to be returned.
Try and perform all operation withing the provided array.
Constraints:
1 <= N <= 105
0 <= A[i] <= N-1, for each valid i
'''
class Solution:
    def duplicates(self,arr,n):
        x=[0]*(max(arr)+1)
        for i in arr:
            if x[i]==0:
                x[i]+=1
            elif x[i]>=1:
                x[i]+=1
        res=[]
        for i in range(len(x)):
            if x[i]>=2:
                res.append(i)
        if len(res)==0:
            res.append(-1)
            return res
        return res

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=5
        # arr=[2,3,1,2,3]
        n=11
        arr=[10,10,7,7,7,4,0,5,10,5,10]

        res=Solution().duplicates(arr,n)
        for i in res:
            print(i,end=' ')
        print()