'''
Minimum characters to be added at front to make string palindrome

Given string str of length N. The task is to find the minimum characters
to be added at the front to make string palindrome.
Note: A palindrome is a word which reads the same backward as forward. Example: "madam".

Example 1:

Input:
S = "abc"
Output: 2
Explanation:
Add 'b' and 'c' at front of above string to make it
palindrome : "cbabc"

Example 2:

Input:
S = "aacecaaa"
Output: 1
Explanation: Add 'a' at front of above string
to make it palindrome : "aaacecaaa"

Your Task:
You don't need to read input or print anything.
Your task is to complete the function minChar() which takes a string S
and returns an integer as output.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= S.length <= 106

'''
'''
Using Two Pointer Approch

If we find Longest Palindromic Substring we can get solution

        bbac
        here longest palindromic substrign is bb
        so bbac-bb = ac
        so cabbac (reversing ac) will give us answer
'''
class Solution:
    def minChar(self,s):
        i=0
        j=len(s)-1
        trim=j
        res=0

        while(i<j):
            if(s[i]==s[j]):
                i+=1
                j-=1
            else:
                res+=1
                i=0 #Again we start comparing from starting
                trim-=1
                j=trim
        return res


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # s=input()
        # s='aacecaaa'
        s='abc'
        obj=Solution()
        ans=obj.minChar(s)
        print(ans)