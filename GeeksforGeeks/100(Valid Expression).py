
'''

Valid Expression
Medium Accuracy: 78.47% Submissions: 1879 Points: 4

Given a string S, composed of different combinations of '(' , ')', '{', '}', '[', ']'. The task is to verify the validity of the arrangement.
Note: Ignore the precedence of brackets.

Example 1:

Input:
S = ()[]{}
Output: 1
Explanation: The arrangement is valid.



Example 2:

Input:
S = ())({}
Output: 0
Explanation: Arrangement is not valid.



Your Task:
You dont need to read input or print anything. Complete the function valid() which takes S as input and returns a boolean value denoting whether the arrangement is valid or not.


Expected Time Complexity: O(N) where N is the length of S.
Expected Auxiliary Space: O(N)


Constraints:
1 <= N <= 104
'''

class Solution:
    def valid(self ,s):
        stack =[]
        for i in s:
            if i== '(':
                stack.append(i)
            elif i == '[':
                stack.append(i)
            elif i == '{':
                stack.append(i)
            else:
                if (i == ')' or i == ']' or i == '}') and len(stack) == 0:
                    return 0
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == ')' and stack[-1] != '(':
                    return 0
                elif i == ']' and stack[-1] != '[':
                    return 0
                elif i == '}' and stack[-1] != '{':
                    return 0
        if len(stack) == 0:
            return 1
        else:
            return 0


if __name__ == '__main__':
    # t=int(input())
    t = 1
    for i in range(t):
        # s=input().strip()
        # s='()[]{}'
        s = '())({}'
        ob = Solution()
        if ob.valid(s):
            print(1)
        else:
            print(0)