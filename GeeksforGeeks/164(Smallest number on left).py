
'''
Smallest number on left

Given an array a of integers of length n, find the nearest smaller number for every element such that the smaller
 element is on left side.If no small element present on the left print -1.

Example 1:

Input: n = 3
a = {1, 6, 2}
Output: -1 1 1
Explaination: There is no number at the
left of 1. Smaller number than 6 and 2 is 1.

Example 2:

Input: n = 6
a = {1, 5, 0, 3, 4, 5}
Output: -1 1 -1 0 3 4
Explaination: Upto 3 it is easy to see
the smaller numbers. But for 4 the smaller
numbers are 1, 0 and 3. But among them 3
is closest. Similary for 5 it is 4.

Your Task:
You do not need to read input or print anything.
Your task is to complete the function leftSmaller() which takes n and a as input parameters
and returns the list of smaller numbers.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 100
1 ≤ a[i] ≤ 104

Input:
n=6
arr=[1,6,4,10,2,5]
Output:
-1,1,1,4,1,2

Input:
n=5
arr=[1,3,0,2,5]
Output:
-1,1,-1,0,2
'''
class Solution:
    def leftSmaller(self,n,a):
        stack=[]
        res=[]
        for i in range(len(a)):
            while(len(stack)!=0 and stack[-1]>=a[i]):
                stack.pop(-1)
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(a[i])
        return res
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # a=list(map(int,input().split()))
        # n=3
        # a=[1,6,2]
        n=6
        a=[1,5,0,3,4,5]
        ob=Solution()
        ans=ob.leftSmaller(n,a)
        for i in ans:
            print(i,end=' ')
        print()