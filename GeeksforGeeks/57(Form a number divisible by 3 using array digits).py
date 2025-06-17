'''
Form a number divisible by 3 using array digits

Given an array arr of integers of length N, the task is to find whether it’s possible to construct an integer using all the digits of these numbers such that it would be divisible by 3. If it is possible then print “1” and if not print “0”.

Example 1:

Input: N = 3
arr = {40, 50, 90}
Output: 1
Explaination: One such number is 405900.

Example 2:

Input: N = 2
arr = {1, 4}
Output: 0
Explaination: The numbers we can form
are 14 and 41. But neither of them are
divisible by 3.

Your Task:
You do not need to read input or print anything. Your task is to complete the function isPossible() which takes N and arr as input parameters and returns 1 if we can form a number by the digits of the given number, otherwise returns 0.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N, arr[i] ≤ 105
'''
from itertools import permutations
class Solution:
    def isPossible(self,N,arr):

        remainder=0
        for i in range(0,N):
            remainder = (remainder+arr[i])%3
        if remainder==0:
            return 1
        else:
            return 0
        # lst=[]
        # lst1=[]
        # # for i in arr:
        # #     for j in str(i):
        # #         lst.append(int(str(j)))
        # # lst1=list((permutations(lst)))
        # lst1=list(permutations(arr))
        # for i in lst1:
        #     sum1=0
        #     z=list(i)
        #     sum1+=sum(z)
        #     if sum1%3==0:
        #         print(z)
        #         print(sum1)
        #         return 1
        # else:
        #     return 0




if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # arr=input().split()
        # for i in range(N):
        #     arr[i]=int(arr[i])
        # N=3
        # arr=[40,50,90]
        N=2
        arr=[1,4]
        ob=Solution()
        # ob.isPossible(N,arr)
        print(ob.isPossible(N,arr))