'''
Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this list to find the smallest lexicographical string that can be made out of this new order. Can you help him?

You are given a string P that denotes the new order of the letters in the English dictionary.

You need to print the smallest lexicographic string made from the given string S.

Constraints
1 <= T <= 1000
Length(P) = 26
1 <= length(S) <= 100
All character in the string S, P are in lower case

Input Format
The first line contains number of test cases T
The second line has the string P
The third line has the string S

Output Format
Print single string in a new line for every test case giving the result

Example:

Input
2
polikujmnhytgbvfredcxswqaz
abcd
qwryupcsfoghjkldezvxbintma
ativedoc

Output
bdca
codevita
'''
'Below Function Code is incorrect for some test cases'
# def LexiString(P,S):
#     dict={}
#     for i in S:
#         dict[i]=P.index(i)
#     print(dict)
#     z=sorted(dict.items(),key=lambda x:x[1])
#     print(z)
#     s1=''
#     for i in z:
#         s1+=i[0]
#     return s1
'Below function code is correct solution for all test cases'
def LexiString(P,S):
    z=[]
    for i in S:
        z.append(P.index(i))
    z.sort()
    s1=''
    for i in z:
        s1+=P[i]
    return s1


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # P=input().lower()
        # S=input().lower()
        # P='polikujmnhytgbvfredcxswqaz'
        # S='abcd'
        # P='qwryupcsfoghjkldezxvbintma'
        # S='ativedoc'
        P='qwryupcsfoghjkldezxvbintma'
        S='ativedoca'
        result=LexiString(P,S)
        print(result)