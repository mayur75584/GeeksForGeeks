'''
Search Pattern (Rabin-Karp Algorithm)

Given two strings, one is a text string and other is a pattern string.
The task is to print the indexes of all the occurences of pattern string in the text string.
 For printing, Starting Index of a string should be taken as 1.
Example 1:
Input:
S = "batmanandrobinarebat", pat = "bat"
Output: 1 18
Explanation: The string "bat" occurs twice
in S, one starts are index 1 and the other
at index 18.

â€‹Example 2:
Input:
S = "abesdu", pat = "edu"
Output: -1
Explanation: There's not substring "edu"
present in S.
Your Task:
You don't need to read input or print anything.
Your task is to complete the function search() which takes the string S and the string pat as inputs and returns an
array denoting the start indices (1-based) of substring pat in the string S.
Expected Time Complexity: O(|S|*|pat|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=105
1<=|pat|<|S|
'''
class Solution:
    def search(self,patt,s):
        #below is logic to find all index of one substring in main string in 1 based indexing
        res=[i+1 for i in range(len(s)) if s.startswith(patt,i)]
        if len(res)==0:
            res=[]
            res.append(-1)
            return res
        else:
            return res
if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # s=input()
        # patt=input()
        s='batmanandrobinarebat'
        patt='bat'
        ob=Solution()
        ans=ob.search(patt,s)
        for value in ans:
            print(value,end=' ')
        print()