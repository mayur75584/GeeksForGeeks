# t=int(input())
t=1
for i in range(t):
    P=int(input())
    T=int(input())
    # P=10000
    # T=20
    bank=[]
    for j in range(2):
        n=int(input())
        # n=3
        sum1=0
        for k in range(n):
            yrs,slab=map(float,input().split())
            yrs=int(yrs)
            x=(1+slab)**(yrs*12)
            y=1-(1/x)
            z=P*slab
            z1=z/y
            sum1+=z1
        bank.append(sum1)
    # print(bank[0],bank[1])
    if bank[0]<bank[1]:
        # print(bank[0])
        print("Bank A",end=" ")
    else:
        # print(bank[1])
        print("Bank B",end=" ")

