'''
First Repeating Element

Given an array arr[] of size n, find the first repeating element.
The element should occurs more than once and the index of its first occurrence
should be the smallest.

Example 1:

Input:
n = 7
arr[] = {1, 5, 3, 4, 3, 5, 6}
Output: 2
Explanation:
5 is appearing twice and
its first appearence is at index 2
which is less than 3 whose first
occuring index is 3.


Example 2:

Input:
n = 4
arr[] = {1, 2, 3, 4}
Output: -1
Explanation:
All elements appear only once so
answer is -1.


Your Task:
You don't need to read input or print anything. Complete the function firstRepeated()
which takes arr and n as input parameters and return the position of the
first repeating element. If there is no such element, return -1.
The position you return should be according to 1-based indexing.



Expected Time Complexity: O(n)
Expected Auxilliary Space: O(n)



Constraints:
1 <= n <= 106
0 <= Ai<= 106
'''

class Solution:
    def firstRepeated(self,arr,n):
        z = [0] * (max(arr) + 1)
        for i in range(len(arr)):
            x = arr[i]
            if z[x] < 1:
                z[x] = 1
            elif z[x] >= 1:
                z[x] = z[x]+1
        for i in range(len(arr)):
            x = arr[i]
            if z[x] >= 2:
                return arr.index(x)+1
        return -1


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=[int(x) for x in input().split()]
        # n=7
        # arr=[1,5,3,4,3,5,6]
        n=4
        arr=[1,2,3,4]
        # n=12
        # arr=[7,4,0,9,4,8,8,2,4,5,5,1]
        ob=Solution()
        print(ob.firstRepeated(arr,n))

    