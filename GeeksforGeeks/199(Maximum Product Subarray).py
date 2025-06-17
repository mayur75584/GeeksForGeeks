'''
Maximum Product Subarray

Given an array Arr[] that contains N integers
(may be positive, negative or zero).
Find the product of the maximum product subarray.

Example 1:

Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}
Output: 180
Explanation: Subarray with maximum product
is [6, -3, -10] which gives product as 180.

Example 2:

Input:
N = 6
Arr[] = {2, 3, 4, 5, -1, 0}
Output: 120
Explanation: Subarray with maximum product
is [2, 3, 4, 5] which gives product as 120.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function maxProduct() which takes the array
of integers arr and n as parameters and returns an integer denoting
the answer.
Note: Use 64-bit integer data type to avoid overflow.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 500
-102 ≤ Arri ≤ 102
'''
class Solution:
    def maxProduct(self, arr, n):
        # code here
        n = len(arr)
        if n == 1:
            return arr[0]

        # max positive product ending at the current position

        max_ending_here = 1

        # min positive product ending at the current position
        min_ending_here = 1

        # Initialize maximum so far
        max_so_far = 0
        flag = 0

        # Traverse throughout the array. Following values
        # are maintained after the ith iteration:
        # max_ending_here is always 1 or some positive product
        # ending with arr[i]
        # min_ending_here is always 1 or some negative product
        # ending with arr[i]
        for i in range(0, n):

            # If this element is positive, update max_ending_here.
            # Update min_ending_here only if min_ending_here is
            # negative
            if arr[i] > 0:
                max_ending_here = max_ending_here * arr[i]
                min_ending_here = min(min_ending_here * arr[i], 1)
                flag = 1

            # If this element is 0, then the maximum product cannot
            # end here, make both max_ending_here and min_ending_here 0
            # Assumption: Output is alway greater than or equal to 1.
            elif arr[i] == 0:
                max_ending_here = 1
                min_ending_here = 1

            # If element is negative. This is tricky
            # max_ending_here can either be 1 or positive.
            # min_ending_here can either be 1 or negative.
            # next min_ending_here will always be prev.
            # max_ending_here * arr[i]
            # next max_ending_here will be 1 if prev
            # min_ending_here is 1, otherwise
            # next max_ending_here will be prev min_ending_here * arr[i]
            else:
                temp = max_ending_here
                max_ending_here = max(min_ending_here * arr[i], 1)
                min_ending_here = temp * arr[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here

        if flag == 0 and max_so_far == 0:
            return 0
        return max_so_far
if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=3
        arr=[-2,0,-1]
        ob=Solution()
        ans=ob.maxProduct(arr,n)
        print(ans)

        t-=1
