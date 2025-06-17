'''
Even and Odd

Given an array arr[] of size N containing equal number of odd and even numbers.
Arrange the numbers in such a way that all the even numbers get the even index
and odd numbers get the odd index.
Note: There are multiple possible solutions, Print any one of them.
Also, 0-based indexing is considered.

Example 1:
Input:
N = 6
arr[] = {3, 6, 12, 1, 5, 8}
Output:
1
Explanation:
6 3 12 1 8 5 is a possible solution.
The output will always be 1 if your
rearrangement is correct.

Example 2:
Input:
N = 4
arr[] = {1, 2, 3, 4}
Output :
1

Your Task:
You don't need to read input or print anything.
Your task is to complete the function reArrange()
which takes an integer N and an array arr of size N as input
and reArranges the array in Place without any extra space.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ arr[i] ≤ 105
'''
class Solution:
    def reArrange(self,arr,N):
        i=0
        j=1
        while(i<N and j<N):
            while(i<N and arr[i]%2==0):
                i+=2
            while(j<N and arr[j]%2!=0):
                j+=2
            if(i<N and j<N):
                arr[i],arr[j]=arr[j],arr[i]
                i+=2
                j+=2
        print(arr)

def check(arr,n):
    flag=1
    c=d=0
    for i in range(n):
        if(i%2==0):
            if(arr[i]%2):
                flag=0
                break
            else:
                c+=1
        else:
            if(arr[i]%2==0):
                flag=0
                break
            else:
                d+=1
    if(c!=d):
        flag=0
    return flag


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # arr=list(map(int,input().split()))
        # N=6
        # arr=[3,6,12,1,5,8]
        N=4
        arr=[1,2,3,4]
        ob=Solution()
        ob.reArrange(arr,N)
        print(check(arr,N))