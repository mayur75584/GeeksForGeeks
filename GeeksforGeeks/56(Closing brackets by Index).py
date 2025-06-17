'https://practice.geeksforgeeks.org/problems/closing-bracket-index5900/1/?category[]=Arrays&category[]=Strings&category[]=python&category[]=python-loops&category[]=OOP&category[]=Reverse&category[]=permutatuins&category[]=Arrays&category[]=Strings&category[]=python&category[]=python-loops&category[]=OOP&category[]=Reverse&category[]=permutatuins&problemStatus=unsolved&page=1&query=category[]Arrayscategory[]Stringscategory[]pythoncategory[]python-loopscategory[]OOPcategory[]Reversecategory[]permutatuinsproblemStatusunsolvedpage1category[]Arrayscategory[]Stringscategory[]pythoncategory[]python-loopscategory[]OOPcategory[]Reversecategory[]permutatuins'

'''
Closing bracket index 

Given a string with brackets ('[' and ']') and the index of an opening bracket. Find the index of the corresponding closing bracket.

Example 1:

Input:
S = "[ABC[23]][89]"
pos = 0
Output: 8
Explanation: [ABC[23]][89]
The closing bracket corresponding to the
opening bracket at index 0 is at index 8.

â€‹Example 2:

Input: 
S = "ABC[58]"
pos = 3
Output: 6
Explanation: ABC[58]
The closing bracket corresponding to the
opening bracket at index 3 is at index 6.


Your Task:
You don't need to read input or print anything. Your task is to complete the function closing() which takes a string S and a position pos as inputs and returns the index of the closing bracket corresponding to the opening bracket at index pos.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


Constraints:
1 <= N <= 2*105

 
'''
class Solution:
    def closing(self,s,pos):
        counter=0
        cnt=0
        z=0
        for i in s[pos:]:
            if i=='[':
                counter+=1
            elif i==']':
                counter-=1
                cnt+=1
            if counter==0 and i==']':
                z=s.index(i,s.index(i)+(cnt-1)) #This line is the important logic
                break
            # if i==']':
            #     counter-=1
            #     cnt+=1
            # if counter==0:
            #     break
        return z






# t=int(input())
t=1
for tc in range(t):
    # s=input()
    # pos=int(input())
    # s='[ABC[23]][89]'
    # pos=0
    s='ABC[58]'
    pos=3
    ob=Solution()
    # ob.closing(s,pos)
    print(ob.closing(s,pos))