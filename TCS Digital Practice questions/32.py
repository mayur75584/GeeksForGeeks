'''
Given an array of n integers and a positive integer k.
Cyclically rotate the array clockwise by k.
Keep the first position of array unaltered.

eg
5 (n)
1 2 3 4 5
2 (k)
o/p-
1 4 5 2 3
'''

def func(n,arr,k):
    if len(arr)==1:
        return arr
    else:
        x=[]
        x.append(arr[0])
        z=arr[1:]
        # print(z)
        while(k!=0):
            m=[]
            m.append(z.pop(-1))
            z=m+z
            k-=1
        x.extend(z)
        return x


if __name__ == '__main__':
    # n=int(input())
    # arr=list(map(int,input().split()))
    # k=int(input())
    # n=5
    # arr=[1,2,3,4,5]
    # k=2
    # n=1
    # arr=[10]
    # k=4
    n=2
    arr=[10,20]
    k=2
    res=func(n,arr,k)
    print(*res)
