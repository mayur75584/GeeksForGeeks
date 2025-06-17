'''
Geek and Number String

Geek has a string Sof size Nconsisting of characters from '0'to '9'.
He wants to minimise the length of the string.
In each minimising operation,
geek can remove any two consecutive characters if they are of the form {"12", "21", "34", "43", "56", "65", "78", "87", "09", "90"}.
Find the minimum possible length of the string after applying minimising operations.


Example 1:

Input:
N = 5
S = "12213"
Output: 1
Explanation: Geek can get the string of
length 1 in two minimising operation,
In 1st operation Geek will remove "12"
from "12213" then Geek left with "213"
In 2nd operation Geek will remove "21"
from "213" then Geek left with "3"



Example 2:

Input:
N = 4
S = "1350"
Output: 4
Explanation: Can't remove any character.



Your Task:
You don't need to read input or print anything.
Complete the functionminLength() which takes N and S as input parameters
and returns the the minimum possible length of the string.


Expected Time Complexity: O(N)
Expected Auxiliary Space:O(N)


Constraints:
1 ≤ N ≤ 105

'''
class Solution:
    def minLength(self,s,n):
        lst=["12", "21", "34", "43", "56", "65", "78", "87", "09", "90"]
        stack=[]
        count1=n
        i=0
        while(i<n):
            if len(stack)==0:
                stack.append(s[i])
            else:
                x=stack.pop(-1)
                if str(x)+str(s[i]) in lst:
                    count1-=2
                else:
                    stack.append(x)
                    stack.append(s[i])
            i+=1
        return count1

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # s=input()
        # n=5
        # s='12213'
        n=4
        s='1350'
        ob=Solution()
        print(ob.minLength(s,n))

