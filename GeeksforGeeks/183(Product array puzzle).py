'''
Product array puzzle
Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal to the product
of all the elements of nums except nums[i].
Example 1:
Input:
n = 5
nums[] = {10, 3, 5, 6, 2}
Output:
180 600 360 300 900
Explanation:
For i=0, P[i] = 3*5*6*2 = 180.
For i=1, P[i] = 10*5*6*2 = 600.
For i=2, P[i] = 10*3*6*2 = 360.
For i=3, P[i] = 10*3*5*2 = 300.
For i=4, P[i] = 10*3*5*6 = 900.

Example 2:
Input:
n = 2
nums[] = {12,0}
Output:
0 12
Your Task:
You do not have to read input. Your task is to complete the function productExceptSelf() that takes array nums[]
and n as input parameters and returns a list of n integers denoting the product array P. If the array has only one
element the returned list should should contains one value i.e {1}
Note: Try to solve this problem without using the division operation.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
Constraints:
1 <= n <= 1000
0 <= numsi <= 200
Array may contain duplicates.
'''
class Solution:
    def productExceptSelf(self,arr,n):
        m=[]
        if len(arr)==1:
            m.append(1)
            return m
        left=[]
        right=[]
        prod=1
        prod1=1
        for i in range(len(arr)):
            prod=prod*arr[i]
            left.append(prod)
        for j in range(len(arr)-1,-1,-1):
            prod1=prod1*arr[j]
            right.append(prod1)
        right=right[::-1]
        print(left,right)

        x=[]
        for i in range(len(arr)):
            if i==0:
                x.append(right[i+1])
            elif i==len(arr)-1:
                x.append(left[i-1])
            else:
                p=left[i-1]*right[i+1]
                x.append(p)
        return x
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=5
        arr=[10,3,5,6,2]
        # n=2
        # arr=[12,0]
        # n=1 #Exception - o/p - 1
        # arr=[85]
        ans=Solution().productExceptSelf(arr,n)
        print(*ans)