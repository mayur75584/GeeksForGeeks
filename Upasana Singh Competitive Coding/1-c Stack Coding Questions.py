'''
Largest Rectangular Area in a Histogram

Find the largest rectangular area possible in a given histogram where
the largest rectangle can be made of a number of contiguous bars.
For simplicity, assume that all bars have same width and the width is 1 unit.
For example consider the following histogram with 7 bars of heights
[6,2,5,4,5,1,6]. The largest possible rectangle possible is 12.
'''
'Most optimal Solution'
def largestRectangleArea(heights):
    stack=[]
    maxA=0
    n=len(heights)
    for i in range(n):
        while(len(stack)!=0 and (i==n or heights[stack[-1]]>=heights[i])):
            h=heights[stack[-1]]
            stack.pop(-1)
            width=999
            if(len(stack)==0):
                width=i
            else:
                width=i-stack[-1]-1
            maxA=max(maxA,width*h)
        stack.append(i)
    return maxA

if __name__ == '__main__':
    heights=[2,1,5,6,2,3,1]
    print(largestRectangleArea(heights))

'Less optimal Solution'
# def largestRectangleArea(heights):
#     n=len(heights)
#     leftSmall=[0]*n
#     rightSmall=[0]*n
#     stack=[]
#     #Left Small
#     for i in range(n):
#         while(len(stack)!=0 and heights[stack[-1]]>=heights[i]):
#             stack.pop(-1)
#         if(len(stack)==0):
#             leftSmall[i]=0
#         else:
#             leftSmall[i]=stack[-1]+1
#         stack.append(i)
#     #cleared the stack to be re-used
#     stack.clear()
#     #Right Small
#     for i in range(n-1,-1,-1):
#         while(len(stack)!=0 and heights[stack[-1]]>=heights[i]):
#             stack.pop(-1)
#         if(len(stack)==0):
#             rightSmall[i]=n-1
#         else:
#             rightSmall[i]=stack[-1]-1
#         stack.append(i)
#     maxA=0
#     for i in range(n):
#         maxA=max(maxA,heights[i]*(rightSmall[i]-leftSmall[i]+1))
#     return maxA
#
# if __name__ == '__main__':
#     heights=[2,1,5,6,2,3,1]
#     print(largestRectangleArea(heights))