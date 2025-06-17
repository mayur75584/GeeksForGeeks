'''
Help Ishaan

Ishaan has been given a task by his teacher.
He needs to find the Nth term of a series.
His teacher gives him some examples to help him out (Refer examples below).
He is a bit weak in pattern searching so to help him his teacher told him
that the Nth term is related to prime numbers.
The Nth term is the difference of N and the closest prime number to N.
Help him find the Nth term for a given N.


Example 1:

Input: N = 10
Output: 1
Explanation: Closest prime to 10 is 11.

Example 2:

Input: N = 7
Output: 0
Explanation: Closest prime to 7 is 7.



Your Task:
You don't need to read or print anything.
Your task is to complete the function NthTerm() which takes N as
input paramater and returns Nth term.


Expected Time Complexity: O(N* √ N)
Expected Space Complexity: O(1)

Constraints:
1 <= N <= 100000

'''
import math
class Solution:
    'Getting TLE'
    # def Prime(self,n):
    #     isprime=True
    #     if n<2:
    #         isprime=False
    #     else:
    #         for i in range(2,n):
    #             if(n%i==0):
    #                 isprime=False
    #                 break
    #     return isprime
    # def NthTerm(self,N):
    #     flag=True
    #     i=1
    #     if(self.Prime(N)):
    #         return 0
    #     else:
    #         z=0
    #         z1=0
    #         while(flag):
    #             if(self.Prime(N+i) and self.Prime(N-i)):
    #                 z1=N+i
    #                 z=N-1
    #                 flag=False
    #             elif(self.Prime(N-i)):
    #                 z=N-i
    #                 flag=False
    #             elif(self.Prime(N+i)):
    #                 z1=N+i
    #                 flag=False
    #             i+=1
    #     if z1-N<=N-z:
    #         return z1-N
    #     else:
    #         return N-z


    def NthTerm(self,N):
        gap = 1
        if (self.isPrime(N)):
            return 0
        while (True):
            if (self.isPrime(N + gap) or self.isPrime(N - gap)):
                break
            gap += 1
        return gap

    def isPrime(self, n):
        if (n < 2):
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                return False
        return True


if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # N=int(input())
        N=10
        # N=7
        ob=Solution()
        ans=ob.NthTerm(N)
        print(ans)