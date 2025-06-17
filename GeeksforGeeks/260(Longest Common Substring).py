'''
Longest Common Substring

Given two strings. The task is to find the length of the longest common substring.


Example 1:

Input: S1 = "ABCDGH", S2 = "ACDGHR"
Output: 4
Explanation: The longest common substring
is "CDGH" which has length 4.

Example 2:

Input: S1 = "ABC", S2 "ACB"
Output: 1
Explanation: The longest common substrings
are "A", "B", "C" all having length 1.


Your Task:
You don't need to read input or print anything.
Your task is to complete the function longestCommonSubstr() which takes
the string S1, string S2 and their length n and m as inputs
and returns the length of the longest common substring in S1 and S2.


Expected Time Complexity: O(n*m).
Expected Auxiliary Space: O(n*m).


Constraints:
1<=n, m<=1000
'''
'''
Dynamic Programming can be used to find the longest common substring in O(m*n) time.
The idea is to find the length of the longest common suffix for all substrings of both strings and store these lengths in a table.

The longest common suffix has following optimal substructure property.
If last characters match, then we reduce both lengths by 1
LCSuff(X, Y, m, n) = LCSuff(X, Y, m-1, n-1) + 1 if X[m-1] = Y[n-1]
If last characters do not match, then result is 0, i.e.,
LCSuff(X, Y, m, n) = 0 if (X[m-1] != Y[n-1])
Now we consider suffixes of different substrings ending at different indexes.
The maximum length Longest Common Suffix is the longest common substring.
LCSubStr(X, Y, m, n) = Max(LCSuff(X, Y, i, j)) where 1 <= i <= m and 1 <= j <= n
'''
'''
Debug it you will better understand the solution
'''
class Solution:
    def longestCommonSubstr(self,S1,S2,n,m):
        LCSuffix=[[0 for k in range(m+1)] for l in range(n+1)]
        print(LCSuffix)

        result=0

        for i in range(n+1):
            for j in range(m+1):
                if(i==0 or j==0):
                    LCSuffix[i][j]=0
                elif(S1[i-1]==S2[j-1]):
                    LCSuffix[i][j]=LCSuffix[i-1][j-1]+1
                    result=max(result,LCSuffix[i][j])
                else:
                    LCSuffix[i][j]=0
        return result


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n,m=map(int,input().split())
        # S1=input()
        # S2=input()
        # n,m=6,6
        # S1='ABCDGH'
        # S2='ACDGHR'
        n,m=3,3
        S1='ABC'
        S2='ACB'
        ob=Solution()
        print(ob.longestCommonSubstr(S1,S2,n,m))