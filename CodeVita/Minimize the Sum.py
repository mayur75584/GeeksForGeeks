
# t=int(input())
t=1
for i in range(t):
    # n,k=map(int,input().split())
    # lst=list(map(int,input().split()))
    n,k=4,3
    lst=[20,7,5,4]
    for j in range(k):
        x=max(lst)
        x1=x//2
        lst.remove(x)
        lst.append(x1)
    print(sum(lst),end=" ")
