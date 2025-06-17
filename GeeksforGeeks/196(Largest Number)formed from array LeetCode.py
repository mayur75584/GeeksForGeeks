'''
Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"



Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 109


'''

class Solution:
    def largestNumber(self, nums):
        if not any(map(bool,nums)): #check , if all elemnts of arr are 0 then return 0 and if #any one element in arr is not 0 then if statement will not execute
            return "0"

        nums=list(map(str,nums))
        if len(nums)<2:
            return "".join(nums)
        def compare(x,y):
            return int(nums[x]+nums[y])>int(nums[y]+nums[x])
        for x in range(len(nums)-1):
            y=x+1
            while(x<len(nums) and y<len(nums)):
                if compare(x,y):
                    pass
                else:
                    nums[y],nums[x]=nums[x],nums[y]
                y+=1
        return "".join(nums)
if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # nums=list(map(int,input().split())
        # nums=[3,30,34,5,9]
        # nums=[54,546,548,60]
        nums=[250,74,659,931,273,545,879,924]
        ob=Solution()
        ans=ob.largestNumber(nums)
        print(ans)
        t-=1


