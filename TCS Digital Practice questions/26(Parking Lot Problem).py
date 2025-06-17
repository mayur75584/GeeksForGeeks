'''
A parking lot in a mall has R*C numbers of parking spaces. Each parking
space will either be empty(0) or full(1). The status (0/1) of a
parking space is represented as the element of the matrix. The task is to find
index of the row(R) in the parking lot that has the most of the parking spaces full(1).

Note:

R*C - Size of the matrix
Elements of the matrix M should be only 0 or 1.

Example1:

Input:
3-> Value of R(row)
3-> value of C(column)
[0,1,0,1,1,0,1,1,1]-> Elements of the array M[R][C] where each element
is separated by new line.

Output:
3-> Row 3 has maximum number of 1's.
'''

def parkingLot(R,C,arr):
    max1=0
    z=0
    for i in range(len(arr)):
        x=arr[i]
        if x.count(1)>max1:
            max1=x.count(1)
            z=i
    print(z+1)


if __name__ == '__main__':
    R=int(input())
    C=int(input())
    arr=[]
    for i in range(R):
        z=list(map(int,input().split()))
        arr.append(z)
    parkingLot(R,C,arr)