'''
Find Pair Given Difference

Given an array arr[] of size n and an integer x, return 1 if there exists a pair of elements in the array whose absolute difference is x, otherwise, return -1.

Example 1:

Input:
n = 6
x = 78
arr[] = {5, 20, 3, 2, 5, 80}
Output:
1
Explanation:
Pair (2, 80) have absolute difference of 78.
Example 2:

Input:
n = 5
x = 45
arr[] = {90, 70, 20, 80, 50}
Output:
-1
Explanation:
There is no pair with absolute difference of 45.
Your Task:
You need not take input or print anything.
Your task is to complete the function findPair() which takes integers n, x, and an array arr[] as input parameters and returns 1 if the required pair exists, return -1 otherwise.

Expected Time Complexity: O(n* Log(n)).
Expected Auxiliary Space: O(1).

Constraints:
1<=n<=106
1<=arr[i]<=106
0<=x<=105
'''

'''
Using two pointer and binary search algorithm,

First sort the array. Then use 2 variables i and j.
Assign i=0 and j=1.

Iterate (Use Linear Loop) using condition i<size_of_array and j<size_of_array

If the sort_array[j]-sort_array[i]<difference then increase j by 1.
If the sort_array[j]-sort_array[i]>difference then increase i by 1.

'''
from typing import List

class Solution:
    def findPair(self,n,x,arr):
        arr_sort = sorted(arr)
        print("sorted",arr_sort)
        i=0
        j=1

        while(i<n and j<n):
            print((arr_sort[j],arr_sort[i]),arr_sort[j]-arr_sort[i])

            if(i!=j and arr_sort[j]-arr_sort[i]==x):
                return 1
            elif(arr_sort[j]-arr_sort[i]<x):
                j+=1
            else:
                i+=1

        return -1


class IntArray:
    def __init__(self):
        pass

    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]
        return arr

    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__ == '__main__':
    # t=int(input())
    # t=1
    t=1
    for _ in range(t):
        # n=int(input())
        # x=int(input())
        # n=6
        # x=78
        # n=5
        # x=45
        # n=6
        # x=8
        n=65
        x=13
        # arr=IntArray().Input(n)
        # arr=[5,20,3,2,5,80] #(2,80) have absolute difference of 78.
        # arr=[90,70,20,80,50]
        # arr=[1,10,1,1,7,2]
        arr=[42,12,54,69,48,45,63,58,38,60,24,42,30,79,17,36,91,43,89,7,41,43,65,49,47,6,91,30,71,51,7,2,94,49,30,24,85,55,57,41,67,77,32,9,45,40,27,24,38,39,19,83,30,42,34,16,40,59,5,31,78,7,74,87,22]
        obj=Solution()
        res=obj.findPair(n,x,arr)

        print(res)