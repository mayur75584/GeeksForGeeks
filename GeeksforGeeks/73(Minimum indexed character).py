'''
Minimum indexed character

Given a string str and another string patt. Find the character in patt that is present at the minimum index in str.


Example 1:

Input: str = "zsyle", patt = "bjz"
Output: "z"

Example 2:

Input: str = "anskg", patt = "me"
Output: "$"



Your Task:
You don't need to read or print anything. Your task is to complete the function printMinIndexChar() which takes str and patt as input parameter and returns the character in patt that is present at the minimum index in str. If not possible returns "$".


Expected Time Complexity: O(max(|str|, |patt|))
Expected Auxilary Space: O(K) where K <= 26


Constraints:
1 ≤ |str|, |patt| ≤ 104
'''

class Solution:
    def printMinIndexChar(self,str,patt):
        min=10
        z1=''
        flag=False
        for i in range(len(patt)):
            if patt[i] in str:
                if str.index(patt[i])<min:
                    min=str.index(patt[i])
                    z1=patt[i]
                    flag=True
        if flag==True:
            return z1
        else:
            return '$'




if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # str=input().strip()
        # patt=input().strip()
        # str='zsyle'
        # patt='bjz'
        str='anskg'
        patt='me'
        obj=Solution()
        # obj.printMinIndexChar(str,patt)
        print(obj.printMinIndexChar(str,patt))
