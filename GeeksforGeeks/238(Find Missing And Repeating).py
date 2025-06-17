'''
Find Missing And Repeating

Given an unsorted array Arr of size N of positive integers.
One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array.
Find these two numbers.

Example 1:

Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and
smallest positive missing number is 1.

Example 2:

Input:
N = 3
Arr[] = {1, 3, 3}
Output: 3 2
Explanation: Repeating number is 3 and
smallest positive missing number is 2.

Your Task:
You don't need to read input or print anything. Your task is to complete
the function findTwoElement() which takes the array of integers arr and n as parameters
and returns an array of integers of size 2 denoting the answer
    ( The first index contains B and second index contains A.)

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ N
'''
'''
Approach for Repeating Element
Traverse the array. While traversing, use the absolute value of every element
as an index and make the value at this index as negative to mark it visited.
If something is already marked negative then this is the repeating element.
'''
'''
Approach for Missing Number

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
'''
Note for approach to find missing number
we have not used case for elements less than 0
so we are not making elements 1 as given above approach.
'''
class Solution:
    def findTwoElement(self,arr,n):
        res=[]
        'Repeating Element'
        z=[0]*(n+1)
        for i in range(n):
            x=arr[i]
            if z[x]!=-1:
                z[x]=-1
            elif z[x]==-1:
                res.append(x)
                break
        'Missing Number'
        ptr=0
        for i in range(n):
            if arr[i]==1:
                ptr=1
                break
        if ptr==0:
            res.append(1)
            return res
        for i in range(n):
            arr[(arr[i]-1)%n]+=n
        for i in range(n):
            if arr[i]<=n:
                res.append(i+1)
                return res
        res.append(n+1)
        return res

if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=2
        # arr=[2,2]
        n=3
        arr=[1,3,3]
        ob=Solution()
        ans=ob.findTwoElement(arr,n)
        print(str(ans[0])+" "+str(ans[1]))
        t=t-1