'''
Equilibrium Point
Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array.
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
Example 1:
Input:
n = 5
A[] = {1,3,5,2,2}
Output: 3
Explanation: For second test case
equilibrium point is at position 3
as elements before it (1+3) =
elements after it (2+2).

Example 2:
Input:
n = 1
A[] = {1}
Output: 1
Explanation:
Since its the only element hence
its the only equilibrium point.

Your Task:
The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium.
Return -1 if no such point exists.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 <= n <= 106
1 <= A[i] <= 108
'''
class Solution:
    def equilibriumPoint(self,arr,N):
        if N==1:
            return arr[0]
        left=[]
        right=[]
        sum1=0
        sum2=0
        i=0
        j=len(arr)-1
        while(i!=len(arr) and j!=-1):
            sum1+=arr[i]
            left.append(sum1)
            sum2+=arr[j]
            right.append(sum2)

            i+=1
            j-=1
        right=right[::-1]
        print(left,right)

        for i in range(len(arr)):
            if i==0:
                pass
            elif i==len(arr)-1:
                pass
            else:
                if left[i-1]==right[i+1]:
                    return arr[i]
        return -1
if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # N=int(input())
        # A=list(map(int,input().split()))
        N=5
        A=[1,3,5,2,2]
        # N=1
        # A=[1]
        ob=Solution()
        print(ob.equilibriumPoint(A,N))

        T-=1






