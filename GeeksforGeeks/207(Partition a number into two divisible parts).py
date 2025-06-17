'''
Partition a number into two divisible parts

Given a number (as string) and two integers a and b,
divide the string in two non-empty parts such that
the first part is divisible by a and the second part is divisible by b.
In case multiple answers exist, return the string such that
the first non-empty part has minimum length.

Example 1:
Input:
1200 4 3
Output:
12 00
Explanation:
12 is divisible by 4, and
00 is divisible by 3.

Example 2:
Input:
125 12 5
Output:
12 5
Explanation:
12 is divisible by 12, and
5 is divisible by 5.

Your Task:

You don't need to read input or print anything.
Your task is to complete the function stringPartition()
which takes the string S and returns a string which will be in the form
of first sub-string + " " (Single Space) + second sub-string.
If not found return -1 as a string.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1<=N<=106
1<=a,b<=N
'''
class Solution:
    def stringPartition(self,s,a,b):
        i = 1
        while (i < len(s)):
            a1, b1 = s[:i], s[i:]
            a2, b2 = int(a1), int(b1)
            if a2 % a == 0 and b2 % b == 0:
                return a1 + ' ' + b1
            else:
                i += 1
        return -1

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        S,a,b=map(str,input().split())
        a=int(a)
        b=int(b)

        ob=Solution()
        print(ob.stringPartition(S,a,b))