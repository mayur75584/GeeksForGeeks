'''
Overlapping Intervals

Given a collection of Intervals, the task is to merge all of the overlapping
Intervals.

Example 1:

Input:
Intervals = {{1,3},{2,4},{6,8},{9,10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: Given intervals: [1,3],[2,4]
[6,8],[9,10], we have only two overlapping
intervals here,[1,3] and [2,4]. Therefore
we will merge these two and return [1,4],
[6,8], [9,10].

Example 2:

Input:
Intervals = {{6,8},{1,9},{2,4},{4,7}}
Output: {{1, 9}}

Your Task:
Complete the function overlappedInterval() that takes the list N intervals as
input parameters and returns sorted list of intervals after merging.

Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(Log(N)) or O(N).

Constraints:
1 ≤ N ≤ 100
0 ≤ x ≤ y ≤ 1000
'''
'''
An efficient approach is to first sort the intervals according to the starting time. 
Once we have the sorted intervals, we can combine all intervals in a linear traversal.
 The idea is, in sorted array of intervals, if interval[i] doesn’t overlap with
  interval[i-1], then interval[i+1] cannot overlap with interval[i-1] because 
  starting time of interval[i+1] must be greater than or equal to interval[i]. 
  Following is the detailed step by step algorithm. 
'''
class Solution:
    def overlappedInterval(self,Intervals):
        z=Intervals
        Intervals.sort(key=lambda x:x[0])

        m=[]
        s=-10000
        max1=-100000
        for i in range(len(Intervals)):
            a=Intervals[i]
            if a[0]>max1:
                if i!=0:
                    m.append([s,max1])
                max1=a[1]
                s=a[0]
            else:
                if a[1]>=max1:
                    max1=a[1]
        # 'max1' value gives the last point of
        # that particular interval
        # 's' gives the starting point of that interval
        # 'm' array contains the list of all merged intervals

        if max1!=-100000 and [s,max1] not in m:
            m.append([s,max1])
        return m

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # a=list(map(int,input().split()))
        # Intervals=[]
        # j=0
        # for k in range(n):
        #     x=a[j]
        #     j+=1
        #     y=a[j]
        #     j+=1
        #     Intervals.append([x,y])
        n=4
        Intervals=[[1,3],[2,4],[6,8],[9,10]]
        # n=4
        # Intervals=[[6,8],[1,9],[2,4],[4,7]]
        obj=Solution()
        ans=obj.overlappedInterval(Intervals)
        for i in ans:
            for j in i:
                print(j,end=' ')
        print()