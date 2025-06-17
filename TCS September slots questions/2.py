
'Split numbers'
def pow(x,a):
    res=1
    while(a):
        if(a&1):
            res=res*x
        x=x*x
        a>>=1
    return res

def breakInteger(N):

    if(N==2):
        return 1
    if(N==3):
        return 2
    maxProduct=0

    if (N%3==0):
        maxProduct=pow(3,int(N/3))
        return maxProduct
    elif (N%3==1):
        maxProduct=2*2*pow(3,int(N/3)-1)
        return maxProduct
    elif (N%3==2):
        maxProduct=2*pow(3,int(N/3))
        return maxProduct

n=int(input())
maxProduct=breakInteger(n)
print(maxProduct)



