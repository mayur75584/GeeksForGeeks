'''
Write an efficient program to find the sum of contiguous subarray within a one-dimensional
array of numbers that has the largest sum.

-2 -3 4 -1 -2 1 5 -3

4+(-1)+(-2)+1+5=7

Maximum Contiguous Array Sum is 7
'''
'''
Kadanes Algorithm is used
'''

def maxSubArray(nums):
    max_sum=nums[0]
    curr_sum=0
    for i in range(n):
        curr_sum+=nums[i]
        if(curr_sum>max_sum):
            max_sum=curr_sum
        if(curr_sum<0):
            curr_sum=0
    return max_sum

if __name__ == '__main__':
    # n=int(input())
    # nums=[]
    # for i in range(n):
    #     nums.append(int(input()))
    # n=5
    # nums=[1,2,3,-2,5]
    n=8
    nums=[-2,-3,4,-1,-2,1,5,-3]
    print(maxSubArray(nums))
