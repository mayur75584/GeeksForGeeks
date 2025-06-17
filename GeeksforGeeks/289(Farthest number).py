'''
Farthest number

Given an array Arr[] of size N.
For every element in the array, the task is to find
the index of the farthest element in the array
to the right which is smaller than the current element.
If no such number exists then print -1.
Note: 0 based indexing.

Example 1:
Input:
N=5
Arr[] = {3, 1, 5, 2, 4}
Output:
3 -1 4 -1 -1
Explanation:
Arr[3] is the farthest smallest element
to the right of Arr[0].
Arr[4] is the farthest smallest element
to the right of Arr[2].
And for the rest of the elements, there is
no smaller element to their right.

Example 2:
Input:
N=5
Arr[] = {1, 2, 3, 4, 0}
Output:
4 4 4 4 -1


Your Task:
You don't need to read input or print anything.
Your task is to complete the function farNumber()
which takes the N (number of elements in Array Arr) ,Arr[],
and returns the array of farthest element to the right for every element of the array.

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 1e5
0 ≤ Arr[i] ≤ 1e9

View Bookmarked Problems
Company Tags
Topic Tags
Binary Search
Arrays
Data Structures

'''

class Solution:
    def farNumber(self,N,Arr):
        arr_min=[0]*(N)
        arr_min[N-1]=Arr[N-1]
        for i in range(N-2,-1,-1):
            arr_min[i]=min(arr_min[i+1],Arr[i])
        print(arr_min)
        for i in range(N):
            low=i+1
            high=N-1
            val=-1
            while(low<=high):
                mid=(low+high)//2
                if(arr_min[mid]<Arr[i]):
                    val=mid
                    low=mid+1
                else:
                    high=mid-1
            arr_min[i]=val
        return arr_min
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # Arr=list(map(int,input().split()))
        # N=5
        # Arr=[3,1,5,2,4]
        N=5
        Arr=[1,2,3,4,0]
        ob=Solution()
        ans=ob.farNumber(N,Arr)
        for i in ans:
            print(i,end=" ")
        print()