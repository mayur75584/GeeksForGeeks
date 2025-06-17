'''
Rearrange a string

Given a string containing uppercase alphabets and integer digits (from 0 to 9), the task is to print the alphabets in the lexicographical order followed by the sum of digits.

Example 1:

Input: S = "AC2BEW3"
Output: "ABCEW5"
Explanation: 2 + 3 = 5 and we print all
alphabets in the lexicographical order.

Example 2:

Input: S = "ACCBA10D2EW30"
Output: "AABCCDEW6"
Explanation: 0+1+2+3 = 6 and we print all
alphabets in the lexicographical order.


Your Task:
You don't need to read input or print anything. Your task is to complete the function arrangeString() which takes the string S as inputs and returns the modified string.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(26)

Constraints:
1 ≤ |S| ≤ 105
S contains only upper case alphabets and digits.
'''
import re
class Solution:
    def arrangeString(self,s):
        temp=re.findall(r'\d',s)
        res=list(map(int,temp))
        # print(res)
        z=''
        for i in s:
            if i.isalpha():
                z+=i
        z1=sorted(z)

        x=str(sum(res))
        z1.append(str(x))
        x1=''.join(z1)
        return x1



if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # s=input()
        # s='AC2BEW3'
        # s='ACCBA10D2EW30'
        s='MJEEAKCOUQWXWSJXBWAGMSDNFQ18W4P1'
        ob=Solution()
        ans=ob.arrangeString(s)
        print(ans)

