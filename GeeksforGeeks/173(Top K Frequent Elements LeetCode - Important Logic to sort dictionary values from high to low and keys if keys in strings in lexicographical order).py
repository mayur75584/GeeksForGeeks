'''
Top K Frequent Words

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.



Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.



Constraints:

    1 <= words.length <= 500
    1 <= words[i] <= 10
    words[i] consists of lowercase English letters.
    k is in the range [1, The number of unique words[i]]

'''

class Solution:
    def topKFrequent(self,words,k):
        dict1={}
        for i in words:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        print(dict1)
        #Syntax to sort dictionary values from highest and keys(string type keys) in lexicographical order
        x=sorted(sorted(dict1),key=dict1.get,reverse=True)
        print(x)
        return x[:k]

if __name__ == '__main__':
    # words=list(map(str,input().split()))
    # words=["i","love","leetcode","i","love","coding"]
    # k=2
    # words=["the","day","is","sunny","the","the","the","sunny","is","is"]
    # k=4
    words=["i","love","leetcode","i","love","coding"]
    k=3
    ob=Solution()
    print(ob.topKFrequent(words,k))
