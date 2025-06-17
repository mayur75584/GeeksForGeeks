'''
Maximum of all subarrays of size k

Given an array arr[] of size N and an integer K.
Find the maximum for each and every contiguous subarray of size K.

Example 1:
Input:
N = 9, K = 3
arr[] = 1 2 3 1 4 5 2 3 6
Output:
3 3 4 5 5 5 6
Explanation:
1st contiguous subarray = {1 2 3} Max = 3
2nd contiguous subarray = {2 3 1} Max = 3
3rd contiguous subarray = {3 1 4} Max = 4
4th contiguous subarray = {1 4 5} Max = 5
5th contiguous subarray = {4 5 2} Max = 5
6th contiguous subarray = {5 2 3} Max = 5
7th contiguous subarray = {2 3 6} Max = 6

Example 2:

Input:
N = 10, K = 4
arr[] = 8 5 10 7 9 4 15 12 90 13
Output:
10 10 10 15 15 90 90
Explanation:
1st contiguous subarray = {8 5 10 7}, Max = 10
2nd contiguous subarray = {5 10 7 9}, Max = 10
3rd contiguous subarray = {10 7 9 4}, Max = 10
4th contiguous subarray = {7 9 4 15}, Max = 15
5th contiguous subarray = {9 4 15 12},
Max = 15
6th contiguous subarray = {4 15 12 90},
Max = 90
7th contiguous subarray = {15 12 90 13},
Max = 90

Your Task:
You dont need to read input or print anything.
Complete the function max_of_subarrays() which takes the array,
N and K as input parameters and returns a list of integers denoting
the maximum of every contiguous subarray of size K.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(k)

Constraints:
1 ≤ N ≤ 107
1 ≤ K ≤ N
0 ≤ arr[i] ≤ 107
'''
'''
Algorithm:  

1-Create a deque to store k elements.
2-Run a loop and insert first k elements in the deque. Before inserting the element, 
check if the element at the back of the queue is smaller than the current element, 
if it is so remove the element from the back of the deque, 
until all elements left in the deque are greater than the current element. 
Then insert the current element, at the back of the deque.
3-Now, run a loop from k to end of the array.
4-Print the front element of the deque.
5-Remove the element from the front of the queue if they are out of the current window.
6-Insert the next element in the deque. Before inserting the element, 
check if the element at the back of the queue is smaller than the current element, 
if it is so remove the element from the back of the deque, 
until all elements left in the deque are greater than the current element. 
Then insert the current element, at the back of the deque.
7-Print the maximum element of the last window.
'''
from collections import deque
class Solution:
    def max_of_subarrays(self,arr,n,k):
        res=[]
        """ Create a Double Ended Queue, q that 
            will store indexes of array elements. 
            The queue will store indexes of useful 
            elements in every window and it will
            maintain decreasing order of values from
            front to rear in Q, i.e., arr[Q.front[]]
            to arr[Q.rear()] are sorted in decreasing
            order"""
        q=deque()
        for i in range(k):
            # For every element, the previous
            # smaller elements are useless
            # so remove them from Q

            while(len(q)!=0 and arr[i]>=arr[q[-1]]):
                q.pop()
            # Add new element at rear of queue
            q.append(i)
        for i in range(k,n):
            res.append(arr[q[0]])
            # Remove the elements which are
            # out of this window
            while(len(q)!=0 and q[0]<=i-k):
                # remove from front of deque
                q.popleft()
            # Remove all elements smaller than
            # the currently being added element
            # (Remove useless elements)
            while(len(q)!=0 and arr[i]>=arr[q[-1]]):
                q.pop()
            q.append(i)
        #Append maximum element of last window
        res.append(arr[q[0]])
        return res
        'Below is the wrong solution'
        # if n<k:
        #     return -1
        # queue=[]
        # res=[]
        # max1=0
        # for i in range(k):
        #     queue.append(arr[i])
        #     if max1<arr[i]:
        #         max1=arr[i]
        # res.append(max1)
        # for i in range(k,n):
        #     queue.pop(0)
        #     queue.append(arr[i])
        #     if max1<arr[i]:
        #         max1=arr[i]
        #     res.append(max1)
        # return res

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n,k=map(int,input().split())
        # arr=list(map(int,input().split()))
        # n,k=9,3
        # arr=[1,2,3,1,4,5,2,3,6]
        n,k=10,4
        arr=[8,5,10,7,9,4,15,12,90,13]
        ob=Solution()
        res=ob.max_of_subarrays(arr,n,k)
        for i in range(len(res)):
            print(res[i],end=' ')
        print()