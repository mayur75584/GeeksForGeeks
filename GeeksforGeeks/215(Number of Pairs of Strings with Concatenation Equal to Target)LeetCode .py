'''
2023. Number of Pairs of Strings With Concatenation Equal to Target

Given an array of digit strings nums and a digit string target,
return the number of pairs of indices (i, j) (where i != j) such that
the concatenation of nums[i] + nums[j] equals target.


Example 1:
Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"

Example 2:
Input: nums = ["123","4","12","34"], target = "1234"
Output: 2
Explanation: Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"

Example 3:
Input: nums = ["1","1","1"], target = "11"
Output: 6
Explanation: Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"



Constraints:
    2 <= nums.length <= 100
    1 <= nums[i].length <= 100
    2 <= target.length <= 100
    nums[i] and target consist of digits.
    nums[i] and target do not have leading zeros.


'''


from itertools import permutations
class Solution:
    def numOfPairs(self,nums,target):
        z = []
        for i in permutations(nums, 2):
            x = list(i)
            a, b = x[0], x[1]
            if a + b == target:
                z.append(x)
        # print(z)
        return len(z)


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        nums=list(map(str,input().split()))
        target=input()

        ob=Solution()
        print(ob.numOfPairs(nums,target))