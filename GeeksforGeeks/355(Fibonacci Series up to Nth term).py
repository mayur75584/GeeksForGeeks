'''
Fibonacci Series up to Nth term

You are given integer N, and return the Fibonacci Series till the Nth term.

Example:

Input:
5
Output:
0 1 1 2 3 5
Explanation:
0 1 1 2 3 5 is the Fibonacci series up to
the 5th term.(0-based indexing)

Your Task:
You don't need to read input or print anything.
Your task is to complete the function Series() which takes
an Integer N as input and returns a Fibonacci Series up to the Nth term.

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraint:
1<=n<100

'''
class Solution:
    def series(self,n):
        if n==0:
            return [0]
        if n==1:
            return [0,1]
        res=[0,1]
        count1=1
        def fibo(res,n,count1):
            if(count1==n):
                return
            res.append(res[-1]+res[-2])
            return fibo(res,n,count1+1)

        fibo(res,n,count1)
        return res

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        N=5

        ob=Solution()
        result=ob.series(N)
        print(*result)