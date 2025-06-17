'''
Remove leading zeros from an IP address

Given an IP address, remove leading zeros from the IP address. Note that our IP address here can be a little different. It can have numbers greater than 255. Also, it does not necessarily have 4 numbers. The count can be lesser/more.

Example 1:

Input:
S = "100.020.003.400"
Output: 100.20.3.400
Explanation: The leading zeros are removed
from 20 and 3.

â€‹Example 2:

Input:
S = "100.000.010.0999"
Output: 100.0.10.999
Explanation: The leading zeros are removed
from 0, 10 and 999.


Your Task:
You don't need to read input or print anything. Your task is to complete the function newIPAdd() which takes the string S representing the IP address as input and returns a string representing the resultant IP address.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).


Constraints:
1<=|S|<=1000
'''
class Solution:
    def newIPAdd(self,S):
        x=S.split('.')
        s1=''
        for i in x:
            s1=s1+str(int(i))+'.'
        return s1[0:-1]



if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        s=input().strip()
        ob=Solution()
        ans=ob.newIPAdd(s)
        print(ans)

