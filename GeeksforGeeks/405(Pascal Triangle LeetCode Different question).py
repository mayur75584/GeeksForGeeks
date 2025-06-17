'''
LeetCode

118. Pascal's Triangle
Solved
Easy
Topics


Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
'''
class Solution:
    def generator(self,i):
        ans_lst=[1]
        res=1
        for col in range(1,i):
            res=res*(i-col)
            res=res//col
            ans_lst.append(res)
        return ans_lst
    def generate(self,n):
        res=1
        ans=[]
        for i in range(1,n+1):
            ans.append(self.generator(i))
        print(ans)

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # n=5
        n=6
        ob=Solution()
        ans=ob.generate(n)
        print(ans)