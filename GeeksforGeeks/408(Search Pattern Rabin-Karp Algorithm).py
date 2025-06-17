'''
Search Pattern (Rabin-Karp Algorithm)
Difficulty: MediumAccuracy: 34.53%Submissions: 75K+Points: 4Average Time: 20m
Given two strings:

A text string in which you want to search.

A pattern string that you are looking for within the text.

Return all positions (1-based indexing) where the pattern occurs as a substring in the text. If the pattern does not occur, return an empty list.

All characters in both strings are lowercase English letters (a to z).

Examples:

Input: text = "birthdayboy", pattern = "birth"
Output: [1]
Explanation: The string "birth" occurs at index 1 in text.
Input: text = "geeksforgeeks", pattern = "geek"
Output: [1, 9]
Explanation: The string "geek" occurs twice in text, one starts are index 1 and the other at index 9.
Constraints:
1<= text.size() <=5*105
1<= pattern.size() <= text.size()


'''


class Solution:
    def search(self,pat,txt):

        positions = [i+1 for i in range(len(txt)) if txt.startswith(pat,i)]
        return positions


if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # txt,pat = map(str,input().split())
        # txt,pat = "birthdayboy", "birth"
        txt,pat = "geeksforgeeks","geeks"
        obj=Solution()
        print(obj.search(pat,txt))
        t-=1