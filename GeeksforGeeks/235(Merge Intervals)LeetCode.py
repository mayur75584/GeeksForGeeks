'''
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.



Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104


'''

class Solution:
    def merge(self,intervals):
        'First Solution'
        # intervals = sorted(intervals, key=lambda x:x[0])
        # ret = []
        # for i in intervals:
        #     newInterval = i
        #     #compare with the last one in ret
        #     if ret:
        #         if ret[-1][1] >= i[0]:
        #             #merge and then replace the last one in ret
        #             newInterval = ret.pop()
        #             if i[1] > newInterval[1]:
        #                 newInterval[1] = i[1]
        #     ret.append(newInterval)
        # return ret
        'Second Solution'
        intervals.sort(key=lambda x: x[0])
        m = []
        s = -10000
        max1 = -100000
        for i in range(len(intervals)):
            a = intervals[i]
            if a[0] > max1:
                if i != 0:
                    m.append([s, max1])
                s = a[0]
                max1 = a[1]
            else:
                if a[1] >= max1:
                    max1 = a[1]
        if max1 != 100000 and [s, max1] not in m:
            m.append([s, max1])
        return m


if __name__ == '__main__':
    # n=int(input())
    # intervals=[]
    # for i in range(n):
    #     intervals.append(list(map(int,input().split())))
    intervals=[[1,3],[2,6],[8,10],[15,18]]
    obj=Solution()
    print(obj.merge(intervals))