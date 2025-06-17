'''
Maximum Volume of a Rectangular Box

John was given a task to make a rectangular box during his innovation competition. He was given with
the A cm of wire and B cm2 of special paper. He had to use all the wire (for the 12 edges) and paper (for the 6 sides)
to make the box. So what will be the maximum volume of that box?

Example 1:
Input:
A = 20, B = 14
Output:
3
Explanation:
The maximum volumed Rectangular
Box we can get is 3cm3.

Example 2:

Input:
A = 20, B = 16
Output:
4
Explanation:
The maximum volumed Rectangular
Box we can get is 4cm3.

Your Task:
You don't need to read input or print anything. Your task is to complete the function getVol()
which takes 2 Integers A, and B as input and returns the answer.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
1 <= A,B <= 106
'''
import math
class Solution:
    def getVol(self,A,B):
        ans = (36 * A * B - math.pow(A, 3) + math.sqrt(math.pow((A * A - 24 * B), 3))) / (12 * 72)
        if (ans < 0):
            ans = 0
        return int(ans)
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        A,B=map(int,input().split())

        ob=Solution()
        print(ob.getVol(A,B))
