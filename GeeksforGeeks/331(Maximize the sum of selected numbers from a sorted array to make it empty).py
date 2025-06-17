'''
Maximize the sum of selected numbers from a sorted array to make it empty

Given a array of N numbers, we need to maximize the sum of selected numbers.
At each step, you need to select a number Ai,
delete one occurrence of Ai-1 (if exists),
and Ai each from the array.
Repeat these steps until the array gets empty.
The problem is to maximize the sum of the selected numbers.

Note: Numbers need to be selected from maximum to minimum.

Example 1:

Input : arr[ ] = {1, 2, 2, 2, 3, 4}
Output : 10
Explanation:
We select 4, so 4 and 3 are deleted leaving us with {1,2,2,2}.
Then we select 2, so 2 & 1 are deleted. We are left with{2,2}.
We select 2 in next two steps, thus the sum is 4+2+2+2=10.


Example 2:

Input : arr[ ] = {1, 2, 3}
Output :  4
Explanation: We select 3, so 3 and 2 are deleted leaving us with {1}.
Then we select 1, 0 doesn't exist so we delete 1. thus the sum is 3+1=4.



Your Task:
This is a function problem. The input is already taken care of by the driver code.
You only need to complete the function maximizeSum() that takes an array (arr),
sizeOfArray (n), and return the maximum sum of the selected numbers.
The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).


Constraints:
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 105
'''
class Solution:
    def maximizeSum(self,arr,n):
        'Getting TLE for below solution'
        # sum1=0
        # dict1={}
        # for i in arr:
        #     if i not in dict1:
        #         dict1[i]=1
        #     else:
        #         dict1[i]+=1
        # while(len(dict1)!=0):
        #     z=max(dict1)
        #     if z-1 in dict1 and dict1[z-1]!=0:
        #         sum1+=z
        #         dict1[z]-=1
        #         dict1[z-1]-=1
        #     else:
        #         sum1+=(z*dict1[z])
        #         dict1[z]=0
        #     if z in dict1:
        #         if dict1[z]==0:
        #             dict1.pop(z)
        #     if z-1 in dict1:
        #         if dict1[z-1]==0:
        #             dict1.pop(z-1)
        # return sum1

        'Optimized Solution'
        '''
        I think I was using inbuild functions like max() and index()
        so thats why I was getting TLE.
        Also Dynamic Programming Concept was used.
        '''
        sum1=0
        max1=arr[0]

        for i in range(len(arr)):
            if(arr[i]>max1):
                max1=arr[i]
        dict1={}
        for i in arr:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in range(n-1,-1,-1):
            key=arr[i]
            if(dict1[key]>0):
                sum1+=key
                dict1[key]-=1
                if key-1 in dict1:
                    dict1[key-1]-=1
        return sum1


# t=int(input())
t=1
for _ in range(t):
    # n=int(input())
    # arr=list(map(int,input().split()))
    n=6
    arr=[1,2,2,2,3,4]
    # n=3
    # arr=[1,2,3]
    arr.sort()
    ob=Solution()

    ans=ob.maximizeSum(arr,n)
    print(ans)