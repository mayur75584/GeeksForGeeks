'''
Find Transition Point

Given a sorted array containing only 0s and 1s, find the transition point.


Example 1:

Input:
N = 5
arr[] = {0,0,0,1,1}
Output: 3
Explanation: index 3 is the transition
point where 1 begins.


Example 2:

Input:
N = 4
arr[] = {0,0,0,0}
Output: -1
Explanation: Since, there is no "1",
the answer is -1.


Your Task:
You don't need to read input or print anything. The task is to complete the function transitionPoint() that takes array and N as input parameters and returns the 0 based index of the position where "0" ends and "1" begins. If array does not have any 1s, return -1. If array does not have any 0s, return 0.


Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 500000
0 ≤ arr[i] ≤ 1
'''

def transitionPoint(arr,n):
    for i in range(len(arr)):
        if arr[i]==1:
            return i
    else:
        return -1




if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr=list(map(int,input().strip().split()))
        # n=5
        # arr=[0,0,0,1,1]
        # n=4
        # arr=[0,0,0,0]
        # n=1
        # arr=[1]
        print(transitionPoint(arr,n))