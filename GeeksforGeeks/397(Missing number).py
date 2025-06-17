'''
Missing number
Difficulty: EasyAccuracy: 45.15%Submissions: 93K+Points: 2
Ritu has all numbers from 2 to n in an array, arr of length n-1 except one number.
You have to return the missing number, Ritu doesn't have from 1 to n.

Note: Don't use Sorting

Examples:

Input: n = 4, arr = [1,  4,  3]
Output: 2
Explanation: Ritu doesn't have the number 2
Input: n = 5, arr = [2,  5,  3,  1]
Output: 4
Explanation: Ritu doesn't have number 4 in her collection
Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
2 ≤ n ≤ 104
1 ≤ arr[i] ≤ n
arr.szie = n-1

'''

from typing import List

class Solution:
    def missingNumber(self,n,arr):
        if n==1 and arr[0]!=1:
            return 1

        sum1=(n*(n+1))//2
        # print(sum1)
        sum2=sum(arr)
        # print(sum2)
        return abs(sum1-sum2)

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=4
        arr=[1,4,3]
        # n=5
        # arr=[2,5,3,1]
        obj=Solution()
        res=obj.missingNumber(n,arr)

        print(res)