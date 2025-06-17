
'''
Given an array Arr[] of N integers and a positive integer K.
The tasks to cyclically rotate the array clockwise by K.
Note: Keep the first position of array unaltered.

Example1:
Input:
N-5
{10,20,30,40,50}-Elements of Arr[]
K-2
Output:
10 40 50 20 30

Example2:
Input:
4
{10,20,30,40}
1
Output:
10 40 20 30

Example3:
3
{10,20,30}
4
Output:
10 20 30

Explanation:
Example1:
Arr[]={10,20,30,40,50} and K=2(Two cyclical rotations)
After 1st rotation={10,50,20,30,40}
After 2nd rotation={10,40,50,20,30}

Constraints:
1<=N<=100
100<=Arr[i]<=100
1<=K<=100
'''



def func(n,arr,k):
    if len(arr)==1:
        return arr
    else:
        z=[]
        x=arr.pop(0)
        # print(arr)
        z.append(x)
        for i in range(k):
            m=[]
            z1=arr.pop()
            m.append(z1)
            arr=m+arr
        x1=z+arr
        return x1

if __name__ == '__main__':
    # n=int(input())
    # arr=list(map(int,input().split()))
    # k=int(input())
    # n=5
    # arr=[10,20,30,40,50]
    # k=2
    # n=4
    # arr=[10,20,30,40]
    # k=1
    n=3
    arr=[10,20,30]
    k=4
    result=func(n,arr,k)
    for i in result:
        print(i,end=' ')