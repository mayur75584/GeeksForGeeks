from math import sqrt
# t=int(input())
t=1
for i in range(t):
    # n,k=map(int,input().split(','))
    # n,k=12,3
    # n,k=30,9
    # n,k=90,5
    n,k=10000000000,7
    lst=[]
    'For n=10000000000 k=7 below comment code will give TLE in codevita'
    'But wihtout comment block will not give '
    'Simply for this kind of situation use int(sqrt(n))+1 then it will not give TLE'
    'Below comment block is because for n=100000000000.... it will generate TLE'
    # for i in range(2,n+1):#for n=10000000000000.... this will take TLE
    #     if n%i==0:
    #         lst.append(i)
    # # print(lst)
    # lst.sort(reverse=True)
    # print(lst)
    # # print(len(lst))
    # # print(lst[k-1])
    # if len(lst)<k:
    #     print(1)
    # else:
    #     print(lst[k-1])
    'To avoid this TLE optimatl solution'
    'Below for loop block is best for any condition if we have to run 10000000....... times'
    for j in range(1,int(sqrt(n))+1):
        if n%j==0:
            lst.append(j)
            lst.append(n//j)
    lst.sort()
    print(lst)
    if len(lst)<k:
        print(1)
    else:
        print(lst[-k])
