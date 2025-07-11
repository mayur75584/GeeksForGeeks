'https://practice.geeksforgeeks.org/problems/tom-and-string1211/1/?problemStatus=unsolved&page=6&sortBy=newest&query=problemStatusunsolvedpage6sortBynewest'
'''
Tom and String

Given a list S consisting of strings separated by a space. Hash the list using the hash rule and a long string X given below and return the hash value.
String X: "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ".
Hash Rule: Hash is the summation of all the character values in the input: (currentIndex + (position of the character In the string initial) ). And then this hash is multiplied by the number of strings in the list.

 

Example 1:

Input:
S = aA1 b
Output:
132
Explanation: 
List is ["aA1", "b"]
a: 0 + 0 = 0
A: 1 + 36 = 37
1: 2 + 26 = 28

b: 0 + 1 = 1
So, 2*(0+1+37+28) = 2*(66) = 132

Example 2:

Input:
S = aa BB cc DD
Output:
640
Explanation: 
List is ["aa", "BB","cc","DD"]
a: 0 + 0 = 0
a: 1 + 0 = 1

B: 0 + 37 = 37
B: 1 + 37 = 38

c: 0 + 2 = 2
c: 1 + 2 = 3

D: 0 + 39 = 39
D: 1 + 39 = 40
So, 4*(0+1+37+38+2+3+39+40)= 4*(160)=640

 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function hashString() which takes string S, list of space-separated strings as a parameter and returns the hash value of the list.

 

Expected Time Complexity: O(Sum of the length of all the strings)
Expected Auxiliary Space: O(Length of initial string)

 

Constraints:
1 ≤ Length of a string ≤ 30
1 ≤ Number of strings in a list ≤ 20
'''

class Solution:
    def hashString(self,S):
        s='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        x=S.split()
        result=[]
        for i in x:
            for j in i:
                c=i.count(j)
                if c==1:
                    z=i.index(j)+s.index(j)
                    result.append(z)
                else:
                    z=i.index(j)+s.index(j)
                    result.append(z)
                    i=i.replace(j,'%',1)
        print(len(x))
        print(result)
        print(sum(result))
        return len(x)*sum(result)





if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # s=input()
        # s='aa BB cc DD'
        s='aA1 b'
        ob=Solution()
        print(ob.hashString(s))