'''
Generate Parentheses

Given an integer N representing the number of pairs of parentheses,
the task is to generate all combinations of well-formed(balanced) parentheses.


Example 1:

Input:
N = 3
Output:
((()))
(()())
(())()
()(())
()()()

Example 2:

Input:
N = 1
Output:
()


Your Task:
You don't need to read input or print anything.
Complete the function AllParenthesis() which takes N as input parameter
and returns the list of balanced parenthesis.

Expected Time Complexity: O(2N * N).
Expected Auxiliary Space: O(2*N*X), X = Number of valid Parenthesis.

Constraints:
1 ≤ N ≤ 12
'''

class Solution:
    def backtrack(self,open1,close,s,n,ans):
        if(len(s)==(2*n)):
            ans.append(''.join(s))
            return
        if(open1<n):
            s.append("(")
            self.backtrack(open1+1,close,s,n,ans)
            s.pop(-1)
        if(close<open1):
            s.append(")")
            self.backtrack(open1,close+1,s,n,ans)
            s.pop(-1)
    def AllParenthesis(self,n):
        ans=[]
        s=""
        s=list(s.split())
        self.backtrack(0,0,s,n,ans)
        return ans

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # n=3
        # n=1
        n=2
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(len(result)):
            print(result[i])