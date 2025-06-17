'''
Pascal's Triangle

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
            1
        1       1
        1  2    1
        1 3  3  1
        1 4 6 4 1

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
'''
class Solution:
    def generate(self,numRows):
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            # print([1,1])
            return [[1], [1, 1]]

        lst = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            lst1 = [0] * (i)
            n = len(lst1)
            lst1[0] = 1
            lst1[n - 1] = 1
            for j in range(1, n - 1):
                x = lst[-1]
                lst1[j] = x[j - 1] + x[j]
            lst.append(lst1)
            # print(lst)
        return lst

if __name__ == '__main__':
    t=1
    for _ in range(1):
        # N=int(input())
        # N=5
        N=6
        ob=Solution()
        ans = ob.generate(N)
        print(ans)