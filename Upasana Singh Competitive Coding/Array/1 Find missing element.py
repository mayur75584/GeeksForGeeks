'''
Given an array of size N-1 such that it only contains distinct integers in the
range of 1 to N. Find the missing element.

Input:
N=5
A[]=[1,2,3,5]
Output:4

Input:
N=10
A[]=[6,1,2,8,3,4,7,10,5]
Output:9
'''
'''
Logic

1,2,3,5

Sum of n naturals numbers - sum of numbers in array

Sum of n naturals numbers formula n*(n+1)//2

5*(5+1)//2 - (1+2+3+5)

5*6//2 - (11)

15-11
Ans=4
'''
def MissingNumber(arr,n):
    s=0
    for i in range(n-1):
        s+=arr[i]
    sum1=n*(n+1)//2
    return int(sum1-s)

if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t!=0):
        # n=int(input())
        # arr=[]
        # for i in range(n-1):
        #     arr.append(int(input()))
        # n=5
        # arr=[1,2,3,5]
        n=10
        arr=[6,1,2,8,3,4,7,10,5]
        print(MissingNumber(arr,n))
        t-=1