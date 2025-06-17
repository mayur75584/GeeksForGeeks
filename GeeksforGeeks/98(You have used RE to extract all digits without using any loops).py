
'''
re - regular expression is used to extract all the digits without
using any for loop from the string

Extract the Number from the String

Given a sentence containing several words and numbers. Find the largest number among them which does not contain 9.

Example 1:

Input:
Sentence="This is alpha 5057 and 97"
Output:
5057
Explanation:
5057 is the only number that does
not have a 9.

Example 2:

Input:
Sentence="Another input 9007"
Output:
-1
Explanation:
Since there is no number that
does not contain a 9,output is -1.

Your task:
You don't need to read input or print anything. Your task is to complete the function ExtractNumber() which takes a string S as input parameter and returns the largest number that does not contain a 9. If no such number exists, return -1.

Expected Time Complexity:O(N)
Expected Auxillary Space:O(1)

Constraints:
1<=Length of Sentence<=106
1<=answer<=1018
'''
import re

class Solution:
    def ExtractNumber(self,S):
        temp=re.findall(r'\d+',S) #extract digits from strings using RE
        res=list(map(int,temp))
        res1=sorted(res,reverse=True)
        for i in res1:
            if '9' not in str(i):
                return i
        else:
            return -1


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # S=input()
        S='This is alpha 5057 and 97'
        ob=Solution()
        ans=ob.ExtractNumber(S)
        print(ans)



