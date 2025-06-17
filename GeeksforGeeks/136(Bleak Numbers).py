'''
Bleak Numbers

Given an integer, check whether it is Bleak or not.

A number ‘n’ is called Bleak if it cannot be represented as sum of a positive number x
and set bit count in x, i.e., x + countSetBits(x) is not equal to n for any non-negative number x.

Example 1:
Input: 4
Output: 1
Explanation: There is no any possible x
such that x + countSetbit(x) = 4

Example 2:
Input: 3
Output: 0
Explanation: 3 is not a Bleak number as
2 + countSetBit(2) = 3.



Your Task:
You don't need to read or print anything.
Your task is to complete the function is_bleak() which takes n as input parameter and
returns 1 if n is not a Bleak number otherwise returns 0.


Expected Time Complexity: O(log(n) * log(n))
Expected Space Complexity: O(1)


Constraints:
1 <= n <= 104
'''
class Solution:
    def is_bleak(self,n):
        for i in range(1,n+1):
            x=i
            z=bin(i).replace('0b','')
            x1=z.count('1')
            if int(x1)+x==n:
                return 0
        else:
            return 1
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n=int(input())
        ob=Solution()
        ans=ob.is_bleak(n)
        print(ans)