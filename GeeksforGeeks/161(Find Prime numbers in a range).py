'''
Find Prime numbers in a range

Given two integers M and N, generate all primes between M and N.

Example 1:

Input:
M=1,N=10
Output:
2 3 5 7
Explanation:
The prime numbers between 1 and 10
are 2,3,5 and 7.

Example 2:

Input:
M=2, N=5
Output:
2,3,5
Explanation:
The prime numbers between 2 and 5 are
2,3 and 5.


Your Task:
You don't need to read input or print anything. Your task is to complete the function primeRange() which takes 2 integer inputs M and N and returns a list of all primes between M and N.


Expected Time Complexity:O(N*sqrt(N))
Expected Auxillary Space:O(1)


Constraints:
1<=M<=N<=106
'''


class Solution:
    def primeRange(self,M,N):
        z = []
        for i in range(M, N + 1):
            if i == 0 or i == 1:
                continue
            elif i==2:
                z.append(i)
            elif i==3:
                z.append(i)
            else:
                for j in range(2, int(i**0.5)+1):
                    if (i % j == 0):
                        break
                else:
                    z.append(i)
        return z



if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # M,N=map(int,input().split())
        # M,N=1,10
        M,N=2,5
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=' ')
        print()