'''
Link to refer the diagram given in question

https://practice.geeksforgeeks.org/problems/3f48d387900a38bd9fd0594b93f9f4f97f5ada8a1644/1#
'''
'''
Triangle and Square

Geek has a ticket to the Geek Summer Carnival. The ticket has a positive integer B written on it.
B denotes the base of a right-angled isosceles triangle.
Geek can avail discounts on X courses in the carnival.

X is the maximum number of squares of size 2x2 units that can fit in the given right-angled isosceles triangle.
Find X.


Example 1:

Input:
B = 8
Output:
6
Explanation:


Example 2:

Input:
B = 2
Output:
0


Your Task:
You don't need to read input or print anything. Complete the function countSquare()
that takes integer b as input parameter and returns the number of possible squares
that can fit into the isosceles triangle.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
1 <= B <= 1000
'''

class Solution:
    def countShare(self,B):
        # removing the extra part we would always need
        B = (B - 2)
        # since each square has base of length of 2
        B = B // 2
        return B * (B + 1) // 2


if __name__ == '__main__':
    for _ in range(int(input())):
        b=int(input())
        obj=Solution()
        print(obj.countShare(b))