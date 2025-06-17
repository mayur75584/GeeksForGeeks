
'''
Make the array beautiful

Given an array of negative and non-negative integers.
You have to make the array beautiful.
An array is beautiful if two adjacent integers, arr[i] and arr[i+1] are either negative or non-negative.
And you can do the following operation any number of times until the array becomes beautiful.

    If two adjacent integers are different i.e. one of them is negative and other is non-negative, remove them.

Return the beautiful array after performing the above operation.

Note:An empty array is also a beautiful array.
There can be many adjacent integers which are different as stated above.
So remove different adjacent integers as described above from left to right.

Example 1:

Input: 4 2 -2 1
Output: 4 1
Explanation: As at indices 1 and 2 , 2 and -2 have
different sign, they are removed. And the  the final
array is: 4 1.

Example 2:

Input: 2 -2 1 -1
Output: []
Explanation: As at indices 0 and 1, 2 and -2 have
different sign, so they are removed. Now the array
is 1 -1.Now 1 and -1 are also removed as they have
different sign. So the final array is empty.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function makeBeautiful() which takes an array as an input parameter and returns an array.

Expected Time Complexity: O(N)
Expected Space Complexity: O(N)


Constraints:
1 <= size of the array <= 105
-105 <= arr[i] <= 105
'''
from typing import List

class Solution:
    def makeBeautiful(self,arr):
        stack=[]
        stack.append(arr[0])
        i=1
        while(i<=len(arr)-1):
            if len(stack)==0:
                stack.append(arr[i])
                i+=1
            else:
                stack.append(arr[i])
                if (stack[len(stack)-1]>=0 and stack[len(stack)-1-1]<0) or (stack[len(stack)-1]<0 and stack[len(stack)-1-1]>=0):
                    stack.pop()
                    stack.pop()

                i+=1

        return stack


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=4
        # arr=[2,-2,1,-1]
        # n=4
        # arr=[4,2,-2,1]
        # n=7
        # arr=[-3,-1,-19,0,6,-13,12]
        n=31
        arr=[70,132,188,-169,-79,-97,-173,168,0,-199,182,-99,20,-45,102,-69,152,-61,44,-67,-147,64,-167,-105,118,-67,76,-137,30,98,150]
        obj=Solution()
        res=obj.makeBeautiful(arr)
        print(*res)