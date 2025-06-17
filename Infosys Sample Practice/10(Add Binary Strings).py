'''
Add Binary Strings

Given two binary strings A and B consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.


Example 1:

Input:
A = "1101", B = "111"
Output: 10100
Explanation:
 1101
+ 111
10100

Example 2:

Input:
A = "10", B = "01"
Output: 11
Explanation:
  10
+ 01
  11


Your Task:
You don't need to read input or print anything. Your task is to complete the function addBinary() which takes 2 binary string A and B and returns a binary string denoting the addition of both the strings.


Expected Time Complexity: O(max(|A|, |B|)).
Expected Auxiliary Space: O(max(|A|, |B|)) (for output string).


Constraints:
1 ≤ |A|, |B| ≤ 106
'''
class Solution:
    def addBinary(self,a,b):
        count1=0
        if len(a)<len(b):
            x=len(b)-len(a)
            a=x*'0'+a
            print(a)
        else:
            x=len(a)-len(b)
            b=x*'0'+b
            print(b)
        a1=a[::-1]
        b1=b[::-1]
        i=0
        sum1=''
        while(i!=len(a)):
            # if count1==1:
            if a1[i]=='1' and b1[i]=='1' and count1==0:
                sum1+='0'
                count1=1
                i+=1
            elif a1[i]=='1' and b1[i]=='1' and count1==1:
                sum1+='1'
                count1=1
                i+=1
            elif a1[i]=='0' and b1[i]=='0' and count1==1:
                sum1+='1'
                count1=0
                i+=1
            elif a1[i]=='0' and b1[i]=='0' and count1==0:
                sum1+='0'
                i+=1
            elif a1[i]=='1' and b1[i]=='0' and count1==0:
                sum1+='1'
                i+=1
            elif a1[i]=='1' and b1[i]=='0' and count1==1:
                sum1+='0'
                count1=1
                i+=1
            elif a1[i]=='0' and b1[i]=='1' and count1==0:
                sum1+='1'
                i+=1
            elif a1[i]=='0' and b1[i]=='1' and count1==1:
                sum1+='0'
                count1=1
                i+=1
        sum2=str(count1)+sum1[::-1]
        m=sum2.index('1')
        return sum2[m:]





if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # a,b=map(str,input().split(" "))
        a,b='1101','111'
        # a,b='10','01'
        ob=Solution()
        answer=ob.addBinary(a,b)
        print(answer)
