'''
Sequence Fun

You have a sequence 2,5,16,65,........Given an integer n as input.
You have to find the value at the nth position in the sequence.


Example 1:

Input: n = 4
Output: 65

Example 2:

Input: n = 10
Output: 9864101



Your Task:

You don't need to read or print anything,
Your task is to complete the function NthTerm()
which takes n as input parameter and returns value
at nth position of the given sequence modulo 109 + 7.


Expected Time Complexity:  O(n)
Expected Space Complexity: O(1)


Constraints:
1 <= n <= 104

'''
class Solution:
    def NthTerm(self,n):
        sum1 = 1
        for i in range(1, n + 1):
            sum1 = (sum1 * i) + 1
        res = sum1 % ((10 ** 9) + 7)
        return res

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n=int(input())
        ob=Solution()
        ans=ob.NthTerm(n)
        print(ans)