'''
Number Formation

Given three integers x, y, and z, the task is to
find the sum of all the numbers formed by
having 4 at most x times, having 5 at most y times,
and having 6 at most z times as a digit.

Note: Output the sum modulo 109+7.

Example 1:

Input: X = 1, Y = 1, Z = 1
Output: 3675
Explanation: 4 + 5 + 6 + 45 + 54 + 56
+ 65 + 46 + 64 + 456 + 465
+ 546 + 564 + 645 + 654 = 3675

Example 2:

Input: X = 0, Y = 0, Z = 0
Output: 0
Explanation: No number can be formed


Your Task:
You don't need to read input or print anything.
Complete the function getSum() which takes X, Y and Z as input parameters
and returns the integer value

Expected Time Complexity: O(X*Y*Z)
Expected Auxiliary Space: O(X*Y*Z)

Constraints:
0 ≤ X, Y, Z ≤ 60

'''
'''
Approach: 
 

    As this problem has the property of sub-problems overlapping and optimal sub-structure, hence dynamic programming can be used to solve it.
    The numbers having exact i 4s, j 5s, and k 6s for all i < x, j < y, j < z are required to get the required sum.
    Therefore the DP array exactnum[i][j][k] will store the exact count of numbers having exact i 4s, j 5s, and k 6s.
    If exactnum[i – 1][j][k], exactnum[i][j – 1][k] and exactnum[i][j][k – 1] are already known, then it can be observed that the sum of these is the required answer, except in the case when exactnum[i – 1][j][k], exactnum[i][j – 1][k] or exactnum[i][j][k – 1] doesn’t exist. In that case, just skip it.
    exactsum[i][j][k] stores the sum of the exact number having i 4’s, j 5’s, and k 6’s in the same way as 
     

exactsum[i][j][k] = 10 * (exactsum[i - 1][j][k] 
                        + exactsum[i][j - 1][k] 
                        + exactsum[i][j][k - 1]) 
                  + 4 * exactnum[i - 1][j][k] 
                  + 5 * exactnum[i][j - 1][k] 
                  + 6 * exactnum[i][j][k - 1] 
'''
import numpy as np
class Solution:
    def getSum(self,X,Y,Z):
        mod = (10 ** 9) + 7
        N = 101
        # exactsum=[[[0 for i in range(X+1)] for j in range(Y+1)]for k in range(Z+1)]
        # print(exactsum)
        # num=[[[0 for i in range(X+1)]for j in range(Y+1)]for k in range(Z+1)]
        # print(num)
        exactsum = np.zeros((N, N, N))
        num = np.zeros((N, N, N))

        num[0][0][0] = 1
        # print(num)

        ans = 0
        for i in range(X + 1):
            for j in range(Y + 1):
                for k in range(Z + 1):
                    if (i > 0):
                        exactsum[i][j][k] += (exactsum[i - 1][j][k] * 10 + 4 * num[i - 1][j][k]) % mod
                        num[i][j][k] += num[i - 1][j][k] % mod
                    if (j > 0):
                        exactsum[i][j][k] += (exactsum[i][j - 1][k] * 10 + 5 * num[i][j - 1][k]) % mod
                        num[i][j][k] += num[i][j - 1][k] % mod
                    if (k > 0):
                        exactsum[i][j][k] += (exactsum[i][j][k - 1] * 10 + 6 * num[i][j][k - 1]) % mod
                        num[i][j][k] += num[i][j][k - 1] % mod
                    ans += exactsum[i][j][k] % mod
                    ans = ans % mod
        return int(ans)

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # X,Y,Z=map(int,input().split())
        # X,Y,Z=1,1,1
        X,Y,Z=0,4,1
        ob=Solution()
        ans=ob.getSum(X,Y,Z)
        print(ans)