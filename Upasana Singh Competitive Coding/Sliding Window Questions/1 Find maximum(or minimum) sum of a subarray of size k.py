'''
Find maximum (or minimum) sum of a subarray of size k

Given an array of integers and a number k, find the maximum sum of
a subarray of size k
Input: arr[]=[100,200,300,400]
k=2
Output:700

Input: arr[]=[1,4,2,10,23,3,1,0,20]
k=4
Output:39
We get maximum sum by adding subarray [4,2,10,23] of size 4.

Input: arr[]=[2,3]
k=3
Output: Invalid
There is no subarray of size 3 as size of which array is 2.
'''

class Solution:
    def maximumSumSubarray(self,K,Arr,N):
        curr_sum=0
        if N<K:
            return -1
        for i in range(K):
            curr_sum+=Arr[i]
        max_sum=curr_sum
        for i in range(K,N):
            curr_sum=(curr_sum-Arr[i-K])+Arr[i]
            if max_sum<curr_sum:
                max_sum=curr_sum
        return max_sum

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N,K=map(int,input().split())
        # Arr=list(map(int,input().split()))
        # N,K=4,2
        # Arr=[100,200,300,400]
        N,K=4,4
        Arr=[100,200,300,400]
        ob=Solution()
        print(ob.maximumSumSubarray(K,Arr,N))