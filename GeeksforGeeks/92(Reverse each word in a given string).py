'''
Reverse each word in a given string

Given a String. Reverse each word in it where the words are separated by dots.

Example 1:

Input:
S = "i.like.this.program.very.much"
Output: i.ekil.siht.margorp.yrev.hcum
Explanation: The words "i", "like",
"this", "program", "very", "much"
are all reversed.

â€‹Example 2:

Input:
S = "pqr.mno"
Output: rqp.onm
Explanation: Both "pqr" and "mno" are
reversed.


Your Task:
You don't need to read input or print anything. Your task is to complete the function reverseWords() which takes the string S as input and returns the resultant string by reversing all the words separated by dots.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).


Constraints:
1<=|S|<=105


'''

class Solution:
    def reverseWords(self,s):
        z=s.split('.')
        # print(z)
        a=[]
        s1=''
        for i in z:
            a.append(i[::-1])
        # print(s1)
        # print(a)
        return '.'.join(a)


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # s=input().strip()
        s='i.like.this.program.very.much'
        ob=Solution()
        ans=ob.reverseWords(s)
        print(ans)