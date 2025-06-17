'''


You will be given a string S of siz N you have to perform a
particular type Query multiple times on this string.

The Query is--> for any string T, find the length of a lexicographically
smallest suffix of S start with T if there is no suffix return 0.

After Performing all the queries you have to return the sum of all Queries.
Since the answer can be very large return it module 10^9+7

Input format
S String
Q Query in array form

13
1
mzadpoghyykht
yk
o/p- 4

12
2
ktmrgjswhwxu
z
w
o/p-5

15
1
tvtrpudosnlydgi
do
o/p-9

'''
def suff(n,s,query,q):
    sum1=0
    for i in query:
        if i in s:
            z=s.index(i)
            if z==-1:
                sum1+=0
            else:
                sum1+=len(s[z:])
    return (sum1%((10**9)+7))



if __name__ == '__main__':
    # n=int(input())
    # query=[]
    # q=int(input())
    # s=input()
    # for i in range(q):
    #     query.append(input())
    # n=12
    # q=2
    # s='ktmrgjswhwxu'
    # query=['z','w']
    # n=13
    # q=1
    # s='mzadpoghyykht'
    # query=['yk']
    n=15
    q=1
    s='tvtrpudosnlydgi'
    query=['do']
    result=suff(n,s,query,q)
    print(result)