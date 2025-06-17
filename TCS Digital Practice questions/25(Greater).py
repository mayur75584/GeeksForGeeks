'''
Given an integer array Arr of size N the task is to find the count of elements
whose value is greater than all its prior elements.

Note: 1st element of the array should be considered in the count of the result.

For example:

Arr[] = {7,4,8,2,9}
As 7 is the first element it will consider in the result.
8 and 9 are also the elemnts that are greater than all of its previous
elements.
Since total of 3 elements is present in the array that meets the condition.
Hence the output = 3.

Example1:
Input:
5-> Value of N,represent size of Arr
7-> Value of Arr[0]
4-> Value of Arr[1]
8-> Value of Arr[2]
2-> Value of Arr[3]
9-> Value of Arr[4]

Output:
3
'''
'''
6
1
4
-1
6
10
2
'''
def greater(N,arr):
    count1=1
    max1=0
    for i in range(N):
        if i==0:
            max1=arr[i]
        else:
            if arr[i]>max1:
                count1+=1
                max1=arr[i]
    print(count1)

if __name__ == '__main__':
    # N=int(input())
    # arr=[]
    # for i in range(N):
    #     arr.append(int(input()))
    # N=5
    # arr=[7,4,8,2,9]
    # N=6
    # arr=[1,4,-1,6,10,2]
    N=5
    arr=[7,8,4,2,9]
    greater(N,arr)


