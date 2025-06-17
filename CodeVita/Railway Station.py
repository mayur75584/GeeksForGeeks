'Note-> Here need greedy Algorithm'
'Greedy Algorithm'
# t=int(input())
t=1
for i in range(t):
    arr=[]
    dept=[]

    n=int(input())
    for i in range(n):
        x,y=map(int,input().split())
        arr.append(x)
        dept.append(x+y)
    arr.sort()
    dept.sort()

    platforms=1
    result=1
    i=1
    j=0

    while i<n and j<n:
        if arr[i]<=dept[j]:
            platforms+=1
            i+=1
        else:
            platforms-=1
            j+=1
    result=max(result,platforms)
    print(result)















'Below solution is mine , but solution is wrong '
# # t=int(input())
# t=1
# for i in range(t):
#     # lst=list(map(int,input().split()))
#     # lst=[3,10,2,5,10,13,5] #Ans 2
#     # lst=[2,2,4,6,2] #Ans 2
#     lst=[5,4,9,14,2,10,5,5,10,3,6] #Ans 3 but giving 1
#     print(lst)
#     n=lst[0]
#     lst.remove(n)
#     print(lst)
#     lst1=[]
#     lst2=[]
#     for j in range(len(lst)):
#         if j%2==0:
#             lst1.append(lst[j])
#         else:
#             lst2.append(lst[j])
#     print(lst1,lst2)
#     count=1
#     z=min(lst1)
#     x=lst1.index(z)
#     y=lst2[x]
#     for k in range(len(lst1)-1):
#
#         lst1.remove(z)
#         lst2.remove(y)
#         l=min(lst1)
#         m=lst1.index(l)
#         n=lst2[m]
#         if z+y>l+n or z+y==l:
#             count+=1
#         z,y=l,n
#     print(count)







