'''
Write a program to print all the combinations of the given word
with or without meaning(when unique characters are given).

Sample Input:
abc
Sample Output:
abc
acb
bac
bca
cba
cab
'''

def permute(a,l,r):
    a=list(a)
    if l==r:
        print(''.join(a))
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i]=a[i],a[l]



if __name__ == '__main__':
    # s=input()
    # s='ABC'
    s='ABCD'
    n=len(s)
    permute(s,0,n-1)


