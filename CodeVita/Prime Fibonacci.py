# num1=23
# num2=3719
# sum=0
# for i in range(3,34+1):
#     sum=num1+num2
#     print(sum)
#     num1=num2
#     num2=sum
######################################################################

def fibo(num1,num2,m):
    sum=0
    for i in range(3,m+1):
        sum=num1+num2
        num1=num2
        num2=sum
    return sum

t=int(input())
# t=1
for i in range(t):
    n1,n2=map(int,input().split())
    # n1=2
    # n2=40
    lst=[]
    lst1=[]
    lst2=[]
    for i in range(n1,n2+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            lst.append(i)
    # print(lst)
    z=lst
    # print(z)
    for i in z:
        x=lst.index(i)
        lst.remove(i)
        for j in lst:
            lst1.append(str(i)+str(j))

        lst.insert(x,i)
    z1=list(set(lst))
    # print(lst1)
    # print(len(lst1))
    for i in lst1:
        for j in range(2,(int(i)//2)+1):
            if int(i)%j==0:
                break
        else:
            if int(i) not in lst2:
                lst2.append(int(i))
    # print(lst2)
    # print(len(lst2))
    m=len(lst2)
    num1=min(lst2)
    num2=max(lst2)
    # print(num1,num2)
    y=fibo(num1,num2,m)
    print(y,end=" ") #Here end because by default it gives next line
    #and in codevita it gives then presentation error so to resolve that problem
    #here we give end=" " after final answer




######Mam's solution
# def prime(n):
#     flag=0
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             flag=1
#             break
#     return flag
#
# n,m=input().split()
# n=int(n)
# m=int(m)
# # n,m=2,40
# Prime1=[]
#
# for i in range(n,m+1):
#     if prime(i)==0:
#         Prime1.append(i)
# # print(Prime1)
# # print(len(Prime1))
# Prime2=[]
# for i in Prime1:
#     for j in Prime1:
#         cross_prod = int(str(i)+str(j))
#         if prime(cross_prod)==0 and cross_prod not in Prime2:
#             Prime2.append(cross_prod)
# # print(Prime2)
# # print(len(Prime2))
# num1=min(Prime2)
# num2=max(Prime2)
# sum=0
# for i in range(len(Prime2)-2):
#     sum=num1+num2
#     num1=num2
#     num2=sum
#
# print(sum,end=" ")


