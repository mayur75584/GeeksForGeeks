'''
Reverse Bits

Given a non-negative integer n. Reverse the bits of n and print the number obtained after reversing the bits.
Note:  The actual binary representation of the number is being considered for reversing the bits, no leading 0’s are being considered.

Example 1:

Input :
N = 11
Output:
13
Explanation:
(11)10 = (1011)2.
After reversing the bits we get:
(1101)2 = (13)10.

Example 2:

Input :
N = 10
Output:
5
Explanation:
(10)10 = (1010)2.
After reversing the bits we get:
(0101)2 = (101)2
        = (5)10.

Your task:
You don't need to read input or print anything. Your task is to complete the function reverseBits() which takes an integer N as input and returns the number obtained after reversing bits.

Expected Time Complexity : O(number of bits in the binary representation of N)
Expected Auxiliary Space :  O(1)

Constraints :
1 ≤ N ≤ 109
'''

class Solution:
    def reverseBits(self,n):
        z=bin(n).replace('0b','')
        # print(z)
        x=z[::-1]
        # print(x)
        y=x.index('1')
        # print(y)
        z=x[y:]
        # print(int(z,2))
        return int(z,2)

if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # n=int(input())
        n=10
        ob=Solution()
        ob.reverseBits(n)
        # print(ob.reverseBits(n))
        T-=1