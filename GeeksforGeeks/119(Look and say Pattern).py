'''
Look and Say Pattern
Given an integer n. Return the nth row of the following look-and-say pattern.
1
11
21
1211
111221


Example 1:

Input:
n = 5
Output: 111221
Explanation: The 5th row of the given pattern
will be 111221.

Example 2:

Input:
n = 3
Output: 21
Explanation: The 3rd row of the given pattern
will be 21.


Your Task:
You dont need to read input or print anything. Complete the function lookandsay() which takes integer n as input parameter and returns a string denoting the contents of the nth row of given pattern.


Expected Time Complexity: O(2n)
Expected Auxiliary Space: O(2n-1)


Constraints:
1 ≤ n ≤ 30
'''


def again(s):
    result=[]
    i=0
    while i<len(s):
        count=1
        while i+1<len(s) and s[i]==s[i+1]:
            i+=1
            count+=1
        result.append(str(count)+s[i])
        i+=1
    return ''.join(result)


class Solution:
    def lookandsay(self,n):
        if n==1:
            return 1
        elif n==2:
            return 11
        else:
            s='1'
            lst=[]
            for i in range(2,n+1):
                s=again(s)
                lst.append(s)
            return lst[-1]





if __name__ == '__main__':
    # t=int(input())
    t=1

    for _ in range(t):
        # n=int(input())
        n=5
        solObj=Solution()
        print(solObj.lookandsay(n))