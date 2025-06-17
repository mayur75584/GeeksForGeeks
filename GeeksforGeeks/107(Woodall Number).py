
'''
Woodall Number

Given a number N. The task is to check if N is woodall number or not. A Woodall Number is of the form:

    Wn = n.2n – 1

The first few Woodall numbers are: 1, 7, 23, 63, 159, 383, 895……

Example 1:

Input: N = 383
Output: 1
Explaination: 6*26 - 1 = 383.

Example 2:

Input: N = 200
Output: 0
Explaination: This is not a Woodall number.

Your task:
You do not need to read input or print anything. Your task is to complete the function isWoodall() which takes N as input parameter and returns 1 if it is a Woodall number, else returns 0.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 106
'''




class Solution:
    def isWoodall(self,N):
        for i in range(1,N+1):
            z=i*(2**i)-1
            if z==N:
                return 1
            elif z>N:
                return 0


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # N=383
        N=200
        ob=Solution()
        print(ob.isWoodall(N))