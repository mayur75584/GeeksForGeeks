'''
Save Ironman


Jarvis is weak in computing palindromes for Alphanumeric characters.
While Ironman is busy fighting Thanos, he needs to activate sonic punch but Jarvis is stuck in computing palindromes.
You are given a string S containing alphanumeric characters. Find out whether the string is a palindrome or not.
If you are unable to solve it then it may result in the death of Iron Man.

Example 1:

â€‹Input : S = "I am :IronnorI Ma, i"
Output : YES
Explanation:
Ignore all the symbol and whitespaces S = "IamIronnorIMai".
Now, Check for pallandrome ignoring uppercase and lowercase
english letter.


â€‹Example 2:

Input : S = Ab?/Ba
Output :  YES



Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function saveIronman() that takes an string (ch), and return the true if the string is a palindrome and false if the string is not a palindrome. The driver code takes care of the printing.

Expected Time Complexity: O(N). where N is the length of the string
Expected Auxiliary Space: O(1).



Constraints:
1 ≤ |S| ≤ 100000
Note: Consider alphabets and numbers only for palindrome check. Ignore symbols and whitespaces.
'''

import re

def saveIronman(s):
    s1=s.lower()
    s2=s1.replace(' ','')
    s3=re.sub('[^A-Za-z0-9]+','',s2)#Here re.sub is used to remove all special characters and whitespaces in single line
    print(s3)
    z=len(s3)
    if z%2==0:
        x=s3[z//2:]
        y=s3[:z//2]
        x1=''.join(list(reversed(x)))
        print(x1,y)
        if x1==y:
            return True
        else:
            return False
    else:
        x=s3[z//2+1:]
        y=s3[:z//2]
        x1=''.join(list(reversed(x)))
        print(x,y)
        print(x1)
        if x1==y:
            return True
        else:
            return False



for _ in range(0,int(input())):
    # s=input()
    s='I am :IroninorI Ma, i'
    ans=saveIronman(s)
    if(ans==True):
        print("YES")
    else:
        print("NO")