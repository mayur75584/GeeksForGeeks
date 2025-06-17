
'My logic'
# def func(n,k,a):
#     z=[]
#     z1=[]
#     j=0
#     while len(a)!=0:
#         lst=[]
#         if a[j]==k:
#             lst.append(a[j])
#             z.append(lst)
#             a.pop(j)
#         elif a[j]<k:
#             x=k-a[j]
#             m=a[j+1:]
#             if x in m:
#                 lst.append(a[j])
#                 lst.append(x)
#                 z.append(lst)
#                 f=a.index(x)
#                 a.pop(f)
#                 a.pop(j)
#             else:
#                 z1.append(a[j])
#                 a.pop(j)
#     print(z)
#     print(z1)
#     if len(z1)!=0:
#         z1.sort()
#         l=len(z1)
#         l1=l//2
#         z2,z3=z1[:l1],z1[l1:]
#         print(z2)
#         print(z3)
#         while (len(z2)!=0) and (len(z3)!=0):
#             lst=[]
#             p=z2.index(max(z2))
#             q=z3.index(max(z3))
#             if len(z2)>=1 and len(z3)>=1:
#                 if z2[p]+z3[q]<=k:
#                     lst.append(z2[p])
#                     lst.append(z3[q])
#                     z.append(lst)
#                     z2.pop(p)
#                     z3.pop(q)
#                 elif z2[p]+z3[q-1]<=k:
#                     lst.append(z2[p])
#                     lst.append(z3[q-1])
#                     z.append(lst)
#                     z2.pop(p)
#                     z3.pop(q-1)
#                 elif z2[p-1]+z3[q]<=k:
#                     lst.append(z2[p-1])
#                     lst.append(z3[q])
#                     z.append(lst)
#                     z2.pop(p-1)
#                     z3.pop(q)
#             elif len(z2)==0 and len(z3)!=0:
#                 if len(z3)==1:
#                     lst=z3[0]
#                     z.append(lst)
#                 else:
#                     lst=[]
#                     while(len(z3)!=0):
#                         if max(z3)+min(z3)<=k:
#                             lst.append(max(z3))
#                             lst.append(min(z3))
#                             z3.remove(max(z3))
#                             z3.remove(min(z3))
#                             z.append(lst)
#             elif len(z3)==0 and len(z2)!=0:
#                 if len(z2)==1:
#                     lst=[z2[0]]
#                     z.append(lst)
#                 else:
#                     lst=[]
#                     while(len(z2)!=0):
#                         if max(z2)+min(z2)<=k:
#                             lst.append(max(z2))
#                             lst.append(min(z2))
#                             z2.remove(max(z2))
#                             z2.remove(min(z2))
#                             z.append(lst)
#     print(z)
#     return len(z)
#
# if __name__ == '__main__':
#     # n=int(input())
#     # k=int(input())
#     # a=list(map(int,input().split()))
#     n=7
#     k=12
#     a=[12,2,3,11,6,8,1]
#     # n=5
#     # k=5
#     # a=[5,2,3,1,4]
#     result=func(n,k,a)
#     print(result)

'Mam Logic'
def function2(arr,N,K):
    arr.sort()
    result=0
    i,j=0,N-1

    while(i<=j):
        result+=1
        if arr[i]+arr[j]<=K:
            i+=1
        j-=1
    return result

# N=int(input())
# K=int(input())
# arr=[]
# counter=0
# for i in range(N):
#     arr.append(int(input()))
# N=7
# K=12
# arr=[12,2,3,11,6,8,1]
N=5
K=5
arr=[5,2,3,1,4]
print(function2(arr,N,K))



