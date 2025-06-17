'''
Generate Parentheses

Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]



Constraints:

    1 <= n <= 8


'''
'''
Here backtracking is used.

two conditions

open<n

close<open
'''

class Solution:
    def backtrack(self,open,close,s,n,ans):
        if(len(s)==2*n):
            ans.append(''.join(s))
            return
        if(open<n):
            s.append('(')
            self.backtrack(open+1,close,s,n,ans)
            s.pop(-1)
        if(close<open):
            s.append(')')
            self.backtrack(open,close+1,s,n,ans)
            s.pop(-1)
    def generateParenthesis(self,n):
        ans=[]
        s=""
        s=list(s.split())
        self.backtrack(0,0,s,n,ans)
        return ans

if __name__ == '__main__':
    # n=int(input())
    n=3
    # n=1
    ob=Solution()
    print(ob.generateParenthesis(n))