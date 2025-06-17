t=int(input())
for i in range(t):
    S,R=map(int,input().split())
    samples=list(map(int,input().split()))
    result=[]
    for j in range(R):
        r1,r2=map(int,input().split())
        count=0
        for i in samples:
            if i>=r1 and i<=r2:
                count+=1
        result.append(count)
    for i in result:
        print(i,end=" ")


################# Mam's Solution

# s,t=[int(x) for x in input().split()]
# c=0
# result=[]
#
# Samples=[int(x) for x in input().split()]
#
# for i in range(t):
#     r1,r2=[int(x) for x in input().split()]
#     for j in Samples:
#         if((j>=r1) and (j<=r2)):
#             c+=1
#     result.append(c)
#     c=0
#
# for i in result:
#     print(i,end=" ")