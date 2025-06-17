'Unique Birthday Gift'
'Not completed'
def func(n,k):
    # res=[]
    # if k==1:
    #     for i in range(1,n+1):
    #         res.append([i])
    # else:
    #     pass
    #
    #
    # print(res)
    # return len(res)
    subarray=[]
    if k==1:
        for i in range(1,n+1):
            subarray.append(i)
        return len(subarray)
    else:
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if j%i==0:
                    pass





if __name__ == '__main__':
    # n=int(input())
    # k=int(input())
    n=2
    k=1
    result=func(n,k)
    print(result)