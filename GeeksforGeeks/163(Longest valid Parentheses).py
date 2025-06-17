'''
Longest valid Parentheses

Given a string S consisting of opening and closing parenthesis '(' and ')'.
Find length of the longest valid parenthesis substring.

A parenthesis string is valid if:

    For every opening parenthesis, there is a closing parenthesis.
    Opening parenthesis must be closed in the correct order.
Example 1:
Input: S = ((()
Output: 2
Explaination: The longest valid
parenthesis substring is "()".

Example 2:
Input: S = )()())
Output: 4
Explaination: The longest valid
parenthesis substring is "()()".

Your Task:
You do not need to read input or print anything. Your task is to complete the function maxLength()
which takes string S as input parameter and returns the length of the maximum valid parenthesis substring.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)
Constraints:
1 ≤ |S| ≤ 105  
'''
'''
In stack we are pushing indexes of parenthesis not parenthesis

'''
class Solution:
    def maxLength(self,S):
        stack=[-1]
        result=0
        for i in range(len(S)):
            if(S[i]=='('):
                stack.append(i)
            else:
                if(len(stack)!=0):
                    stack.pop(-1)
                if(len(stack)!=0):
                    result=max(result,i-stack[-1])
                else:
                    stack.append(i)
        return result
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # S=input()
        # S=')()())'
        S='((()'
        ob=Solution()
        print(ob.maxLength(S))