
'''
Triangular Number

Given a number N.Check whether it is a triangular number or not.
Note: A number is termed as a triangular number if we can represent it in the form of a triangular grid of points such
that the points form an equilateral triangle and each row contains as many points as the row number, i.e.,
the first row has one point, the second row has two points, the third row has three points and so on.
The starting triangular numbers are 1, 3 (1+2), 6 (1+2+3), 10 (1+2+3+4).

Example 1:
Input:
N=55
Output:
1
Explanation:
55 is a triangular number.
It can be represented in 10 rows.

Example 2:
Input:
N=56
Output:
0
Explanation:
56 is not a triangular number.

Your Task:
You don't need to read input or print anything. Your task is to complete the function isTriangular() that takes a number N as input parameter and returns 1 if it is a triangular number. Otherwise, it returns 0.

Expected Time complexity:O(LogN)
Expected Auxillary Space:O(1)

Constraints:
1<=N<=106
'''

class Solution:
    def isTriangular(self,N):

        x=int(math.sqrt(2*N))
        if x*(x+1)==2*N:
            return 1
        return 0

import math
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        N=55
        ob=Solution()
        print(ob.isTriangular(N))

