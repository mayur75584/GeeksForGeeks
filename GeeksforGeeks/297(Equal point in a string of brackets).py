'''
Equal point in a string of brackets

Given a string S of opening and closing brackets '(' and ')' only.
The task is to find an equal point. An equal point is an index such
that the number of closing brackets on right from that point must be equal
to number of opening brackets before that point.

Example 1:
Input: str = "(())))("
Output: 4
Explanation:
After index 4, string splits into (())
and ))(. Number of opening brackets in the
first part is equal to number of closing
brackets in the second part.

Example 2:
Input : str = "))"
Output: 2
Explanation:
As after 2nd position i.e. )) and "empty"
string will be split into these two parts:
So, in this number of opening brackets i.e.
0 in the first part is equal to number of
closing brackets in the second part i.e.
also 0.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function findIndex() which
takes the string S as inputs and returns the occurrence of the equal point in the string.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ S ≤ 106
String can be unbalanced
'''

class Solution:
    def findIndex(self,s):
        'Getting TLE for below slicing code'
        # if len(s)==1 and s=='(':
        #     return 0
        # if len(s)==1 and s==')':
        #     return 1
        # for i in range(len(s)):
        #     x=s[:i+1]
        #     y=s[i+1:]
        #     if x.count("(")==y.count(")"):
        #         return i+1
        # return len(s)
        open=[]
        close=[]
        c1=0
        c2=0
        if len(s)==1 and s=='(':
            return 0
        if len(s)==1 and s==')':
            return 1
        if len(set(s))==1:
            return len(s)
        for i in range(len(s)):
            if s[i]=='(':
                c1+=1
            open.append(c1)
        for i in range(len(s)-1,-1,-1):
            if s[i]==')':
                c2+=1
            close.append(c2)
        close=close[::-1]
        print(open)
        print(close)
        for i in range(len(open)-1):
            if open[i]==close[i+1]:
                return i+1

if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # s=input()
        # s='(())))('
        s='))'
        # s='))))(()'
        # s='('
        # s=')'
        ob=Solution()
        print(ob.findIndex(s))

        T-=1