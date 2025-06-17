'''
Subarray with given sum

Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.

In case of multiple subarrays, return the subarray which comes first
on moving from left to right.

Example 1:
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.

Example 2:
Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements
from 1st position to 5th position
is 15.

Your Task:
You don't need to read input or print anything.
The task is to complete the function subarraySum() which takes arr, N and S
as input parameters and returns a list containing the starting and ending
positions of the first such occurring subarray from the left where sum equals
to S. The two indexes in the list should be according to 1-based indexing.
If no such subarray is found, return an array consisting only one element that is -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= Ai <= 109
'''
'''
The complete solution is

    Maintain start and last index to store and print these values
    Iterate the complete array.
    Add array elements to current sum
    If current sum becomes greater than S, then remove elements starting 
    from start index, till it become less than or equal to S, and increment start.
    if current sum becomes equals to S, then return the starting and last index.
    if the current sum never matches to S, then return -1.

'''
class Solution:
    def subArraySum(self,arr,n,s):
        curr_sum = arr[0]
        start = 0
        i = 1

        while (i <= n):
            while curr_sum > s and start < i - 1:
                curr_sum = curr_sum - arr[start]
                start += 1
            if curr_sum == s:
                x = []
                x.extend([start + 1, i])
                return x
            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1
        x = []
        x.append(-1)
        return x
if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # N,S=map(int,input().split())
        # A=list(map(int,input().split()))
        # N,S=5,12
        # A=[1,2,3,7,5]
        N,S=10,15
        A=[1,2,3,4,5,6,7,8,9,10]
        ob=Solution()
        ans=ob.subArraySum(A,N,S)
        for i in ans:
            print(i,end=' ')
        print()
        T-=1
