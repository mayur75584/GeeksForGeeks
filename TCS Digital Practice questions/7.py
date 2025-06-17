'''
Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.
Examples :


Input:
Matrix:
 1  2  3
 4  5  6
 7  8  9
Output:
 3  6  9
 2  5  8
 1  4  7
The given matrix is rotated by 90 degree
in anti-clockwise direction.

Input:
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16
Output:
 4  8 12 16
 3  7 11 15
 2  6 10 14
 1  5  9 13
The given matrix is rotated by 90 degree
in anti-clockwise direction.
'''

def func(arr):
    n=len(arr)-1
    arr1=[]
    arr2=[]
    count=0
    # for i in arr:
    #     arr1.append(reversed(i))
    for i in range(len(arr)):
        z=[]
        for j in arr:
            z.append(j[n])
            count+=1
        arr2.append(z)
        if count==len(arr):
            count=0
            n-=1
    # print(arr2)
    return arr2



if __name__ == '__main__':
    # n=int(input())
    # arr=[]
    # for i in range(n):
    #     z=[]
    #     for j in range(n):
    #         k=int(input())
    #         z.append(k)
    #     arr.append(z)
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append([int(j) for j in input().split()])
    print(arr)


    # n=3
    # arr=[[1,2,3],[4,5,6],[7,8,9]]
    result=func(arr)
    for k in result:
        print(*k)

