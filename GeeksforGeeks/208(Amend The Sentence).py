'''
Amend The Sentence

Given a string which is basically a sentence without spaces between words.
However the first letter of every word is in uppercase.
You need to print this sentence after following amendments:
(i) Put a single space between these words
(ii) Convert the uppercase letters to lowercase.
Note: The first character of the string can be both uppercase/lowercase.

Example 1:
Input:
s = "BruceWayneIsBatman"
Output: bruce wayne is batman
Explanation: The words in the string are
"Bruce", "Wayne", "Is", "Batman".

â€‹Example 2:
Input:
s = "You"
Output: you
Explanation: The only word in the string
is "You".

Your Task:
You don't need to read input or print anything.
Your task is to complete the function amendSentence() which takes
the string s as input and returns a string with the stated amendments.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (for output string).

Constraints:
1<=Size of String <=106
'''

class Solution:
    def amendSentence(self,s):
        res=''
        s1=s[0]
        i=1
        while(i<len(s)):
            if s[i].isupper():
                res+=s1.lower()+' '
                s1=''
                s1+=s[i]
            else:
                s1+=s[i]
            i+=1
        if len(s1)>0:
            res+=s1.lower()
        return res


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # s=input()
        # s='BruceWayneIsBatman'
        s='You'
        solObj=Solution()
        print(solObj.amendSentence(s))
