'''
Majority Element

Given an array A of N elements. Find the majority element in the array.
A majority element in an array A of size N is an element that appears more than N/2 times in the array.

Example 1:

Input:
N = 3
A[] = {1,2,3}
Output:
-1
Explanation:
Since, each element in
{1,2,3} appears only once so there
is no majority element.

Example 2:

Input:
N = 5
A[] = {3,1,3,3,2}
Output:
3
Explanation:
Since, 3 is present more
than N/2 times, so it is
the majority element.


Your Task:
The task is to complete the function majorityElement() which returns the majority element in the array.
 If no majority exists, return -1.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).


Constraints:
1 ≤ N ≤ 107
0 ≤ Ai ≤ 106



'''
from collections import Counter

class Solution:
    def majorityElement(self,A,N):

        d=dict(Counter(A))
        print(d)
        val=list(d.values())
        keys=list(d.keys())
        print(val,keys)
        for i in range(len(val)):
            if val[i]>N//2:
                return keys[i]
        else:
            return -1

if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # N=int(input())
        # A=[int(x) for x in input().strip().split()]
        N=5
        A=[3,1,3,3,2]
        # N=3
        # A=[1,2,3]
        # N=2
        # A=[1,13]
        obj=Solution()
        print(obj.majorityElement(A,N))

        T-=1
