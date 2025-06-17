'''
Codevita Round 2
Question - Position

Not running this solution
'''
# import numpy

def change(z):
    res=[]
    for i in z:
        if (i=='a' or i=='d'):
            res.append('a')
            res.append('b')
        elif(i=='c' or i=='b'):
            res.append('c')
            res.append('d')
    return res

def between(n):
    for i in range(0,(n//2)+2):
        if(n<pow(2,i)):
            return i
    return 0

if __name__ == '__main__':
    # print([[0]*1]*6)
    # n=int(input())
    # n=2
    n=7
    # n=17
    # n=265
    if n==1 or n==2:
        print("a")
        exit()
    if n==3:
        print("b")
        exit()
    rows=65
    cols=2000
    size=rows*cols
    # a=numpy.array([""]*size).reshape(rows,cols)
    a=[["."]*cols]*(rows+1)
    a[1][0]="a"
    a[2][0]="a"
    a[2][1]="b"
    print(a)
    print(type(a))
    print(len(a))
    print(a[0])
    print(len(a[0]))
    rNum=between(n)
    for i in range(3,rNum+1):
        x=change(a[i-1])
        print(type(x))
        # print(x)
        print(len(x))
        m=[""]*(cols-len(x))
        print(len(m))
        x.extend(m)
        a[i],x=x,a[i]
    for i in a:
        for j in i:
            print(j,end=' ')
        print()
    print(a[rNum][n-pow(2,rNum-1)])


