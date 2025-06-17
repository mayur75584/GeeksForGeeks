'Not able to solve'
def func(n,A):
    # for i in range(len(A)):
    #     for j in range(i+1,len(A)):
    #         if ((A[i]&A[j])*2)<(A[i]|A[j]):
    #
    #             print(((A[i]&A[j])*2),(A[i]|A[j]),A[i],A[j])
    z=len(A)
    for i in range(z+1):
        for j in range(i+1,z+1):
            if (((A[i]&A[j])*2)<(A[i]|A[j]))==True:
                print(A[i],A[j])



if __name__ == '__main__':
    # n=int(input())
    # A=[]
    # for i in range(n):
    #     x=int(input())
    #     A.pop(x)
    n=5
    A=[15,6,5,12,1]
    # n=7
    # A=[17,16,12,2,8,17,17]
    res=func(n,A)
    print(res)