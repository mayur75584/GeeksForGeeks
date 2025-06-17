


n=int(input())
r=int(input())
arr=[]
for i in str(n):
    arr.append(int(i))
z=0
for i in range(r):
    z+=sum(arr)
z1=0
for i in str(z):
    z1+=int(i)
print(z1)

'Prepinsta solution'

# s=input()
#
# n=int(input())
#
# sum=0
#
# for i in s:
#
#     sum+=int(i)
#
# sum*=n
#
# s=str(sum)
#
# while len(s)>1:
#
#     sum=0
#
#     for i in s:
#
#         sum+=int(i)
#
#     s=str(sum)
#
# print(s)