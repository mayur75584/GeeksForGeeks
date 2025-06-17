'''
Given a zero-based permutation nums(0-indexed), build an array
ans of the same length where ans[i] = nums[nums[i]]
for each 0<=i<nums.length and return it.
A zero-based permutation nums is an array of distinct integers
from 0 to nums.length-1 (inclusive).

Example 1:
Input:
nums=[0,2,1,5,3,4]
Output:
[0,1,2,4,5,3]

Example2:
Input:
nums=[5,0,1,2,3,4]
Output:
[4,5,0,1,2,3]
'''
'Optimizing space complexity'
'''
Time Complexity is O(n)
Space Complexity is O(1)
'''
'Below is the optimized code for space complexity'
def func(nums):
    n=len(nums)
    for i in range(len(nums)):
        nums[i] = nums[i] + n*(nums[nums[i]%n]%n) #Formula
    print(nums)
    for i in range(len(nums)):
        nums[i]//=n
        print(nums[i],end=' ')


if __name__ == '__main__':
    # nums=list(map(int,input().split()))
    nums=[0,2,1,5,3,4]
    # nums=[5,0,1,2,3,4]
    func(nums)


'''
Time complexity is O(n)
Space complexity is O(n)
'''
# def func(nums):
#     n=len(nums)
#     ans=[0]*n
#     print(ans)
#     for i in range(len(nums)):
#         ans[i]=nums[nums[i]]
#     for i in ans:
#         print(i,end=' ')
#
#
#
# if __name__ == '__main__':
#     # nums=list(map(int,input().split()))
#     nums=[0,2,1,5,3,4]
#     # nums=[5,0,1,2,3,4]
#     func(nums)
