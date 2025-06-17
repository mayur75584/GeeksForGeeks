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
# t=int(input())
t=1
for i in range(t):
    # p=input()
    # s=input()
    # p='polikujmnhytgbvfredcxswqaz'
    # s='abcdd'
    # p='qwryupcsfoghjkldezvxbintma'
    # s='ativedoc'
    # p='qwryupcsfoghjkldezvxbintma'
    # s='ativedoca'
    lst=[]
    for j in s:
        lst.append(p.index(j))
    lst.sort()
    for k in lst:
        print(p[k],end=" ")
    print()

