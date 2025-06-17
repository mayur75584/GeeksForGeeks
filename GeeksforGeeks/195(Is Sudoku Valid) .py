'''
Is Sudoku Valid

Given an incomplete Sudoku configuration in terms of a 9x9  2-D square matrix(mat[][])
the task to check if the current configuration is valid or not where a 0 represents an empty block.
Note: Current valid configuration does not ensure validity of the final solved sudoku.
Refer to this : https://en.wikipedia.org/wiki/Sudoku

Example 1:

Input: mat[][] = [
[3, 0, 6, 5, 0, 8, 4, 0, 0]
[5, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 7, 0, 0, 0, 0, 3, 1]
[0, 0, 3, 0, 1, 0, 0, 8, 0]
[9, 0, 0, 8, 6, 3, 0, 0, 5]
[0, 5, 0, 0, 9, 0, 6, 0, 0]
[1, 3, 0, 0, 0, 0, 2, 5, 0]
[0, 0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]
Output: 1
Explaination: It is possible to have a
proper sudoku.

Your Task:
You do not need to read input or print anything. Your task is to complete the function isValid() which takes mat[][] as input parameter and returns 1 if any solution is possible. Otherwise, returns 0.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:
0 ≤ mat[i][j] ≤ 9
'''
class Solution:
    def isValid(self,mat):
        S = set()
        for i in range(9):
            for j in range(9):
                val = mat[i][j]
                if (val != 0):
                    block = 3 * (i // 3) + (j // 3)
                    if (S.__contains__(tuple(['r', i,val]))):  # here insted of S.__contains__ we can also use if tuple(['r',i,val]) in S:
                        return 0
                    if (S.__contains__(tuple(['c', j, val]))):
                        return 0
                    if (S.__contains__(tuple(['b', block, val]))):
                        return 0
                    else:
                        S.add(tuple(['r', i, val]))
                        S.add(tuple(['c', j, val]))
                        S.add(tuple(['b', block, val]))
        return 1


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # mat=[]
        # for i in range(9):
        #     arr=list(map(int,input().split()))
        #     mat.append(arr)
        mat=[[3, 0, 6, 5, 0, 8, 4, 0, 0],[5, 2, 0, 0, 0, 0, 0, 0, 0],[0, 8, 7, 0, 0, 0, 0, 3, 1],[0, 0, 3, 0, 1, 0, 0, 8, 0],[9, 0, 0, 8, 6, 3, 0, 0, 5],[0, 5, 0, 0, 9, 0, 6, 0, 0],[1, 3, 0, 0, 0, 0, 2, 5, 0],[0, 0, 0, 0, 0, 0, 0, 7, 4],[0, 0, 5, 2, 0, 6, 3, 0, 0]]

        ob=Solution()
        print(ob.isValid(mat))


