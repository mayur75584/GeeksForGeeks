'''
Remove the balls

You are given two arrays, color and radius, representing a sequence of balls:

color[i] is the color of the i-th ball.

radius[i] is the radius of the i-th ball.

If two consecutive balls have the same color and radius, remove them both. Repeat this process until no more such pairs exist.


Return the number of balls remaining after all possible removals.

Examples:

Input: color[] = [2, 3, 5], radius[] = [3, 3, 5]
Output: 3
Explanation: All the 3 balls have different colors and radius.
Input: color[] = [2, 2, 5], radius[] = [3, 3, 5]
Output: 1
Explanation: First ball and second ball have same color 2 and same radius 3. So, after removing only one ball is left.
It cannot be removed from the array. Hence, the final array has length 1.
Constraints:
1 ≤ color.size() = radius.size() ≤ 105
1 ≤ color[i] ≤ 109
1 ≤ radius[i] ≤ 109


'''
class Solution:
    def findLength(self,color,radius):
        s1,s2=[],[]
        i,j=0,0

        while(i<len(color)):

            if i<len(color) and len(s2)<1:
                s1.append(color[i])
                i+=1
                s2.append(radius[j])
                j+=1
            else:
                if s1[-1]==color[i] and s2[-1]==radius[j]:
                    d1=s1.pop(-1)
                    i+=1
                    d2=s2.pop(-1)
                    j+=1
                else:
                    s1.append(color[i])
                    i+=1
                    s2.append(radius[j])
                    j+=1

        #if i >= len(s1):
        if len(s1)==2 and len(s2)==2:
            if s1[-1] == s1[-2] and s2[-1] == s2[-2]:
                    d1 = s1.pop(-1)
                    d2 = s1.pop(-1)
                    d3 = s2.pop(-1)
                    d4 = s2.pop(-1)

        print(s1)
        return len(s1)

if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # color=list(map(int,input().split()))
        # radius=list(map(int,input().split()))
        # color=[2,3,5]
        # radius=[3,3,3]
        # color=[2,2,5]
        # radius=[3,3,5]
        # color=[1,2,2,1]
        # radius=[1,2,2,1]
        # color=[4,4]
        # radius=[5,5]
        color=[51,14,14,11,81,84,71,78,45,5]
        radius=[60,52,27,80,67,27,15,77,13,91]
        obj=Solution()
        print(obj.findLength(color,radius))
        t-=1