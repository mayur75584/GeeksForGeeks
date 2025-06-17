'''
There is a range given n and m in which we have to find the count all the prime
pairs whose difference is 6.
We have to find how many sets are there within a given range.

Output:
The output consists of a single line, print the count prime pairs in a given range.
Else print "No Prime Pairs".

Constraints:
2<=n<=1000
n<=m<=2000

Sample Input:
4
30
Sample Output:
6
Explanation:
(5,11)(7,13)(11,17)(13,19)(17,23)(23,29)
'''

'Optimized method'
'Sieve Method'

def count_prime(l,r):
    count=0
    prime=[True for i in range(r+1)]
    p=2
    while(p*p<=r+1):
        if(prime[p] == True):
            for i in range(p*p,r+1,p):
                prime[i]=False
        p+=1
    lst=[]
    for i in range(l,(r+1)-6):
        if i==0 or i==1:
            continue
        x=[]
        if prime[i] and prime[i+6]:
            count+=1
            x.append(i)
            x.append(i+6)
            lst.append(tuple(x))
    print(lst)
    if count>0:
        print(count)
    else:
        print("No Prime Pairs")


if __name__ == '__main__':
    # n=int(input())
    # m=int(input())
    n=4
    m=30
    # n=1
    # m=11
    count_prime(n,m)


# def isprime(a):
#     if a>1:
#         for i in range(2,int(a/2)+1):
#             if (a%i)==0:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def prime(n,m):
#     lst=[]
#     for i in range(n,m+1):
#         if isprime(i):
#             lst.append(i)
#     print(lst)
#     z=[]
#     for i in lst:
#         x=[]
#         if (i+6) in lst:
#             x.append(i)
#             x.append(i+6)
#             z.append(tuple(x))
#     print(z)
#     return len(z)
#
#
#
#
#
# if __name__ == '__main__':
#     # n=int(input())
#     # m=int(input())
#     # n=4
#     # m=30
#     n=1
#     m=11
#     result=prime(n,m)
#     if result==0:
#         print("No Prime Pairs")
#     else:
#         print(result)