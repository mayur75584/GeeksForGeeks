'''


Input1:
P=[8,10]
T=[3,1,8,7,4,2,5,2]
Output1:
16

Input2:
P=[5,11]
T=[3,1,8,7,4,2,5,2]
Output2:
14

'''

def processorTime(P,T):
    res=[]
    z=sorted(T)
    count1=0
    y=sorted(P)
    j=0
    for i in range(len(z)-1,-1,-1):
        if count1==4:
            count1=0
            j+=1

        count1+=1
        res.append(y[j]+z[i])
    print(res)
    return max(res)


if __name__ == '__main__':
    # P=list(map(int,input().split()))
    # T=list(map(int,input().split()))
    P=[5,11]
    T=[3,1,8,7,4,2,5,2]
    # P=[8,10]
    # T=[3,1,8,7,4,2,5,2]
    result=processorTime(P,T)
    print(result)