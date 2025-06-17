'''
Longest consecutive subsequence

Given an array of positive integers.
Find the length of the longest sub-sequence such that elements in the
subsequence are consecutive integers, the consecutive numbers can be in any order.

Example 1:
Input:
N = 7
a[] = {2,6,1,9,4,5,3}
Output:
6
Explanation:
The consecutive numbers here
are 1, 2, 3, 4, 5, 6. These 6
numbers form the longest consecutive
subsquence.

Example 2:
Input:
N = 7
a[] = {1,9,3,10,4,20,2}
Output:
4
Explanation:
1, 2, 3, 4 is the longest
consecutive subsequence.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function findLongestConseqSubseq()
which takes the array arr[] and the size of the array as inputs and
returns the length of the longest subsequence of consecutive integers.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
0 <= a[i] <= 105
'''

class Solution:
    def findLongestConseqSubseq(self,arr,n):
        s=set()
        ans=0
        # check each possible sequence from the start
        # then update optimal length
        for i in arr:
            s.add(i)

        for i in range(n):
            # if current element is the starting
            # element of a sequence
            if(arr[i]-1 not in s):
                # Then check for next elements in the
                # sequence
                j=arr[i]
                while(j in s):
                    j+=1
                # update  optimal length if this length
                # is more
                ans=max(ans,j-arr[i])
        return ans

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # a=list(map(int,input().split()))
        n=7
        a=[1,9,3,10,4,20,2]
        print(Solution().findLongestConseqSubseq(a,n))