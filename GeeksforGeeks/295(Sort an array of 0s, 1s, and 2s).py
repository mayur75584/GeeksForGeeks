'''
Sort an array of 0s, 1s and 2s

Given an array of size N containing only 0s, 1s, and 2s;
sort the array in ascending order.

Example 1:
Input:
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated
into ascending order.

Example 2:
Input:
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated
into ascending order.


Your Task:
You don't need to read input or print anything.
Your task is to complete the function sort012()
that takes an array arr and N as input parameters and sorts the array in-place.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 10^6
0 <= A[i] <= 2
'''
class Solution:
    def sort012(self,arr,n):
        count0=0
        count1=0
        count2=0
        for i in arr:
            if i==0:
                count0+=1
            elif i==1:
                count1+=1
            else:
                count2+=1
        i=0
        while(count0>0):
            arr[i]=0
            i+=1
            count0-=1
        while(count1>0):
            arr[i]=1
            i+=1
            count1-=1
        while(count2>0):
            arr[i]=2
            i+=1
            count2-=1
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=5
        # arr=[0,2,1,2,0]
        n=3
        arr=[0,1,0]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i,end=' ')
        print()