'''
Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]



Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109


'''
'''
Time Complexity : O(log n) 
Auxiliary Space : O(1) 
'''
class Solution:
    # If target is present in arr[] then
    # returns the index of FIRST
    # occurrence of target in arr[0..n-1],
    # otherwise returns -1
    def first(self,nums,target,n):
        low=0
        high=n-1
        res=-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]>target):
                high=mid-1
            elif(nums[mid]<target):
                low=mid+1
            # If arr[mid] is same as target, we
            # update res and move to the left
            # half.
            else:
                res=mid
                high=mid-1
        return res

    # If target is present in arr[] then returns
    # the index of FIRST occurrence of target in
    # arr[0..n-1], otherwise returns -1
    def last(self,nums,target,n):
        low=0
        high=n-1
        res=-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]>target):
                high=mid-1
            elif(nums[mid]<target):
                low=mid+1
            # If arr[mid] is same as target, we
            # update res and move to the Right
            # half.
            else:
                res=mid
                low=mid+1
        return res
    def searchRange(self,nums,target):
        res=[]
        res1=self.first(nums,target,len(nums))
        res2=self.last(nums,target,len(nums))
        res.append(res1)
        res.append(res2)
        return res

if __name__ == '__main__':
    # nums=list(map(int,input().split()))
    # target=int(input())
    # nums=[5,7,7,8,8,10]
    # target=8
    # nums=[5,7,7,8,8,10]
    # target=6
    nums=[]
    target=0
    ob=Solution()
    print(ob.searchRange(nums,target))