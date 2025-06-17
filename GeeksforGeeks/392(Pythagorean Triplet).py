'''
Pythagorean Triplet

Given an array arr of n integers, write a function that returns true if there is a triplet (a, b, c) from the array (where a, b, and c are on different indexes) that satisfies a2 + b2 = c2, otherwise return false.

Example 1:

Input:
N = 5
Arr[] = {3, 2, 4, 6, 5}
Output: Yes
Explanation: a=3, b=4, and c=5 forms a
pythagorean triplet.
Example 2:

Input:
N = 3
Arr[] = {3, 8, 5}
Output: No
Explanation: No such triplet possible.
Your Task:
You don't have to take any input or print any thing. You have to complete the function checkTriplet() which takes an array arr, a single integer n, as input parameters and returns boolean denoting answer to the problem.
Note: The driver will print "Yes" or "No" instead of corresponding to the boolean value returned.

Expected Time Complexity: O(n+max(Arr[i])2)
Expected Auxiliary Space: O(max(Arr[i]))

Constraints:
1 <= n <= 105
1 <= arr[i] <= 1000
'''

from itertools import combinations
class Solution:
    def checkTriplet(self,arr,n):
        dict1={}
        for i in arr:
            dict1[i]=(i*i)
        lst_values=list(dict1.values())
        # print(lst_values)
        comb=combinations(lst_values,2)
        for i in list(comb):
            if sum(i) in lst_values:
                return True
        return False


if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=5
        # arr=[3,2,4,6,5]
        n=3
        arr=[3,8,5]
        ob=Solution()
        ans=ob.checkTriplet(arr,n)
        if ans:
            print("Yes")
        else:
            print("No")
        t-=1