'''
Quick Sort
Quick Sort is a Divide and Conquer algorithm.
It picks an element as pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position low and its ending position high.

Implement the partition() and quickSort() functions to sort the array.


Example 1:

Input:
N = 5
arr[] = { 4, 1, 3, 9, 7}
Output:
1 3 4 7 9

Example 2:

Input:
N = 9
arr[] = { 2, 1, 6, 10, 4, 1, 3, 9, 7}
Output:
1 1 2 3 4 6 7 9 10


Your Task:
You don't need to read input or print anything. Your task is to complete the
functions partition()  and quickSort() which takes the array arr[], low and high
as input parameters and partitions the array. Consider the last element as the
pivot such that all the elements less than(or equal to) the pivot lie before it
and the elements greater than it lie after the pivot.


Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 103
1 <= arr[i] <= 104
'''

'''
The key process in quickSort is partition(). 
Target of partitions is, given an array and an element x of array as pivot, 
put x at its correct position in sorted array and put all smaller elements 
(smaller than x) before x, and put all greater elements (greater than x) after x. 
All this should be done in linear time. 
Pseudo Code for recursive QuickSort function : 
'''
class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        # code here
        if len(arr) == 1:
            return arr
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        # code here
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

        # The main function that implements QuickSort
        # arr[] --> Array to be sorted,
        # low  --> Starting index,
        # high  --> Ending index



if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=5
        arr=[4,1,3,9,7]
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=' ')
        print()