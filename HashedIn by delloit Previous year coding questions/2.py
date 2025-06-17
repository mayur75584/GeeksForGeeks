'''
Given 2 Strings str and word, you have to find how many words can you make from that given string.
Input : str="This is a test string" word="tsit"
Output : 2
Explanation : there are 4 t's 4 s's 3 i's in the given str, by which you can only make 2 "tsit".
Input: str="Here is HashedIn Technologies" word="neurons"
Output : 0
Explanation: since you do not have 'u' in str. thus u can't form word "neurons".
'''
'Note-> Dont know whether the solution is completely correct or not.'
def func(s,word):
    dict1={}
    s=s.lower()
    word=word.lower()
    for i in s:
        if i in word:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
    print(dict1)
    count1=0
    i=0
    while(True):
        if(word[i] not in dict1):
            break
        if(dict1[word[i]]==0):
            break
        dict1[word[i]]-=1
        i+=1
        if i==len(word):
            count1+=1
            i=0
    return count1

if __name__ == '__main__':
    # s=input()
    # word=input()
    s='This is a test string'
    word='tsit'
    # s='Here is HashedIn Technologies'
    # word='neurons'
    res=func(s,word)
    print(res)