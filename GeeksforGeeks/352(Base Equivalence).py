'''
Base Equivalence

Given a number (n) and no. of digits (m) to represent the number,
we have to check if we can represent n using exactly m digits in any base from 2 to 32.

Example 1:

Input: n = 8, m = 2
Output: Yes
Explanation: Possible in base 3 as 8 in base 3 is 22.


Example 2:

Input: n = 8, m = 3
Output: No
Explanation: Not possible in any base.


Your Task:
You dont need to read input or print anything.
Complete the function baseEquiv() which takes n and m as input parameter
and returns "Yes" if its possible to represent the number else "No" without quotes..

Expected Time Complexity: O(logN).
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <=109
1 <= m <=32

'''
'''
log10 is used to find number of digits
'''
import math
class Solution:
    def baseEquiv(self,n,m):

        for i in range(2,32+1):
            a=math.log10(n)
            b=math.log10(i)
            num=int(a//b)
            num+=1

            if(num==m):
                return "Yes"
        return "No"


if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # n,m=map(int,input().split())
        n,m=8,2

        ob=Solution()
        print(ob.baseEquiv(n,m))