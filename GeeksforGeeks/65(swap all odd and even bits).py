'''
Swap all odd and even bits

Given an unsigned integer N. The task is to swap all odd bits with even bits.
For example, if the given number is 23 (00010111), it should be converted to 43(00101011).
Here, every even position bit is swapped with adjacent bit on the right side(even position bits are highlighted in the binary representation of 23),
and every odd position bit is swapped with an adjacent on the left side.

Example 1:

Input: N = 23
Output: 43
Explanation:
Binary representation of the given number
is 00010111 after swapping
00101011 = 43 in decimal.

Example 2:

Input: N = 2
Output: 1
Explanation:
Binary representation of the given number
is 10 after swapping 01 = 1 in decimal.


Your Task: Your task is to complete the function swapBits() which takes an integer and returns an integer
with all the odd and even bits swapped.


Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 109
'''

class Solution:
    def swapBits(self,n):
        z=bin(n).replace('0b','')
        s1=''
        if len(z)%2!=0:
            z='0'+z
        # print(z)
        s1=''

        for i in range(len(z)):
            if i%2==0:
                s1+=z[i+1]
            else:
                s1+=z[i-1]

        return int(s1,2)




if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):

        # n=int(input())
        n=23
        # n=2
        ob=Solution()
        # ob.swapBits(n)
        print(ob.swapBits(n))
        T-=1