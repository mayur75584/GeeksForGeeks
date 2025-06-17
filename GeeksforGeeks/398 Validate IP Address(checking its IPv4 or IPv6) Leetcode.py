'''
468. Validate IP Address
Solved
Medium
Topics
Companies
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.



Example 1:

Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.


Constraints:

queryIP consists only of English letters, digits and the characters '.' and ':'.

'''

'These question has come in my Turing Company assessment which I was not able to solve.'

class Solution:
    def validIPAddress(self,queryIP):
        alpha1=['a','b','c','d','e','f','A','B','C','D','E','F']
        flag1,flag2=True,True

        if '.' in queryIP:
            x=queryIP.split('.')
            if queryIP.count('.')==3:
                for i in x:
                    if i.isnumeric():
                        if ((int(i)>=0 and int(i)<=255)):
                            if len(i)>1 and i[0]!='0':
                                pass
                            elif len(i)==1 and i[0].isnumeric():
                                continue
                            else:
                                flag1=False
                                break
                        else:
                            flag1=False
                            break
                    else:
                        flag1=False
                        break
                else:
                    flag1=True
                    flag2=False
            else:
                flag1=False
                flag2=False
        else:
            flag1=False

        if ':' in queryIP:
            y=queryIP.split(':')
            if queryIP.count(':')==7:
                for i in y:
                    if i.isalnum()  and len(i)<=4:
                        for j in i:
                            if j.isalpha():
                                if j not in alpha1:
                                    flag2=False
                                    break
                                else:
                                    continue
                            else:
                                continue
                    else:
                        flag2=False
                        break
                    if flag2==False:
                        break

                else:
                    flag2=True
                    flag1=False
            else:
                flag2=False
                flag1=False
        else:
            flag2=False

        if flag1==True and flag2==False:
            return "IPv4"
        if flag1==False and flag2==True:
            return "IPv6"
        if flag1==False and flag2==False:
            return "Neither"

if __name__ == '__main__':
    queryIP="172.16.254.1"
    # queryIP="2001:0db8:85a3:0:0:8A2E:0370:7334"
    # queryIP="256.256.256.256"
    # queryIP="2001:0db8:85a3:0:0:8A2E:0370:7334:"
    # queryIP="12.12.12.12.12"
    # queryIP="20EE:FGb8:85a3:0:0:8A2E:0370:7334"
    # queryIP="192.0.0.1"
    # queryIP=input()
    ans=Solution().validIPAddress(queryIP)
    print(ans)



