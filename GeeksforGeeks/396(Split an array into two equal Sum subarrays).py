'''
Split an array into two equal Sum subarrays

Given an array of integers arr, return true if it is possible to split it in two subarrays (without reordering the elements),
such that the sum of the two subarrays are equal. If it is not possible then return false.

Examples:

Input: arr = [1, 2, 3, 4, 5, 5]
Output: true
Explanation: In the above example, we can divide the array into two subarrays with equal sum. The two subarrays are: [1, 2, 3, 4] and [5, 5].
The sum of both the subarrays are 10. Hence, the answer is true.
Input: arr = [4, 3, 2, 1]
Output: false
Explanation: In the above example, we cannot divide the array into two subarrays with equal sum. Hence, the answer is false.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
1<=arr.size()<=105
1<=arr[i]<=106


'''


class Solution:
    def canSplit(self,arr):
        left = 0
        right = 0

        sum_arr = sum(arr)
        for i in range(len(arr)-1,-1,-1):
            right+=arr[i]
            left=sum_arr-right
            if right==left:
                return True
        return False





if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # arr=list(map(int,input().split()))
        arr=[1,2,3,4,5,5]
        # arr=[4,3,2,1]
        # arr=[4,1,2,3,4]
        obj=Solution()
        res=obj.canSplit(arr)
        if(res):
            print("true")
        else:
            print("false")