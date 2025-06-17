'Note-> Read again and solve again'
# t=int(input())
t=1
for i in range(t):
    # n=int(input())
    # a=[]
    # for i in range(3):
    #     b=[]
    #     for j in range(n):
    #         j=input()
    #         b.append(j)
    #     print(b)
    #     a.append(b)
    a=[['*', '.', '*', '#', '*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '.', '*', '.'], ['*', '.', '*', '#', '*', '.', '*', '#', '.', '*', '.', '#', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '*', '.', '*']]
    print(a)
    lst=[]
    lst1=[]
    lst2=[]
    lst3=[]
    for i in a:
        s1=''
        for j in i:
            s1+=j
        x=s1.split('#')
        lst.append(x)
        # lst2.append(y)
        # lst3.append(z)
    print(lst)





