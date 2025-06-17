'''
Max Sum Subarray of size K

Given an array of integers Arr of size N and a number K.
Return the maximum sum of a subarray of size K.

Example 1:

Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700
Explanation:
Arr3  + Arr4 =700,
which is maximum.

Example 2:

Input:
N = 4, K = 4
Arr = [100, 200, 300, 400]
Output:
1000
Explanation:
Arr1 + Arr2 + Arr3
+ Arr4 =1000,
which is maximum.

Your Task:

You don't need to read input or print anything.
Your task is to complete the function maximumSumSubarray() which takes the integer k,
vector Arr with size N,
containing the elements of the array and returns the maximum sum of a subarray of size K.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1<=N<=106
1<=K<=N
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