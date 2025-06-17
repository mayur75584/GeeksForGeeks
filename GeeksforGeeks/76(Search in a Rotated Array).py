'''
Search in a Rotated Array

Given a sorted and rotated array A of N distinct elements which is rotated at some point,
and given an element key. The task is to find the index of the given element key in the array A.

Example 1:

Input:
N = 9
A[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}
key = 10
Output:
5
Explanation: 10 is found at index 5.

Example 2:

Input:
N = 4
A[] = {3, 5, 1, 2}
key = 6
Output:
-1
Explanation: There is no element that has value 6.

Your Task:
Complete the function search() which takes an array arr[] and start, end index of the array and the K as input parameters,
and returns the answer.

Can you solve it in expected time complexity?

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 108
1 ≤ key ≤ 108


'''

class Solution:
    def search(self,A:list, l:int,h:int,key:int):
        for i in range(len(A)):
            if A[i]==key:
                # print(A.index(A[i]))
                return A.index(A[i])
        else:
            return -1

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # A=[int(x) for x in input().split()]
        # k=int(input())
        n=9
        A=[5,6,7,8,9,10,1,2,3]
        k=10
        ob=Solution()
        # ob.search(A,0,n-1,k)
        print(ob.search(A,0,n-1,k))