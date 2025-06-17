'''
IPL 2021 - Final

IPL 2021 Finals are here and it is between the most successful team
of the IPL Mumbai Indians and the team striving to garb their first trophy
Royal Challengers Banglore. Rohit Sharma, captain of the team Mumbai Indians
has the most experience in IPL finals, he feels lucky if he solves a programming
question before the IPL finals. So, he asked the team's head coach  Mahela
Jayawardene for a question. Question is, given a string S consisting only
of opening and closing parenthesis 'ie '('  and ')',  the task is to find out
the length of the longest valid parentheses substring.

NOTE: The length of the smallest valid substring ( ) is 2.

Example 1:
Input: S = "(()("
Output: 2
Explanation: The longest valid
substring is "()". Length = 2.

Example 2:
Input: S = "()(())("
Output: 6
Explanation: The longest valid
substring is "()(())". Length = 6.

Your Task:
You don't need to read input or print anything.
Complete the function findMaxLen() which takes S as input parameter
and returns the max length.

Constraints:
1 ≤ |S|  ≤ 105
'''

class Solution:
    def findMaxLen(self,S):
        stack = [-1]
        result = 0
        for i in range(len(S)):
            if (S[i] == '('):
                stack.append(i)
            else:
                if (len(stack) != 0):
                    stack.pop(-1)
                if (len(stack) != 0):
                    result = max(result, i - stack[-1])
                else:
                    stack.append(i)
        return result

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # S=input()
        S='(()('

        ob=Solution()
        print(ob.findMaxLen(S))
