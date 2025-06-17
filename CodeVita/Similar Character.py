t=int(input())
# t=1
for i in range(t):
    n=int(input())
    s=input()
    q=int(input())
    result=[]
    # n=9
    # s='abacsddaa'
    # q=2
    for j in range(q):
        p=int(input())
        z1=s[p-1]
        z=s[:p-1]
        result.append(z.count(z1))
    for k in range(len(result)-1):
        print(result[k])
    print(result[-1],end=' ') #Used for in range instead of for in sequence to avoid presentation error

