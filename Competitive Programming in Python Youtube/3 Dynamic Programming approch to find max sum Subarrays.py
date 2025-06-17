'''
Example Test Case:
Array is given below
[-2,-3,4,-1,-2,1,5,-3]
Subarray with maximum sum
[4,-1,-2,1,5] = 7
'''
'''
Time Complexity O(N)
'''


#to find the maximum
#maximize the maxsum
#to maximize the maxsum we add positive integers/sum/prefixsum only
#and neglect negative integers/sum/prefixsum

def dp(A):
    n=len(A)
    for i in range(1,n):
        if A[i-1]>0: #positive integers/sum/prefixsum
            A[i] = A[i]+A[i-1]
    # then return the max of Array
    # meaning we are returning the max of integers/sum/prefixsum
    ans=max(A)
    print(ans)



testcase = [-2,-3,4,-1,-2,1,5,-3]
dp(testcase)



