'''
Longest subarray with sum divisible by K

Given an array containing N integers and a positive integer K,
find the length of the longest sub array with sum of the elements divisible by the given value K.

Example 1:
Input:
A[] = {2, 7, 6, 1, 4, 5}
K = 3
Output: 4
Explanation:The subarray is {7, 6, 1, 4}
with sum 18, which is divisible by 3.

Example 2:
Input:
A[] = {-2, 2, -5, 12, -11, -1, 7}
K = 3
Output: 5
Explanation:
The subarray is {2,-5,12,-11,-1} with
sum -3, which is divisible by 3.

Your Task:
The input is already taken care of by the driver code.
You only need to complete the function longSubarrWthSumDivByK()
that takes an array (arr), sizeOfArray (n), positive integer K,
and return the length of the longest subarray which has sum divisible by K.
The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1<=N,K<=106
-105<=A[i]<=105
'''
class Solution:
    def longSubarrWithSumDivByK(self,arr,n,K):
        res=0
        sum,rem=0,0
        dict1={0:-1}
        for i in range(len(arr)):
            sum+=arr[i]
            rem=(sum%K)

            if(rem<0):
                rem+=K
            if(rem in dict1):
                index=dict1[rem]
                leng=i-index

                if(leng>res):
                    res=leng
            else:
                dict1[rem]=i
        return res

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n,K=map(int,input().split())
        # arr=list(map(int,input().split()))
        # n,K=6,3
        # arr=[2,7,6,1,4,5]
        n,K=7,3
        arr=[-2,2,-5,12,-11,-1,7]
        ob=Solution()
        res=ob.longSubarrWithSumDivByK(arr,n,K)
        print(res)
