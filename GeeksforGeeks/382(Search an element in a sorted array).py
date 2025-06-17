'''
Searching an element in a sorted array

Given an array arr[] sorted in ascending order of size N and an integer K.
Check if K is present in the array or not.


Example 1:

Input:
N = 5, K = 6
arr[] = {1,2,3,4,6}
Output: 1
Exlpanation: Since, 6 is present in
the array at index 4 (0-based indexing),
output is 1.



Example 2:

Input:
N = 5, K = 2
arr[] = {1,3,4,5,6}
Output: -1
Exlpanation: Since, 2 is not present
in the array, output is -1.



Your Task:
You don't need to read input or print anything.
Complete the function searchInSorted() which takes the sorted array arr[], its size N and the element K as input parameters and returns 1 if K is present in the array, else it returns -1.


Expected Time Complexity: O(Log N)
Expected Auxiliary Space: O(1)



Constraints:
1 <= N <= 106
1 <= K <= 106
1 <= arr[i] <= 106


'''

import math

class Solution:
    def searchInSorted(self, arr, N, K):
        # Your code here
        left, right = 0, N - 1


        while (left <= right):
            mid = (left + right) // 2
            if arr[mid] == K:
                return 1

            if (arr[left] <= arr[mid]):
                if (arr[left] <= K < arr[mid]):
                    right = right - 1
                else:
                    left = left + 1
            else:
                if (arr[right] <=K < arr[mid]):
                    left = left + 1
                else:
                    right = right - 1
        return -1



if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # NK = input().strip().split()
        # N = int(NK[0])
        # K = int(NK[1])
        # A = [int(x) for x in input().strip().split()]
        # N,K = 5,6
        # A=[1,2,3,4,6]
        N,K = 5,2
        A=[1,3,4,5,6]
        ob=Solution()
        print(ob.searchInSorted(A,N,K))