'''
You are given with a string consisting of lowercase characters only.
The letters can be duplicate or non-duplicate. Duplicate letters have
multiple copies present in the string. where as non-duplicates are unique and occurs
single. Your task is to return the index of first non-duplicating letter
present in the string if we traverse it from left to right.
Use the indexing starting from 1.
If no such letter is present return -1.

Constraints: 1<=length of string<=10^5

i/p: statistics o/p:3
i/p: hackthegame o/p:3
'''

def getUniqueLetter(s):
    res=0
    flag=False
    for i in range(len(s)):
        if s.count(s[i])==1:
            res=i+1
            flag=True
            break
    if flag==True:
        return res
    else:
        return -1



if __name__ == '__main__':
    s=input()
    result=getUniqueLetter(s)
    print(result)