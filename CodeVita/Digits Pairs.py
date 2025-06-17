'Not complete solution, one condition is remaining'
# t=int(input())
t=1
for i in range(t):
    # n=int(input())
    # lst=list(map(int,input().split()))
    n=8
    lst=[234,567,321,345,123,110,767,111]
    lst1=[]
    for j in lst:
        max1=int(max(str(j)))
        min1=int(min(str(j)))
        z=max1*11+min1*7
        if len(str(z))>2:
            z1=str(z)
            x=z1[-2:]
            lst1.append(int(x))
        else:
            lst1.append(int(z))
    print(lst1)
    even=[]
    odd=[]
    for i in range(len(lst1)):
        if i%2==0:
            even.append(lst1[i])
        else:
            odd.append(lst1[i])
    print(even,odd)
    dict={}
    count=0
    for i in range(len(even)):
        for j in range(i+1,len(even)):
            x=str(even[i])
            x1=x[0]
            y=str(even[j])
            y1=y[0]
            if x1==y1:
                count+=1
                dict[x1]=x1
    for i in range(len(odd)):
        for j in range(i+1,len(odd)):
            x=str(odd[i])
            x1=x[0]
            y=str(odd[j])
            y1=y[0]
            if x1==y1:
                count+=1
                dict[x1]=x1
    print(count)
    print(dict)


