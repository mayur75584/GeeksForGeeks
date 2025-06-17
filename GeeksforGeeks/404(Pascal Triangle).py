'''
Pascal Triangle

Given a positive integer n, return the nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.

File:PascalTriangleAnimated2.gif

Examples:

Input: n = 4
Output: [1, 3, 3, 1]
Explanation: 4th row of pascal's triangle is [1, 3, 3, 1].
Input: n = 5
Output: [1, 4, 6, 4, 1]
Explanation: 5th row of pascal's triangle is [1, 4, 6, 4, 1].
Input: n = 1
Output: [1]
Explanation: 1st row of pascal's triangle is [1].
Constraints:
1 ≤ n ≤ 20

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)

'''

'''
Formula -

If given row then consider row-1 and given column then column-1.

Then n^^C base r = n!/r!*(n-r)! i.e nCr
Shortcut -
7C2 = 7*6*5*4*3*2*1/2*1 * (7-2)!
    = 7*6*5*4*3*2*1/2*1 * (5*4*3*2*1)
    = 7*6/2*1

Similarly = 10C3
    we can keep -
    10*9*6/1*2*3

    means 10/1 * 9/2 * 6*3

'''

class Solution:

    def nthRowOfPascalTriangle(self,n):
        #fact=self.factorial(n)
        lst=[1]
        res=1
        for i in range(1,n):
            '''
            res=res*(n-i) #For 0 value 10-0=0, For 1 value will be 10-1=9, for 2 value will be 10-2=8
            res=res/(i+1) # For i when 0 then i+1 i.e 1, for i=1 then i+1 i.e 2
            '''
            res=res*(n-i)
            res=res//i
            # print(res)
            lst.append(res)
        return lst

if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n=int(input())
        # n=5
        n=11
        ob=Solution()
        ans=ob.nthRowOfPascalTriangle(n)
        print(ans)
        t-=1
        print("~")