'''
Parenthesis Checker

Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.

Example 1:

Input:
{([])}
Output:
true
Explanation:
{ ( [ ] ) }. Same colored brackets can form
balaced pairs, with 0 number of
unbalanced bracket.

Example 2:

Input:
()
Output:
true
Explanation:
(). Same bracket can form balanced pairs,
and here only 1 type of bracket is
present and in balanced way.

Example 3:

Input:
([]
Output:
false
Explanation:
([]. Here square bracket is balanced but
the small bracket is not balanced and
Hence , the output will be unbalanced.

Your Task:
This is a function problem. You only need to complete the function ispar() that takes a string as a parameter and returns a boolean value true if brackets are balanced else returns false.
The printing is done automatically by the driver code.

Expected Time Complexity: O(|x|)
Expected Auixilliary Space: O(|x|)

Constraints:
1 ≤ |x| ≤ 32000

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".
'''



class Solution:
    def ispar(self,x):
        stack=[]
        for i in x:
            if i in ['{','[','(']:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False

                if i=='}':
                    if stack[-1]=='{':
                        stack.pop()
                        continue
                    else:
                        return False
                if i==']':
                    if stack[-1]=='[':
                        stack.pop()
                        continue
                    else:
                        return False
                if i==')':
                    if stack[-1]=='(':
                        stack.pop()
                        continue
                    else:
                        return False
        if len(stack)==0:
            return True
        else:
            return False
if __name__ == '__main__':
    # test_cases = int(input())
    test_cases=1
    for cases in range(test_cases):
        # s=str(input())
        # s="{([])}"
        s="{}{(}))}"
        # s="("
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")