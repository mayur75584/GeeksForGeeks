'''
Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33


Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''
class Solution:
    def getRow(self,rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            # print([1,1])
            lst = [[1],[1,1]]
            return lst[1]

        lst = [[1], [1, 1]]
        for i in range(3, rowIndex + 2):
            lst1 = [0] * (i)
            n = len(lst1)
            lst1[0] = 1
            lst1[n - 1] = 1
            for j in range(1, n - 1):
                x = lst[-1]
                lst1[j] = x[j - 1] + x[j]
            lst.append(lst1)
            # print(lst)
        return lst[rowIndex]


if __name__ == '__main__':
    t=1
    for i in range(t):
        # N=int(input())
        # N=1
        # N=3
        N=4
        ob=Solution()
        ans = ob.getRow(N)
        print(ans)