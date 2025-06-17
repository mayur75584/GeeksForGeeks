
'''
Count More than n/k Occurences

Given an array arr[] of size N and an element k.
The task is to find all elements in array that appear more than n/k times.

Example 1:

Input:
N = 8
arr[] = {3,1,2,2,1,2,3,3}
k = 4
Output: 2
Explanation: In the given array, 3 and
 2 are the only elements that appears
more than n/k times.

Example 2:

Input:
N = 4
arr[] = {2,3,3,2}
k = 3
Output: 2
Explanation: In the given array, 3 and 2
are the only elements that appears more
than n/k times. So the count of elements
are 2.

Your Task:
The task is to complete the function countOccurence()
which returns count of elements with more than n/k times appearance.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 104
1 <= a[i] <= 106
1 <= k <= N
'''

class Solution:
    # Function to find all elements in array that appear more than n/k times.
    def countOccurence(self ,arr ,n ,k):
        # Your code here
        dict1={}
        for i in arr:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        count1 =0
        for i in dict1.items():
            if i[1]>n//k:
                count1+=1
        return count1


if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        N=int(input())
        A=list(map(int,input().split()))
        K=int(input())
        print(Solution().countOccurence(A,N,K))
        T-=1