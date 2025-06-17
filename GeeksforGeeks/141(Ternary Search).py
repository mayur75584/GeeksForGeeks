'''
Searching an element in a sorted array (Ternary Search)

Given a sorted array arr[] of size N and an integer K. The task is to check if K is present in the array or not using ternary search.

Ternary Search- It is a divide and conquer algorithm that can be used to find an element in an array. In this algorithm, we divide the given array into three parts and determine which has the key (searched element).


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
You don't need to read input or print anything. Complete the function ternarySearch() which takes the sorted array arr[], its size N and the element K as input parameters and returns 1 if K is present in the array, else it returns -1.

Expected Time Complexity: O(Log3N)
Expected Auxiliary Space: O(1)

Constraints:
1 < N < 106
1 < K < 106
1 < arr[i] < 106
'''
class Solution:
    def ternarySearch(self,arr,N,K):
        #Algorithm for ternary search
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid1 = l + (r - l) // 3
            mid2 = r - (r - l) // 3

            if K == arr[mid1]:
                return 1 #if element found return 1
            if K == arr[mid2]:
                return 1 #if element found return 1
            if K < arr[mid1]:
                r = mid1 - 1
            elif K > arr[mid2]:
                l = mid2 + 1
            else:
                l = mid1 + 1
                r = mid2 - 1
        return -1 #if element not found return -1



if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N,K=map(int,input().split())
        arr=[]
        for i in range(N):
            arr.append(int(input()))
        ob=Solution()
        print(ob.ternarySearch(arr,N,K))