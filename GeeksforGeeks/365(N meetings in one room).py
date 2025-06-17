'''
N meetings in one room

There is one meeting room in a firm.
There are N meetings in the form of (start[i], end[i])
where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings
that can be accommodated in the meeting room when only one meeting
can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time
of the other chosen meeting.


Example 1:

Input:
N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output:
4
Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)

Example 2:

Input:
N = 3
start[] = {10, 12, 20}
end[] = {20, 25, 30}
Output:
1
Explanation:
Only one meetings can be held
with given start and end timings.


Your Task :
You don't need to read inputs or print anything.
Complete the function maxMeetings() that takes two arrays start[]
and end[] along with their size N as input parameters and
returns the maximum number of meetings that can be held in the meeting room.


Expected Time Complexity : O(N*LogN)
Expected Auxilliary Space : O(N)


Constraints:
1 ≤ N ≤ 105
0 ≤ start[i] < end[i] ≤ 105

'''
class Solution:
    def maximumMeetings(self,n,start,end):
        lst=[]
        for i in range(n):
            lst.append((start[i],end[i]))
        print(lst)
        lst=sorted(lst,key= lambda x:x[1])
        print(lst)
        min1=-9999999999
        max1=-9999999999
        count1=0
        for i in lst:
            if i[0]>max1 and min1<i[1] and max1<i[1]:
                min1=i[0]
                max1=i[1]
                count1+=1
        return count1

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # start=list(map(int,input().split()))
        # end=list(map(int,input().split()))
        # n=6
        # start=[1,3,0,5,8,5]
        # end=[2,4,6,7,9,9]
        n=3
        start=[10,12,20]
        end=[20,25,30]
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))