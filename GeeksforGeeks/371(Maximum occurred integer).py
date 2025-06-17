'''
Maximum occured integer

Given n integer ranges, the task is to find the maximum occurring integer in these ranges.
If more than one such integer exists, find the smallest one.
The ranges are given as two arrays L[] and R[].  L[i] consists of starting point of range and R[i] consists of corresponding end point of the range.

For example consider the following ranges.
L[] = {2, 1, 3}, R[] = {5, 3, 9)
Ranges represented by above arrays are.
[2, 5] = {2, 3, 4, 5}
[1, 3] = {1, 2, 3}
[3, 9] = {3, 4, 5, 6, 7, 8, 9}
The maximum occurred integer in these ranges is 3.

Example 1:

Input:
n = 4
L[] = {1,4,3,1}
R[] = {15,8,5,4}
Output: 4
Explanation: The given ranges are [1,15]
 [4, 8] [3, 5] [1, 4]. The number that
is most common or appears most times in
the ranges is 4.

Example 2:

Input:
n = 5
L[] = {1,5,9,13,21}
R[] = {15,8,12,20,30}
Output: 5
Explanation: The given ranges are
[1,15] [5, 8] [9, 12] [13, 20]
[21, 30]. The number that is most
common or appears most times in
the ranges is 5.

Your Task:
The task is to complete the function maxOccured() which returns the maximum occured integer in all ranges.

Expected Time Complexity: O(n+maxx).
Expected Auxiliary Space: O(maxx).
-maxx is maximum element in R[]


Constraints:
1 ≤ n ≤ 106
0 ≤ L[i], R[i] ≤ 106

'''
'''
Algo

->Initiliaze array by 0
->Increment arr[Li] by 1 and decrement arr[Ri+1] by -1
->Take prefix sum of the array and return the minimum index with maximum prefix sum
'''
class Solution:
    def maxOccurred(self,L,R,N,maxx):
        # print(maxx)
        a=[0]*(maxx+2)
        pre_sum=0
        for i in range(N):
            a[L[i]]+=1
            a[R[i]+1]-=1
        print(a)
        pre_sum+=a[0]
        for i in range(1,len(a)):
            if a[i]==0:
                a[i]=pre_sum
            else:
                pre_sum+=a[i]
                a[i]=pre_sum
        return a.index(max(a))

import math
A=[0]*1000000

def main():
    # T=int(input())
    T=1
    while(T>0):
        global A
        # N=int(input())
        # L=[int(x) for x in input().split()]
        # R=[int(x) for x in input().split()]
        # N=4
        # L=[1,4,3,1]
        # R=[15,8,5,4]
        # N=4
        # L=[1,4,4,1]
        # R=[3,7,5,4]
        N=5
        L=[1,5,9,13,21]
        R=[15,8,12,20,30]
        maxx=max(R)

        ob=Solution()
        print(ob.maxOccurred(L,R,N,maxx))
        T-=1
if __name__ == '__main__':
    main()