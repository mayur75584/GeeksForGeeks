'''
Print Anagrams Together

Given an array of strings, return all groups of strings that are anagrams.
The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.

Note: The finial output will be in lexicographic order.


Example 1:

Input:
N = 5
words[] = {act,god,cat,dog,tac}
Output:
act cat tac
god dog
Explanation:
There are 2 groups of
anagrams "god", "dog" make group 1.
"act", "cat", "tac" make group 2.

Example 2:

Input:
N = 3
words[] = {no,on,is}
Output:
no on
is
Explanation:
There are 2 groups of
anagrams "no", "on" make group 1.
"is" makes group 2.


Your Task:
The task is to complete the function Anagrams() that takes a list of strings as input and
returns a list of groups such that each group consists of all the strings that are anagrams.


Expected Time Complexity: O(N*|S|*log|S|), where |S| is the length of the strings.
Expected Auxiliary Space: O(N*|S|), where |S| is the length of the strings.


Constraints:
1<=N<=100

1<=|S|<=10
'''

class Solution:
    def Anagrams(self,words,n):
        dict1={}
        for i in words:
            x=''.join(sorted(i))
            if x not in dict1:
                dict1[x]=[i]
            else:
                m=dict1.get(x)
                m.append(i)
        print(dict1)
        lst=list(dict1.values())
        return lst


if __name__ == '__main__':
    # t=int(input())
    t=1
    for tcs in range(t):
        # n=int(input())
        # words=list(map(str,input().split()))
        n=5
        words=["act","god","cat","dog","tac"]

        ob=Solution()
        ans=ob.Anagrams(words,n)

        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()