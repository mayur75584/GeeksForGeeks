'''
Distinct Substrings

Given a string s consisting of uppercase and lowercase alphabetic characters. Return the  number of distinct substrings of size 2 that appear in s as contiguous substrings.

Example

Input :
s = "ABCAB"
Output :
3
Explanation:  For "ABCAB", the
three distinct substrings of size
2 are "AB", "BC" and "CA".

Example

Input :
s = "XYZ"
Output :
2
Explanation: For "XYZ", the
two distinct substrings of size 2 are
"XY" and "YZ".

Your Task :

You don't need to read input or print anything. You have to complete the function fun() which takes the string s as input parameter and returns the number of distinct contiguous substring of size 2.

Expected Time Complexity : O(|s|)
Expected Auxilliary Space : O(|s|)

Constraints:
1<=|s|<=100

|s| denotes the length of the string s.
'''

class Solution:
    def fun(self,s):
        lst=[]
        i=0
        j=1
        while (j!=len(s)):
            x=s[i:j+1]
            if x not in lst:
                lst.append(x)
            i+=1
            j+=1
        return len(lst)



if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # s=input()
        # s='ABCAB'
        s='XYZ'
        solObj = Solution()
        print(solObj.fun(s))