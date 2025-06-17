'''
Longest Increasing Subsequence

Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

Example 1:

Input:
N = 16
A[]={0,8,4,12,2,10,6,14,1,9,5
     13,3,11,7,15}
Output: 6
Explanation:Longest increasing subsequence
0 2 6 9 13 15, which has length 6

Example 2:

Input:
N = 6
A[] = {5,8,3,7,9,1}
Output: 3
Explanation:Longest increasing subsequence
5 7 9, with length 3

Your Task:
Complete the function longestSubsequence() which takes the input array and its size as input parameters
and returns the length of the longest increasing subsequence.

Expected Time Complexity : O( N*log(N) )
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
0 ≤ A[i] ≤ 106
'''
'''
The Longest Increasing Subsequence (LIS) problem is to find the length 
of the longest subsequence of a given sequence such that all elements 
of the subsequence are sorted in increasing order. 
For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 
and LIS is {10, 22, 33, 50, 60, 80}. 
'''
# Binary search (note
# boundaries in the caller)
# A[] is ceilIndex
# in the caller
def CeilIndex(a,l,r,key):
    while(r-l>1):
        m=l+(r-l)//2
        if(a[m]>=key):
            r=m
        else:
            l=m
    return r
class Solution:
    def longestSubsequence(self,a,n):
        # Add boundary case,
        # when array size is one
        tailTable=[0 for i in range(n+1)]
        leng=0 # always points empty slot
        tailTable[0]=a[0]
        leng=1
        for i in range(1,n):
            if(a[i]<tailTable[0]):
                # new smallest value
                tailTable[0]=a[i]
            elif(a[i]>tailTable[leng-1]):
                # A[i] wants to extend
                # largest subsequence
                tailTable[leng]=a[i]
                leng+=1
            else:
                # A[i] wants to be current
                # end candidate of an existing
                # subsequence. It will replace
                # ceil value in tailTable
                tailTable[CeilIndex(tailTable,-1,leng-1,a[i])]=a[i]
        return leng


if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # a=[int(x) for x in input().split()]
        # n=16
        # a=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
        n=6
        a=[5,8,3,7,9,1]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
