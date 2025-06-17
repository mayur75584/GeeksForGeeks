'''
Equal Sum

Given an array Arr of length N. Determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero.
Formally, find an i, such that, Arr1 + Arr2 ... Arri-1 = Arri+1 + Arri+2 ... ArrN.

Example 1:

Input:
N = 4
Arr[] = {1, 2, 3, 3}
Output: YES
Explanation: Consider i = 3, for [1, 2]
sum is 3 and for [3] sum is also 3.

Example 2:

Input:
N = 2
Arr[] = {1, 5}
Output: NO
Explanation: No such index present.

Your Task:
Complete the function equilibrium() which takes array arr and size n, as input parameters and returns a string representing the answer(YES or NO). You don't to print answer or take inputs.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 106
'''

class Solution:
    def equilibrium(self,a,n):
        for i in range(len(a)//2,0,-1):
            x=a[:i]
            y=a[i:]
            if sum(a[:i])==sum(a[i+1:]):
                return 'YES'
        return 'NO'


if __name__ == '__main__':
    # tc=int(input())
    tc=1
    while(tc>0):
        # n=int(input())
        # a=list(map(int,input().strip().split()))
        # n=4
        # a=[1,2,3,3]
        n=2
        a=[1,5]
        ob = Solution()
        ans=ob.equilibrium(a,n)
        print(ans)
        tc=tc-1


