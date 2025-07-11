
'''
First and last occurrences of x

Given a sorted array arr containing n elements with possibly duplicate elements,
the task is to find indexes of first and last occurrences of an element x
in the given array.

Example 1:
Input:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  2 5
Explanation: First occurrence of 5 is at index 2 and last
             occurrence of 5 is at index 5.

Example 2:

Input:
n=9, x=7
arr[] = { 1, 3, 5, 5, 5, 5, 7, 123, 125 }
Output:  6 6

Your Task:
Since, this is a function problem.
You don't need to take any input, as it is already accomplished by the driver code.
You just need to complete the function find() that takes array arr,
integer n and integer x as parameters and returns the required answer.
Note: If the number x is not found in the array just return both index as -1.



Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1).



Constraints:
1 ≤ N ≤ 107
'''

def first(arr,n,x):
    low=0
    high=n-1
    res=-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>x):
            high=mid-1
        elif(arr[mid]<x):
            low=mid+1
        else:
            res=mid
            high=mid-1
    return res
def last(arr,n,x):
    low=0
    high=n-1
    res=-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>x):
            high=mid-1
        elif(arr[mid]<x):
            low=mid+1
        else:
            res=mid
            low=mid+1
    return res

def find(arr,n,x):
    # code here
    res=[]
    a1=first(arr,n,x)
    a2=last(arr,n,x)
    res.append(a1)
    res.append(a2)
    return res


t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    ans=find(arr,x)
    print(*ans)