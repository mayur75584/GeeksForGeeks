'Note-> Not understood solution'

def checkPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
        return True

# t=int(input())
t=1
for i in range(t):
    # d,p=map(int,input().split())
    d,p=36,3
    h=d//p
    n=h
    res=0

    while n>1:
        i=0
        cnt=0
        while True:
            k=(i*h)+n

            if checkPrime(int(k)) and k<=d:
                cnt=cnt+1

            if i==(p-1):
                break
            i+=1

        if cnt==p:
            res+=1
        n-=1
    print(res,end=" ")


