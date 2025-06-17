'''
Rightmost different bit

Given two numbers M and N.
The task is to find the position of the rightmost different bit
in the binary representation of numbers.

Example 1:

Input: M = 11, N = 9
Output: 2
Explanation: Binary representation of the given
numbers are: 1011 and 1001,
2nd bit from right is different.

Example 2:

Input: M = 52, N = 4
Output: 5
Explanation: Binary representation of the given
numbers are: 110100 and 0100,
5th-bit from right is different.

User Task:
The task is to complete the function posOfRightMostDiffBit()
which takes two arguments m and n and returns the position
of first different bits in m and n.
If both m and n are the same then return -1 in this case.

Expected Time Complexity: O(max(log m, log n)).
Expected Auxiliary Space: O(1).

Constraints:
0 <= M <= 109
0 <= N <= 109

'''

import math

class Solution:
    def posOfRightMostDiffBit(self,m,n):
        a=bin(m).replace("0b","")
        b=bin(n).replace("0b","")
        print(a)
        print(b)
        x = abs(len(a) - len(b))
        if len(a) > len(b):
            b = x * '0' + b
        else:
            a = x * '0' + a
        if len(a)<=len(b):
            count1=0
            for i in range(len(a)-1,-1,-1):
                count1+=1
                if a[i]!=b[i]:
                    return count1
            else:
                return -1
        else:
            count2=0
            for i in range(len(b)-1,-1,-1):
                count2+=1
                if a[i]!=b[i]:
                    return count2
            else:
                return -1

if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # m,n=map(int,input().split())
        # m,n=11,9
        # m,n=52,4
        m,n=9,9
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))

        T-=1