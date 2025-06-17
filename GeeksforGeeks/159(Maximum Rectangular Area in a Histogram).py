

'''
Link for the image

https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1

Maximum Rectangular Area in a Histogram

Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have the same width and the width is 1 unit, there will be N bars height of each bar will be given by the array arr.

Example 1:

Input:
N = 7
arr[] = {6,2,5,4,5,1,6}
Output: 12
Explanation: 


Example 2:

Input:
N = 8
arr[] = {7 2 8 9 1 3 6 5}
Output: 16
Explanation: Maximum size of the histogram 
will be 8  and there will be 2 consecutive 
histogram. And hence the area of the 
histogram will be 8x2 = 16.

Your Task:
The task is to complete the function getMaxArea() which takes the array arr[] and its size N as inputs and finds the largest rectangular area possible and returns the answer.

Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 ≤ N ≤ 106
1 ≤ arr[i] ≤ 1012
'''

'''
Formula to find area of rectangle at each index

{[left-right]+1}*height

where {[left-right]+1} is width
'''
'Most Efficient, clears all test cases'
class Solution:
    def getMaxArea(self,histogram):
        stack=[-1]
        max_area=0
        for i in range(len(histogram)):
            while(stack[-1]!=-1 and histogram[stack[-1]]>=histogram[i]):
                curr_height=histogram[stack.pop()]
                curr_width=i-stack[-1]-1
                max_area=max(max_area,curr_height*curr_width)
            stack.append(i)
        while(stack[-1]!=-1):
            curr_height=histogram[stack.pop()]
            curr_width=len(histogram)-stack[-1]-1
            max_area=max(max_area,curr_height*curr_width)
        return max_area

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # a=list(map(int,input().split()))
        n=5
        a=[1,2,3,4,5]
        # n=7
        # a=[6,2,5,4,5,1,6]
        # n=8
        # a=[7,2,8,9,1,3,6,5]
        ob=Solution()
        print(ob.getMaxArea(a))

'Most Optimized Solution not able to clear sorted one test case'
# class Solution:
#     def getMaxArea(self,histogram):
#         stack=[]
#         maxA=0
#         n=len(histogram)
#         for i in range(n):
#             while(len(stack)!=0 and(i==n or histogram[stack[-1]]>=histogram[i])):
#                 h=histogram[stack[-1]]
#                 stack.pop(-1)
#                 width=999
#                 if(len(stack)==0):
#                     width=i
#                 else:
#                     width=i-stack[-1]-1
#                 maxA=max(maxA,width*h)
#             stack.append(i)
#         return maxA
#
# if __name__ == '__main__':
#     # t=int(input())
#     t=1
#     for i in range(t):
#         # n=int(input())
#         # a=list(map(int,input().split()))
#         # n=7
#         # a=[6,2,5,4,5,1,6]
#         # n=8
#         # a=[7,2,8,9,1,3,6,5]
#         n=5
#         a=[1,2,3,4,5]
#         ob=Solution()
#         print(ob.getMaxArea(a))

'Getting TLE for some test cases'
# class Solution:
#     def getMaxArea(self,histogram):
#         n=len(histogram)
#         leftSmall=[0]*n
#         rightSmall=[0]*n
#
#         st=[]
#         #Left array
#         for i in range(n):
#             while(len(st)!=0 and histogram[st[-1]]>=histogram[i]):
#                 st.pop(-1)
#             if(len(st)==0):
#                 leftSmall[i]=0
#             else:
#                 leftSmall[i]=st[-1]+1
#             st.append(i)
#         print(leftSmall)
#
#         while(len(st)!=0):
#             st.pop(-1)
#
#         #Right array
#         for i in range(n-1,-1,-1):
#             while(len(st)!=0 and histogram[st[-1]]>=histogram[i]):
#                 st.pop(-1)
#             if(len(st)==0):
#                 rightSmall[i]=n-1
#             else:
#                 rightSmall[i]=st[-1]-1
#             st.append(i)
#         print(rightSmall)
#
#         #Calculating Area and Finding Maximum Area
#         maxA=0
#         for i in range(n):
#             maxA=max(maxA,histogram[i]*((rightSmall[i]-leftSmall[i]) +1))
#
#         return maxA
# if __name__ == '__main__':
#     # t=int(input())
#     t=1
#     for _ in range(t):
#         # n=int(input())
#         # a=list(map(int,input().split()))
#         # n=7
#         # a=[6,2,5,4,5,1,6]
#         n=8
#         a=[7,2,8,9,1,3,6,5]
#         ob=Solution()
#         print(ob.getMaxArea(a))

