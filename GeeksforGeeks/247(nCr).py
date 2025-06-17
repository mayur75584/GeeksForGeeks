'''
nCr

Given two integers n and r, find nCr. Since the answer may be very large,
calculate the answer modulo 109+7.

Example 1:

Input: n = 3, r = 2
Output: 3
Explaination: 3C2 = 3.


Example 2:

Input: n = 2, r = 4
Output: 0
Explaination: r is greater than n.


Your Task:
You do not need to take input or print anything.
Your task is to complete the function nCr() which takes n and r as
input parameters and returns nCr modulo 109+7..


Expected Time Complexity: O(n*r)
Expected Auxiliary Space: O(r)


Constraints:
1 ≤ n ≤ 1000
1 ≤ r ≤ 800
'''

import math

class Solution:
    def nCr(self,n,r):
        if(r>n):
            return 0
        n_fac = math.factorial(n)
        r_fac = math.factorial(r)
        nr_fac = math.factorial(n - r)
        a1 = r_fac * nr_fac
        a2 = n_fac // a1
        return a2 % ((10 ** 9) + 7)


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n,r=[int(x) for x in input().split()]
        # n,r=3,2
        n,r=2,4
        ob=Solution()
        print(ob.nCr(n,r))