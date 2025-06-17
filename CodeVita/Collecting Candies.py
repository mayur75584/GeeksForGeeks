t=int(input())
# t=1
res=[]#To avoid presentation error take list outside and add answer in it and after that print it
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    # n=4
    # lst=[1,2,3,4]
    # n=5
    # lst=[1,2,3,4,5]
    lst1=[]
    lst.sort()
    while(len(lst)!=0):
        z=lst[0]+lst[1]
        lst1.append(z)
        lst.remove(lst[1])
        lst.remove(lst[0])
        lst.append(z)
        lst.sort()
        if len(lst)==1:
            break
    '''Here printing answer will give presentation error in codevita
      so add answer in list which is taken outside for loop of testcases i.e res[]
      and append answer in that and after completion of main for loop
      print ans in res list , this removes presentation error as taking input and
      and printing output in same for loop gives you presentation error in codevita'''
    res.append(sum(lst1))
for i in res:
    print(i)

#####Mam's solution
#
# T=int(input())
# res=[]
# for i in range(0,T):
#     arr=[]
#     N=int(input())
#
#     candy=[int(x) for x in input().split()]
#     candy.sort()
#
#     while(len(candy)>=2):
#         candy.sort()
#         sum1=candy[0]+candy[1]
#         arr.append(sum1)
#         candy.pop(0)
#         candy.pop(0)
#         candy.append(arr[-1])
#     res.append(sum(arr))
# for r in res:
#     print(r)

