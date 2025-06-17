'''
Length of longest subarray with positive product

Given an array arr[] consisting of N integers,
the task is to print the length of the longest subarray with a positive product.

Examples:

    Input: arr[] ={0, 1, -2, -3, -4}
    Output: 3
    Explanation:
    The longest subarray with positive products is: {1, -2, -3}.
    Therefore, the required length is 3.

    Input: arr[]={-1, -2, 0, 1, 2}
    Output: 2
    Explanation:
    The longest subarray with positive products are: {-1, -2}, {1, 2}. Therefore, the required length is 2.

Time Complexity: O(N)
Auxiliary Space: O(1)
'''
'''
Efficient Approach:
The problem can be solved using Dynamic Programming.
The idea here is to maintain the count of positive elements and negative elements such that their product is positive.
Follow the steps below to solve the problem:

    Initialize the variable, say res, to store the length of the longest subarray with the positive product.
    Initialize two variables, Pos and Neg, to store the length of the current subarray with the positive and negative products respectively.
    Iterate over the array.
    If arr[i] = 0: Reset the value of Pos and Neg.
    If arr[i] > 0: Increment Pos by 1. If at least one element is present in the subarray with the negative product, then increment Neg by 1.
    If arr[i] < 0: Swap Pos and Neg and increment the Neg by 1. If at least one element is present in the subarray with the positive product, then increment Pos also.
    Update res=max(res, Pos).
'''
class Solution:
    def maxLength(self,arr,n):
        # Stores the length of current
        # subarray with positive product
        Pos=0
        # Stores the length of current
        # subarray with negative product
        Neg=0
        # Stores the length of the longest
        # subarray with positive product
        res=0
        for i in range(n):
            if(arr[i]==0):
                # Reset the value
                Pos=Neg=0
            # If current element is positive
            elif(arr[i]>0):
                # Increment the length of
                # subarray with positive product
                Pos+=1
                # If at least one element is
                # present in the subarray with
                # negative product
                if(Neg!=0):
                    Neg+=1
                # Update res
                res=max(res,Pos)
            # If current element is negative
            else:
                Pos,Neg=Neg,Pos
                # Increment the length of subarray
                # with negative product
                Neg+=1
                # If at least one element is present
                # in the subarray with positive product
                if(Pos!=0):
                    Pos+=1
                res=max(res,Pos)
        return res

# T=int(input())
T=1
while(T>0):
    # n=int(input())
    # arr=[int(x) for x in input().strip().split()]
    # n=5
    # arr=[0,1,-2,-3,-4]
    # n=5
    # arr=[-1,-2,0,1,2]
    n=5
    arr=[1,-2,3,-4,-1]
    obj=Solution()
    print(obj.maxLength(arr,n))
    T-=1