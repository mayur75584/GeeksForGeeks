
# 'https://practice.geeksforgeeks.org/problems/finding-the-numbers0215/1#'
'''
Case-specific Sorting of Strings

Given a string S consisting of uppercase and lowercase characters.
The task is to sort uppercase and lowercase letters separately such that
if the ith place in the original string had an Uppercase character then it should not have a lowercase character
after being sorted and vice versa.

Example 1:
Input:
N = 12
S = defRTSersUXI
Output: deeIRSfrsTUX
Explanation: Sorted form of given string
with the same case of character as that
in original string is deeIRSfrsTUX

Example 2:
Input:
N = 6
S = srbDKi
Output: birDKs
Explanation: Sorted form of given string
with the same case of character will
result in output as birDKs.

Your Task:
You only need to complete the function caseSort that returns sorted string.

Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 103
'''

class Solution:
    def caseSort(self,s,n):
        s1=''
        z=sorted(s)
        print(z)
        x=''
        y=''
        for i in z:
            if i.isupper():
                x+=i
            elif i.islower():
                y+=i
        print(x,y)
        for i in range(len(s)):
            if s[i].isupper():
                s1+=x[0]
                x=x.replace(x[0],'',1)
            else:
                s1+=y[0]
                y=y.replace(y[0],'',1)
        return s1
if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # s=input()
        # n=12
        # s='defRTSersUXI'
        n=6
        s='srbDKi'
        print(Solution().caseSort(s,n))





