'''
Heap Sort

Given an array of size N. The task is to sort the array elements by completing functions
heapify() and buildHeap() which are used to implement Heap Sort.

Example 1:
Input:
N = 5
arr[] = {4,1,3,9,7}
Output:
1 3 4 7 9
Explanation:
After sorting elements
using heap sort, elements will be
in order as 1,3,4,7,9.

Example 2:
Input:
N = 10
arr[] = {10,9,8,7,6,5,4,3,2,1}
Output:
1 2 3 4 5 6 7 8 9 10
Explanation:
After sorting elements
using heap sort, elements will be
in order as 1, 2,3,4,5,6,7,8,9,10.

Your Task :
You don't have to read input or print anything.
Your task is to complete the functions heapify(),
buildheap() and heapSort() where heapSort() and buildheap() takes the array
and it's size as input and heapify() takes the array,
it's size and an index i as input. Complete and use these functions
to sort the array using heap sort algorithm.
Note: You don't have to return the sorted list.
You need to sort the array "arr" in place.

Expected Time Complexity: O(N * Log(N)).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 106
1 ≤ arr[i] ≤ 106
'''

class Solution:
    def heapify(self,arr,n,i):
        largest=i #Initialize largest as root
        l=2*i+1 #left=2*i+1
        r=2*i+2 #right=2*i+2

        #See if left child of root exists and is
        #greater than root
        if l<n and arr[largest]<arr[l]:
            largest=l
        #See if right child of root exists and is
        #greater than root
        if r<n and arr[largest]<arr[r]:
            largest=r
        #Change root, if needed
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i] #swap

            #Heapify the root
            self.heapify(arr,n,largest)
    def buildHeap(self,arr,n):
        #Build MaxHeap
        for i in range(n//2-1,-1,-1):
            self.heapify(arr,n,i)
    def HeapSort(self,arr,n):
        self.buildHeap(arr,n)

        #One by one extract elemnts
        for i in range(n-1,0,-1):
            arr[i],arr[0]=arr[0],arr[i] #swap
            self.heapify(arr,i,0)

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=5
        # arr=[4,1,3,9,7]
        n=10
        arr=[10,9,8,7,6,5,4,3,2,1]
        Solution().HeapSort(arr,n)
        print(*arr)