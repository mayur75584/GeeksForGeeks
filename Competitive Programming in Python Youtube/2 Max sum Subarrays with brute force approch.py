'''
Example Test Case:
Array is given below
[-2,-3,4,-1,-2,1,5,-3]
Subarray with maximum sum
[4,-1,-2,1,5] = 7
'''
'''
Time Complexity is N^3 very large
'''

#generate all the subarrays
#check which subarray has the max sum
def bruteforce(A):
    n=len(A)
    subarrays=[]
    maxsum = float('-inf') #here -inf means minus infinity
    for i in range(n+1):
        for j in range(i+1,n+1):
            s=A[i:j]
            # subarrays.append(s)
            maxsum = max(maxsum,sum(s))
    # print(subarrays)
    print(maxsum)


testcase = [-2,-3,4,-1,-2,1,5,-3]
bruteforce(testcase)