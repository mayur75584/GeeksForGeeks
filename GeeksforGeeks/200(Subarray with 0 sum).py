'''
Subarray with 0 sum

Given an array of positive and negative numbers.
Find if there is a subarray (of size at-least one) with 0 sum.

Example 1:

Input:
5
4 2 -3 1 6

Output:
Yes

Explanation:
2, -3, 1 is the subarray
with sum 0.

Example 2:

Input:
5
4 2 0 1 6

Output:
Yes

Explanation:
0 is one of the element
in the array so there exist a
subarray with sum 0.

Your Task:
You only need to complete the function subArrayExists()
that takes array and n as parameters and returns true or false
depending upon whether there is a subarray present with 0-sum or not.
 Printing will be taken care by the drivers code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= n <= 104
-105 <= a[i] <= 105
'''
class Solution:
    def subArrayExists(self,arr,n):
        #traverse through the array and store prefix sums
        n_sum=0
        s=set()
        for i in range(n):
            n_sum+=arr[i]

            #If prefix sum is 0 or
            #it is already present
            if n_sum==0 or n_sum in s:
                return True
            s.add(n_sum)
        return False

if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=5
        # arr=[4,2,-3,1,6]
        n=5
        arr=[4,2,0,1,6]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")

        T-=1