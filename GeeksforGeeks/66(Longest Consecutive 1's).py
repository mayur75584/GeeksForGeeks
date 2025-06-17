'''

Longest Consecutive 1's

Given a number N. Find the length of the longest consecutive 1s in its binary representation.

Example 1:

Input: N = 14
Output: 3
Explanation:
Binary representation of 14 is
1110, in which 111 is the longest
consecutive set bits of length is 3.

Example 2:

Input: N = 222
Output: 4
Explanation:
Binary representation of 222 is
11011110, in which 1111 is the
longest consecutive set bits of length 4.

Your Task:
You don't need to read input or print anything. Your task is to complete the function maxConsecutiveOnes()
which returns the length of the longest consecutive 1s in the binary representation of given N.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106

'''

class Solution:
    def maxConsecutiveOnes(self,N):
        z=bin(N).replace('0b','')
        # print(z)
        lst=[]
        if z.__contains__('0'):
            lst=z.split('0')
            # print(lst)
            # print(max(*lst))
            return len(max(*lst))
        else:
            return len(z)

if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # n=int(input())
        # n=14
        # n=222
        # n=384
        n=4095
        obj = Solution()
        # obj.maxConsecutiveOnes(n)
        print(obj.maxConsecutiveOnes(n))
        T-=1