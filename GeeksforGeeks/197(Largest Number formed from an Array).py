'''
Largest Number formed from an Array
Given a list of non negative integers, arrange them in such a manner
that they form the largest number possible.
The result is going to be very large, hence return the result in the
 form of a string.


Example 1:

Input:
N = 5
Arr[] = {3, 30, 34, 5, 9}
Output: 9534330
Explanation: Given numbers are {3, 30, 34,
5, 9}, the arrangement 9534330 gives the
largest value.

Example 2:

Input:
N = 4
Arr[] = {54, 546, 548, 60}
Output: 6054854654
Explanation: Given numbers are {54, 546,
548, 60}, the arrangement 6054854654
gives the largest value.


Your Task:
You don't need to read input or print anything. Your task is to complete
the function printLargest() which takes the array of strings arr[]
 as parameter and returns a string denoting the answer.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 105
0 ≤ Arr[i] ≤ 1018
Sum of all the elements of the array is greater than 0.
'''

from functools import cmp_to_key as c
# cmp_to_key is used to convert a comparator into a key type
# function

class Solution:
    'Getting TLE for below Solution'
    # def printLargest(self, arr):
        # code here
        # if not any(map(bool,arr)): #check , if all elemnts of arr are 0 then return 0 and if any one element in arr is not 0 then if statement will not execute
        #     return "0"
        # nums=list(map(str,arr))
        # if len(nums)<2:
        #     return "".join(nums)
        # def compare(x,y):
        #     return int(nums[x]+nums[y])>int(nums[y]+nums[x])
        # for x in range(len(nums)-1):
        #     y=x+1
        #     while(x<len(nums) and y<len(nums)):
        #         if compare(x,y):
        #             pass
        #         else:
        #             nums[y],nums[x]=nums[x],nums[y]
        #         y+=1
        # return "".join(nums)

    'Correct Solution '
    def printLargest(self,arr):
        arr=list(map(str,arr))
        def compare(a,b):
            if((a+b)>(b+a)):
                return 1
            elif((a+b)<(b+a)):
                return -1
            else:
                return 0
        sorted_arr=sorted(arr,key=c(compare),reverse=True)
        ans="".join(sorted_arr)
        return ans
if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=8
        arr = [250, 74, 659, 931, 273, 545, 879, 924]
        ob=Solution()
        ans=ob.printLargest(arr)
        print(ans)
        t-=1

