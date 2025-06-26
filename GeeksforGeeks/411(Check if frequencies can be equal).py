'''
Check if frequencies can be equal

Given a string s consisting only lowercase alphabetic characters, check whether it is possible to remove
at most one character such that the  frequency of each distinct character in the string becomes same.
Return true if it is possible; otherwise, return false.

Examples:

Input: s = "xyyz"
Output: true
Explanation: Removing one 'y' will make frequency of each distinct character to be 1.
Input: s = "xyyzz"
Output: true
Explanation: Removing one 'x' will make frequency of each distinct character to be 2.
Input: s = "xxxxyyzz"
Output: false
Explanation: Frequency can not be made same by removing at most one character.
Constraints:
1 ≤ s.size() ≤ 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
'''
class Solution:
    def sameFreq(self,s):
        dict1={}
        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        print(dict1)
        dict1=dict(sorted(dict1.items(),key=lambda x:x[0]))
        dict2={}
        for i,j in dict1.items():
            if j not in dict2:
                dict2[j]=1
            else:
                dict2[j]+=1

        print(dict2)
        max1=0
        key1=0

        for i,j in dict2.items():
            if j>max1:
                max1=j
                key1=i
        print(max1,key1)

        for i,j in dict1.items():
            if j!=key1:
                dict1[i]-=1
                break
        print(dict1)
        dict_final={}
        for i,j in dict1.items():
            if j!=0:
                dict_final[i]=j
        print(dict_final)

        val=list(set(dict_final.values()))
        print(val)

        if len(val)==1:
            return True
        else:
            return False

if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # s=input()
        # s="xyyz"
        # s="xyyzz"
        # s="xxxxyyzz"
        # s="deedaadc"
        s="babaaaabbbabbbbbbbbaabababbbbabaababbabbbbaabbababbaabbbbaaabaabbabababbaabbbaaaabbaaaabaaaaababababbaababbbaaababbbaababbaaaabbbbbbbaaaabbabbaaaabaabababaababbaaaaaabababbbbaabababbabbaaababbababbaaabaaababaaaaaaabbaabaaababbababbabaabbaabbbbbabbabababbbababbabababbbbababbabbabbaaabbbaabaaaabaaabaaaaaaaabbbaaabbbbbabbabababaabbbabaaaabbaaababbabbbaaababaaaaababaabaababaaabbbabbbbabbbabaababaaaabbaaabbabbabbbabaaaaabaabaabbbaaabababbbababbababbbabbaabbbbbbaabaaaaaaabababbbabaaaabbbabbbbabbbbbbaaabbaaabaabbbbaaaababaabbbbbbaabaababaabbbabbbabbabaabaabbbaaababbaaabaabbbbaaabbbbbbbaababbababaaabbabbaaaaabbbaabababbaaababbaabbababbbbbaabbbbbbabbbaaaabababaabbbbabbaabbbbaabbabbababaabaaabaaaaaaabbbabbbababbaaababaaaabaaaaababbabaaaaabbbbaabbababbaabaabbabbabbaaabbaabbaabbaababaabaabbaabaabbabaabbbaaabaabababbbbaaabbababbabbaabbabbbbaaaaaabaabbbaaabababbaaaabaaabbbbaaababababbaabbbbbbbaaabbbabbaabbbbbbbbbababbaabbaababaababababbabaaabaaabbaabbbabbaabaaaaaabbabaaabbababaaaaaaabaabaaaabbaaabbabbbbabaababbbabbbabbbaaabaabbbaababbaaabaababbbbababaabbabbaabbbbbaaaabbbabaababaaa"
        obj=Solution()
        ans=obj.sameFreq(s)
        if ans==True:
            print("true")
        else:
            print("false")
        t-=1