'''
Last non-zero digit in factorial

Given a number n, find the last non-zero digit in n!.


Examples:

Input  : n = 5
Output : 2
5! = 5 * 4 * 3 * 2 * 1 = 120
Last non-zero digit in 120 is 2.

Input  : n = 33
Output : 8

Your Task:
You don't need to read input or print anything.
Your task is to complete the function lastNon0Digit()
which takes the integer N as input parameters
and returns the last non-zero digit in n!.

Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(1)



Constraints:
1 ≤ N ≤ 100

'''
class Solution:
    def lastNon0Digit(self,N):
        fact1=1
        for i in range(1,N+1):
            fact1=fact1*i
        print(fact1)

        def func1(fact,dig):
            if dig!=0:
                return dig
            else:
                return func1(fact//10,fact%10)
        fact=func1(fact1,fact1%10)
        return fact
if __name__ == '__main__':
    ob=Solution()
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # N=5
        # N=33
        N=57
        ans=ob.lastNon0Digit(N)
        print(ans)