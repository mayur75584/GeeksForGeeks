'''
Nth Fibonacci Number
Given a positive integer n, find the nth fibonacci number.
Since the answer can be very large, return the answer modulo 1000000007.

Example 1:

Input: n = 2
Output: 1
Explanation: 1 is the 2nd number
of fibonacci series.

Example 2:

Input: n = 5
Output: 5
Explanation: 5 is the 5th number
of fibonacci series.


Your Task:
You dont need to read input or print anything.
Complete the function nthFibonacci() which takes n as input parameter
and returns nth fibonacci number.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1<= n <=1000
'''
class Solution:
    def nthFibonacci(self,n):
        num1 = 0
        num2 = 1
        if n < 0:
            return -1
        if n == 0:
            return num1
        if n == 1:
            return num2
        num3 = 0
        for i in range(3, n + 2):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return num2 % (1000000007)


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        n=5
        # n=2
        # n=656
        ob=Solution()
        print(ob.nthFibonacci(n))





