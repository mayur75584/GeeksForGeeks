'''
Largest subarray with 0 sum

Given an array having both positive and negative integers.
The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.

Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n,
where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
-1000 <= A[i] <= 1000, for each valid i

'''
class Solution:
    def maxLen(self,n,arr):
        dict1=dict()
        sum1=0
        max_len=0
        for i in range(n):
            sum1+=arr[i]
            if sum1==0:
                max_len=i+1
            if sum1 not in dict1:
                dict1[sum1]=i
            else:
                max_len=max(max_len,i-dict1[sum1])
        print(dict1)
        return max_len

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=8
        arr=[15,-2,2,-8,1,7,10,23]
        # n=3
        # arr=[1,2,3]
        # n=79
        # arr=[-341 ,778 ,-826 ,-153 ,-574 ,-289 ,-993 ,-622 ,-989 ,-695 ,150 ,-692 ,755 ,-150 ,-586 ,-123 ,960 ,-182 ,-605 ,168 ,-635 ,47 ,-108 ,126 ,158 ,71 ,-584 ,-482 ,565 ,-51 ,369 ,-431 ,431 ,467 ,305 ,572 ,-793 ,276 ,639 ,-706 ,574 ,158 ,894 ,-849 ,979 ,-959 ,432 ,-25 ,712 ,-897 ,-476 ,661 ,791 ,880 ,-686 ,-278 ,364 ,-123 ,429 ,-65 ,230 ,459 ,-770 ,-872 ,330 ,-202 ,-944 ,783 ,-502 ,869 ,-246 ,-154 ,-935 ,572 ,959 ,-475 ,18 ,-198 ,-769]
        ob=Solution()
        print(ob.maxLen(n,arr))