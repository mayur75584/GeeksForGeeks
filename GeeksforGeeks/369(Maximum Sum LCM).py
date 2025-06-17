'''
Maximum Sum LCM

Given a positive number n.
You need to write a program to find the maximum sum of distinct numbers such that the LCM of all these numbers is equal to n.

Example 1:

Input: n = 2
Output: 3 
Explanation: The distinct numbers you can have are
just 1 and 2 and their sum is equal to 3.

Example 2:

Input: n = 5
Output: 6
Explanation: The distinct numbers you can have
are just 1 and 5 and their sum is equal to 6.


Your Task:  
You dont need to read input or print anything.
Complete the function maxSumLCM() which takes n as input parameter
and returns the maximum sum of distinct numbers such that the LCM of all these numbers is equal to n.

Expected Time Complexity: O(sqrt(n))
Expected Auxiliary Space: O(1)

Constraints:
1<= N <=1000000000

'''
import math
class Solution:
    def maxSumLCM(self,n):
        factors=[]
        for i in range(1,int(math.sqrt(n))+1):
            if(n%i==0):
                if i not in factors:
                    factors.append(i)
                if int(n/i) not in factors:
                    factors.append(int(n/i))
        print(factors)
        return sum(factors)


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # n=5
        # n=44
        n=4
        ob=Solution()
        print(ob.maxSumLCM(n))