'''
Number of Rectangles in a Circle


Given a circular sheet of radius, r.
Find the total number of rectangles with integral length and width that can be cut from the sheet that can fit on the circle, one at a time.

Examples :

Input: r=1
Output: 1
Explanation: Only 1 rectangle of dimensions 1x1.
Input: r=2
Output: 8
Explanation: The 8 possible rectangles are
(1x1)(1x2)(1x3)(2x1)(2x2)(2x3)(3x1)(3x2).
Expected Time Complexity: O(r2)
Expected Auxillary Space: O(1)


Constraints:
1<=r<=1000


'''
'''
Using Pythagoras theorem

a**2 + b**2 = d**2 i.e (2*r)**2

since we have radius , we can find diameter and then its square also.
then we can find one of the side i.e

a**2=(2*r)*(2*r)-b**2

since we have to find all pairs, so our value of a and b will be
less than or equal to 2*r
'''
import math

class Solution:
    def rectanglesInCircle(self,r):
        d=2*r
        rec=0
        for i in range(1,2*r):
            for j in range(1,2*r):
                if(i**2<=(((2*r)*(2*r))-j**2)):
                    print(str(i),str(j),i+j)
                    rec+=1
        return rec
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # N=2
        N=3
        ob=Solution()
        ans=ob.rectanglesInCircle(N)
        print(ans)



