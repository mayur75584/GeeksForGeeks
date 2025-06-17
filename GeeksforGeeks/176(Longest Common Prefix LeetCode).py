'''
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
'''
class Solution:
    def longestCommonPrefix(self,strs):
        #["flower","flow","flight"]
        #Sorting["flight","flow","flower"]
        n=len(strs)
        if n==0:
            return ""
        if n==1:
            return strs[0]
        s=sorted(strs)
        first=s[0]
        last=s[-1]
        leng=min(len(first),len(last))
        i=0
        while(i<leng and first[i]==last[i]):
            i+=1
        return first[:i]
if __name__ == '__main__':
    # strs=list(map(str,input().split()))
    strs=["flower","flow","flight"]
    # strs=["dog","racecar","car"]
    ob=Solution()
    ans=ob.longestCommonPrefix(strs)
    print(ans)