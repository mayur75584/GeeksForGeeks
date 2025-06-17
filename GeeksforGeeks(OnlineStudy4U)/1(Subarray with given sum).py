'''
Subarray with given sum

Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.



Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.



Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements
from 1st position to 5th position
is 15.



Your Task:
You don't need to read input or print anything.
The task is to complete the function subarraySum() which takes arr, N and S as input parameters and returns a list
containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S.
The two indexes in the list should be according to 1-based indexing. If no such subarray is found, return an array consisting only one element that is -1.



Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)



Constraints:
1 <= N <= 105
1 <= Ai <= 1010
'''

'Note-> Logic by onlinestudy4U is not passing all test cases'
class Solution:
    def subArraySum(self, arr, n, s):
        lst = []
        curr_sum=arr[0]
        start=0
        for i in range(1,n):
            while(curr_sum>s and start < i-1):
                curr_sum = curr_sum - arr[start]
                start+=1
            if curr_sum == s:
                lst.append(start+1)
                lst.append(i)
                return lst
            else:
                curr_sum = curr_sum + arr[i]
        return -1


if __name__ == '__main__':
    # T=int(input())
    T = 1
    while (T > 0):
        # NS=input().strip().split()
        # N=int(NS[0])
        # S=int(NS[1])
        #
        # A=list(map(int,input().split()))

        # N,S=5,12
        # A=[1,2,3,7,5]
        # N, S = 10, 15
        # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        N,S=42,468
        A=[135, 101, 170, 125 ,79 ,159 ,163 ,65 ,106 ,146 ,82 ,28, 162, 92 ,196, 143, 28 ,37 ,192 ,5 ,103, 154 ,93 ,183 ,22 ,117 ,119 ,96 ,48 ,127 ,172 ,139 ,70 ,113 ,68 ,100 ,36 ,95 ,104 ,12 ,123 ,134]
        ob = Solution()
        ob.subArraySum(A, N, S)
        ans=ob.subArraySum(A,N,S)

        for i in ans:
            print(i,end=' ')
        print()

        T -= 1