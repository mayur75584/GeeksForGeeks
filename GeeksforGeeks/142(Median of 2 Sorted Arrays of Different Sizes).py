'''
Median of 2 Sorted Arrays of Different Sizes

Given two sorted arrays array1 and array2 of size m and n respectively. Find the median of the two sorted arrays.

Example 1:

Input:
m = 3, n = 4
array1[] = {1,5,9}
array2[] = {2,3,6,7}
Output: 5
Explanation: The middle element for
{1,2,3,5,6,7,9} is 5

Example 2:

Input:
m = 2, n = 4
array1[] = {4,6}
array2[] = {1,2,3,5}
Output: 3.5

Your Task:
The task is to complete the function MedianOfArrays() that takes array1 and array2 as input and returns their median.

Can you solve the problem in expected time complexity?

Expected Time Complexity: O(min(log n, log m)).
Expected Auxiliary Space: O((n+m)/2).

Constraints:
0 ≤ m,n ≤ 104
1 ≤ array1[i], array2[i] ≤ 105
'''

import numpy as np
class Solution:
    def MedianOfArrays(self,array1,array2):
        z=sorted(array1+array2)
        x=np.median(z)
        x1,x2=str(x).split('.')
        if int(x2)==0:
            return int(x1)
        else:
            return x


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # m=int(input())
        # arr1=list(map(int,input().split()))
        # n=int(input())
        # arr2=list(map(int,input().split()))

        m=3
        arr1=[1,5,9]
        n=4
        arr2=[2,3,6,7]
        # m=2
        # arr1=[4,6]
        # n=4
        # arr2=[1,2,3,5]
        ob=Solution()
        print(ob.MedianOfArrays(arr1,arr2))