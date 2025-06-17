
'Dynamic Programming'
t=int(input())
for i in range(t):
    n=int(input())
    ways=[]
    ways=[0]*(n+1)
    ways[0]=1
    ways[1]=1
    ways[2]=2

    for i in range(3,n+1):
        ways[i]=ways[i-3]+ways[i-2]+ways[i-1]
    print(ways[n])

'Recursion'

# def Find_Ways(n):
#     if (n==1 or n==0):
#         return 1
#     elif(n==2):
#         return 2
#     else:
#         return Find_Ways(n-3)+Find_Ways(n-2)+Find_Ways(n-1)
#
# t=int(input())
# for i in range(t):
#     n=int(input())
#     print(Find_Ways(n))