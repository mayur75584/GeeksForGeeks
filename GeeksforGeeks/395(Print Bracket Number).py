'''
Print Bracket Number

Given a string str, the task is to find the bracket numbers, i.e., for each bracket in str, return i if the bracket is the ith opening or closing bracket to appear in the string.

 Examples:

Input:  str = "(aa(bdc))p(dee)"
Output: 1 2 2 1 3 3
Explanation: The highlighted brackets in
the given string (aa(bdc))p(dee) are
assigned the numbers as: 1 2 2 1 3 3.
Input:  str = "(((()("
Output: 1 2 3 4 4 5
Explanation: The highlighted brackets in
the given string (((()( are assigned
the numbers as: 1 2 3 4 4 5
Expected Time Complexity: O(|str|)
Expected Auxiliary Space: O(|str|)

Constraints:
1 <= |str| <= 105
str contains lowercase English alphabets, and '(', ')' characters
At any index, the number of opening brackets is greater than or equal to closing brackets

Seen this question in a real interview before ?
Yes
No
Company Tags
Flipkart
Topic Tags
StringsStackRegular ExpressionData Structures
'''
'''
Note here in gfg problem hint it is given to keep track of opening id
in stack means keep track of count of opening id's i.e ( .
'''
class Solution:
    def bracketNumbers(self,S):
        lst=[]
        stack=[]
        count1=0
        for i in S:
            if i=="(":
                count1+=1
                stack.append(count1)
                lst.append(count1)
            elif i==")":
                if len(stack)!=0:
                    lst.append(stack.pop(-1))
        return lst

if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # S=input()
        S="(aa(bdc))p(dee)"
        # S="(((()("
        ob=Solution()
        answer=ob.bracketNumbers(S)
        for value in answer:
            print(value,end=" ")
        print()