'Used of Binary Search to find element which occurs only once'

'''
Find the element that appears once

Given a sorted array A[] of N positive integers having all the numbers 
occurring exactly twice, except for one number which will occur only once. 
Find the number occurring only once.

Example 1:
Input:
N = 5
A = {1, 1, 2, 5, 5}
Output: 2
Explanation: 
Since 2 occurs once, while
other numbers occur twice, 
2 is the answer.

Example 2:
Input:
N = 7
A = {2, 2, 5, 5, 20, 30, 30}
Output: 20
Explanation:
Since 20 occurs once, while
other numbers occur twice, 
20 is the answer.

Your Task:
You don't need to read input or print anything. 
Your task is to complete the function search() which takes two 
arguments(array A and integer N) and returns the number occurring only once.

Expected Time Complexity: O(Log(N)).
Expected Auxiliary Space: O(1).

Constraints
0 <   N  <= 10^6
0 <= A[i] <= 10^9
'''
class Solution:
    def search(self,arr,n):
        start=0
        end=len(arr)-1
        mid=0

        if(len(arr)==1):
            return arr[0]
        if(arr[start]!=arr[start+1]):
            return arr[start]
        if(arr[end]!=arr[end-1]):
            return arr[end]

        while(start<=end):
            mid=start+(end-start)//2

            if(arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]):
                return arr[mid]
            elif((arr[mid]==arr[mid+1] and mid%2==0) or (arr[mid]==arr[mid-1] and mid%2!=0)):
                start=mid+1
            else:
                end=mid-1
        return -1

if __name__ == '__main__':
    # t=int(input())
    t=1
    for tc in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=7
        # arr=[2,2,5,5,20,30,30]
        n=5
        arr=[1,1,2,5,5]
        ob=Solution()
        print(ob.search(arr,n))

