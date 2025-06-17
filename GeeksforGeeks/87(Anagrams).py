'''
Anagram

Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “act” and “tac” are an anagram of each other.

Example 1:

Input:
a = geeksforgeeks, b = forgeeksgeeks
Output: YES
Explanation: Both the string have same
characters with same frequency. So,
both are anagrams.

Example 2:

Input:
a = allergy, b = allergic
Output: NO
Explanation:Characters in both the strings
are not same, so they are not anagrams.

Your Task:
You don't need to read input or print anything.Your task is to complete the function isAnagram() which takes the string a and string b as input parameter and check if the two strings are an anagram of each other. The function returns true if the strings are anagram else it returns false.

Expected Time Complexity: O(|a|+|b|).
Expected Auxiliary Space: O(Number of distinct characters).

Note: |s| represents the length of string s.

Constraints:
1 ≤ |a|,|b| ≤ 105
'''

class Solution:
    def isAnagram(self,a,b):
        x=sorted(a)
        y=sorted(b)
        for i in range(len(x)):
            if len(x)==len(y):

                if x[i]==y[i]:

                    if x.count(x[i])!=y.count(y[i]):
                        return False
                else:
                    return False
            else:
                return False
        return True

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # a,b=map(str,input().strip().split())
        # a,b='geeksforgeeks','forgeeksgeeks'
        # a,b='allergy','allergic'
        a,b='abcdef','cdefabmn'
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO")