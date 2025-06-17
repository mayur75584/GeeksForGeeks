
t=int(input())
lst=[]
for i in range(t):
    N=int(input())
    for j in range(1,int(N**0.5)+1): #Because Here comes TLE we have used loop upto square root of number
        if N%j==0:
            if j*j==N: #here if case is 16 ans will be 1 2 4 4 8 16 so to avoid double 4 in asnwer here we used this condition
                print(j,end=" ")
            else:
                print(j,end=" ")
                lst.insert(0,N//j)
    # lst=list(set())
    for i in lst:
        print(i,end=" ")
    lst=[]
