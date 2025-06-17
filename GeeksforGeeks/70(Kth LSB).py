'''
Kth LSB

A number N is given. Find its ‘K’th Least Significant Bit.

Example 1:

Input: N = 10, K = 4
Output: 1
Explanation: Binary Representation
of 10 is 1010. 4th LSB is 1.

â€‹Example 2:

Input: N = 16, K = 3
Output: 1
Explanation: Binary Representation of
16 is 10000. 3rd LSB is 0.

Your Task:
You don't need to read input or print anything. Your task is to complete the function KthLSB() which takes the N and K as inputs and returns the bit (1 or 0) in K'th LSB.
Expected Time Complexity: O(K)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 109
1 ≤ K ≤ 32
'''

class Solution:
    def KthLSB(self,n,k):
        z=bin(n).replace('0b','')
        # print(z)
        if len(z)<k:
            return 0
        else:
            return z[-k]


if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # n,k=input().split()
        # n=int(n)
        # k=int(k)
        # n=16
        # k=3
        n=99894785
        k=20
        ob=Solution()
        ans=ob.KthLSB(n,k)
        print(ans)