'''
Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
'''
class Solution:
    def groupAnagrams(self,strs):
        dict1={}
        for i in strs:
            x=''.join(sorted(i))
            if x not in dict1:
                dict1[x]=[i]
            else:
                m=dict1.get(x)
                m.append(i)
        print(dict1)
        val=list(dict1.values())
        return val
if __name__ == '__main__':
    # strs=list(map(int,input().split()))
    # strs=["eat","tea","tan","ate","nat","bat"]
    # strs=[""]
    strs=["a"]
    ob=Solution()
    print(ob.groupAnagrams(strs))