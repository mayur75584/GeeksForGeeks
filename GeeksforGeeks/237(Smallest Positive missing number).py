'''
Smallest Positive missing number

You are given an array arr[] of N integers including 0.
The task is to find the smallest positive number missing from the array.

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing
number is 6.

Example 2:

Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Explanation: Smallest positive missing
number is 2.

Your Task:
The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
-106 <= arr[i] <= 106
'''

'Approch in O(N) Time Complexity and O(1) Space Complexity'
'''
The smallest positive integer is 1. First we will check if 1 is present in the array or not.
If it is not present then 1 is the answer.
If present then, again traverse the array. The largest possible answer is N+1 where N is the size of array.
This will happen when array have all the elements from 1 to N. When we are traversing the array,
if we find any number less than 1 or greater than N, then we will change it to 1.
This will not change anything as answer will always between 1 to N+1. Now our array has elements from 1 to N.
Now, for every ith number, increase arr[ (arr[i]-1) ] by N. But this will increase the value more than N.
So, we will access the array by arr[(arr[i]-1)%N]. What we have done is for each value we have increased value
at that index by N.
We will find now which index has value less than N+1. Then i+1 will be our answer.
'''
class Solution:
    def missingNumber(self,arr,n):
        ptr=0
        #Check if 1 is present in array or not
        for i in range(n):
            if arr[i]==1:
                ptr=1
                break
        #If 1 is not present
        if ptr==0:
            return 1
        #Changing values to 1
        for i in range(n):
            if arr[i]<=0 or arr[i]>n:
                arr[i]=1
        #Updating indices by + n according to values
        for i in range(n):
            arr[(arr[i]-1)%n]+=n
        #Finding which index has values less than n
        for i in range(n):
            if arr[i]<=n:
                return i+1
        #If array has values from 1 to n
        return n+1
if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=5
        arr=[1,2,3,4,5]
        # n=5
        # arr=[0,-10,1,3,-20]
        ob=Solution()
        print(ob.missingNumber(arr,n))
        t-=1
    
