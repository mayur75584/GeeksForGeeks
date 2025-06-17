'''
Element with left side smaller and right side greater

Given an unsorted array of size N. Find the first element in array such that
all of its left elements are smaller and all right elements to it are greater than it.

Note: Left and right side elements can be equal to required element.
And extreme elements cannot be required element.



Example 1:

Input:
N = 4
A[] = {4, 2, 5, 7}
Output:
5
Explanation:
Elements on left of 5 are smaller than 5
and on right of it are greater than 5.



Example 2:

Input:
N = 3
A[] = {11, 9, 12}
Output:
-1



Your Task:
You don't need to read input or print anything.
Your task is to complete the function findElement() which takes the array A[]
and its size N as inputs and returns the required element.
If no such element present in array then return -1.



Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)



Constraints:
3 <= N <= 106
1 <= A[i] <= 106

'''
def findElement(arr,n):
    left=[]
    right=[]
    min1=9999999
    max1=0
    for i in range(len(arr)):
        if i==0:
            left.append(arr[0])
            max1=arr[0]
        else:
            max1=max(max1,arr[i])
            left.append(max1)
    print(left)
    for i in range(len(arr)-1,-1,-1):
        if i==len(arr)-1:
            right.insert(0,arr[i])
            min1=arr[i]
        else:
            min1=min(min1,arr[i])
            right.insert(0,min1)
    print(right)
    for i in range(1,len(arr)-1):
        if(left[i]<=arr[i]<=right[i]):
            return arr[i]
    return -1


# T=int(input())
T=1
while(T>0):
    # n=int(input())
    # a=[int(x) for x in input().split()]
    # n=4
    # a=[4,2,5,7]
    # n=3
    # a=[11,9,12]
    n=5
    a=[10,1,6,21,37]
    print(findElement(a,n))
    T-=1