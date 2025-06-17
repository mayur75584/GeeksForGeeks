#Method1


t=int(input())
for i in range(1,t+1):
    n=int(input())
    count=0
    while(n>0):
        n=n//2
        count+=1
    print(count)

#Method2
# t=int(input())
# # t=1
# for i in range(1,t+1):
#     n=int(input())
#     # n=10
#     z=str(bin(n))
#     # print(z)
#     k=z.replace('0b','')
#     print(len(k))
    