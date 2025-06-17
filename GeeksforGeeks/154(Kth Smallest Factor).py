



'https://practice.geeksforgeeks.org/problems/count-the-number-of-subarrays/1'
'https://practice.geeksforgeeks.org/problems/distinct-palindromic-substrings5141/1'
'https://practice.geeksforgeeks.org/problems/next-smallest-palindrome4740/1'
'Above problems was not able to do'
'''
Kth Smallest Factor 

GIven two positive integers N and K. You have to find the Kth smallest factor of N. A factor of N is a positive integer which divides N. Output the Kth smallest factor of N if it exists otherwise print -1.

 

Example 1:

Input : N = 4 , K = 2
Output: 2
Explanation:
All factors of 4 are 1,2 and 4. Out of
these 2 is the 2nd smallest.

Example 2:

Input : N = 4 , K = 3
Output: 4
Explanation:
All factors of 4 are 1,2 and 4. Out of
these 4 is the 3rd smallest.

 

Your Task:
You don't need to read input or print anything. Your task is to complete the function kThSmallestFactor() which takes 2 Integers N and K as input and returns the answer.

 

Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 106
1 <= K <= 106
'''

class Solution:
    def kthSmallestFactor(self,N,K):
        z=[]
        i=1
        while i*i <= N:
            if N%i==0:
                z.append(i)

                if N//i !=i:
                    z.append(N//i)
            i+=1
        z.sort()
        print(z)


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N,K=map(int,input().split())
        # N,K=4,2
        # N,K=4,3
        N,K=8,5
        ob=Solution()
        print(ob.kthSmallestFactor(N,K))



