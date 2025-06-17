'''
The Nth Fibonnaci
Given a positive integer N, find the last digit of the Nth term from the Fibonacci series.

Note: For N=0 you have to return 0.


Example 1:

Input:
N = 5
Output:
5
Explanation:
5th Fibonacci number is 5

Example 2:

Input:
N = 14
Output:
7
Explanation:
14th Fibonacci number is 377
It's last digit is 7


Your Task:
You don't need to read input or print anything.
Your task is to complete the function fib() which takes an integer N as input parameter
and returns the last digit of Nth Fibonacci number.

Expected Time Complexity: O(N)
Expected Space Complexity: O(1)


Constraints:
0 <= N <= 1000
'''

class Solution:
    def fib(self,N):
        if N==0:
            return 0
        if N==1:
            return 1
        if N==2:
            return 1
        if N==3:
            return 2
        n1=1
        n2=1
        sum1=n1+n2
        n1=n2
        n2=sum1
        for i in range(4,N+1):
            sum1=n1+n2
            n1=n2
            n2=sum1
        print(sum1)
        return str(sum1)[-1]

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # N=14
        N=13
        ob=Solution()
        print(ob.fib(N))