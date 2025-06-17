'''
Count triplets with sum smaller than X

Given an array arr[] of distinct integers of size N and a value sum,
the task is to find the count of triplets (i, j, k),
having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.

Example 1:
Input: N = 4, sum = 2
arr[] = {-2, 0, 1, 3}
Output:  2
Explanation: Below are triplets with
sum less than 2 (-2, 0, 1) and (-2, 0, 3).

Example 2:
Input: N = 5, sum = 12
arr[] = {5, 1, 3, 4, 7}
Output: 4
Explanation: Below are triplets with
sum less than 12 (1, 3, 4), (1, 3, 5),
(1, 3, 7) and (1, 4, 5).

Your Task:
This is a function problem. You don't need to take any input,
as it is already accomplished by the driver code.
You just need to complete the function countTriplets() that take array arr[],
integer N  and integer sum as parameters and returns the count of triplets.

Expected Time Complexity: O(N2).
Expected Auxiliary Space: O(1).

Constraints:
3 ≤ N ≤ 103
-103 ≤ arr[i] ≤ 103
'''
'''
1) Sort the input array in increasing order.
2) Initialize result as 0.
3) Run a loop from i = 0 to n-2.  An iteration of this loop finds all
   triplets with arr[i] as first element.
     a) Initialize other two elements as corner elements of subarray
        arr[i+1..n-1], i.e., j = i+1 and k = n-1
     b) Move j and k toward each other until they meet, i.e., while (j<k),
            (i) If arr[i] + arr[j] + arr[k] >= sum
                then k--
            // Else for current i and j, there can (k-j) possible third elements
            // that satisfy the constraint.
            (ii) Else Do ans += (k - j) followed by j++ 
'''

class Solution:
    def countTriplets(self,a,n,k):
        a.sort()
        ans=0
        for i in range(n-2):
            l=i+1
            r=n-1
            while(l<r):
                if(a[i]+a[l]+a[r]>=k):
                    r=r-1
                else:
                    ans+=(r-l)
                    l+=1
        return ans

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n,k=map(int,input().split())
        # a=list(map(int,input().split()))
        # n,k=4,2
        # a=[-2,0,1,3]
        n,k=5,12
        a=[5,1,3,4,7]
        ob=Solution()
        ans=ob.countTriplets(a,n,k)
        print(ans)
