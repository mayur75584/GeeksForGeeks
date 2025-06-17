'''
Roman Number to Integer

Given a string in roman no format (s)  your task is to convert it to an integer .
Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

Example 1:

Input:
s = V
Output: 5

Example 2:

Input:
s = III
Output: 3

Your Task:
Complete the function romanToDecimal() which takes a string as input parameter and returns the equivalent decimal number.

Expected Time Complexity: O(|S|), |S| = length of string S.
Expected Auxiliary Space: O(1)

Constraints:
1<=roman no range<=3999
'''
class Solution:
    def romanToDecimal(self,S):
        dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=len(S)
        if n==1:
            return dict1[S[0]]
        else:
            res=dict1[S[n-1]]
            for i in range(n-2,-1,-1):
                c=S[i]
                if dict1[c]>=dict1[S[i+1]]:
                    res=res+dict1[c]
                else:
                    res=res-dict1[c]
            return res





if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        ob=Solution()
        # S=input()
        # S='III'
        S='VI'
        print(ob.romanToDecimal(S))