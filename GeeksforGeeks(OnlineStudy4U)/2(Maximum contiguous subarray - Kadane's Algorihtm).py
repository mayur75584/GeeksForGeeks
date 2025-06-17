'''
Kadane's Algorithm

Given an array arr of N integers. Find the contiguous sub-array with maximum sum.


Example 1:

Input:
N = 5
arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which
is a contiguous subarray.

Example 2:

Input:
N = 4
arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1
of element (-1)


Your Task:
You don't need to read input or print anything.
The task is to complete the function maxSubarraySum() which takes arr and N as input parameters and
 returns the sum of subarray with maximum sum.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 106
-107 ≤ A[i] ≤ 107
'''
'Note-> Kadanes Algorithm only work on positive numbers'
'''
But in this  Kadanes Algorihtm will not work
we have to modify Kadanes Algorithm so that it can take negive values also
'''

class Solution:
    def maxSubArraySum(self,a ,size):
        cur_max=a[0]
        max=a[0]
        for i in range(1,size):
            cur_max+=a[i]
            if (a[i]>cur_max):
                cur_max=a[i]
            if cur_max>max:
                max=cur_max
        return max

'Alternative approach'


class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        ##Your code here
        n = len(arr)
        c_pos = 0
        c_neg = 0
        for i in arr:
            if i > 0:
                c_pos += 1
            elif i < 0:
                c_neg += 1
        if c_pos == n:
            return sum(arr)
        elif c_neg == n:

            return max(arr)
        else:
            res = arr[0]
            max1 = arr[0]
            for i in range(1, len(arr)):
                max1 = max(max1 + arr[i], arr[i])
                # print("max1",max1,"res",res)
                res = max(max1, res)
            return res


import math

def main():
    # T=int(input())
    T=1
    while(T>0):

        # n=int(input())
        # arr=[int(x) for x in input().strip().split()]

        # n=4
        # arr=[-1,-2,-3,-4]

        n=8
        arr=[-2,-3,4,-1,-2,1,5,-3]
        ob = Solution()
        print(ob.maxSubArraySum(arr,n))

        T-=1

if __name__ == '__main__':
    main()
