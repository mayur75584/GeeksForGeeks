'''
Two Repeated Elements

You are given an array of N+2 integer elements.
All elements of the array are in range 1 to N. Also,
all elements occur once except two numbers which occur twice.
Find the two repeating numbers.

Example 1:
Input:
N = 4
array[] = {1,2,1,3,4,3}
Output: 1 3
Explanation: In the given array,
1 and 3 are repeated two times.

Example 2:
Input:
N = 2
array[] = {1,2,2,1}
Output: 2 1
Explanation: In the given array,
1 and 2 are repeated two times
and second occurence of 2 comes
before 1. So the output is 2 1.

Your Task:
The task is to complete the function repeatedElements()
which takes array arr[] and an integer N as inputs
(the size of the array is N + 2 and elements are in range[1, N])
and finds the two repeated element in the array and return them in a list.
Note: Return the numbers in their order of appearing twice.
So, if X and Y are the repeating numbers,
and X repeats twice before Y repeating twice, then the order should be (X,Y).

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
2 ≤ N ≤ 105
1 ≤ array[i] ≤ N
'''
class Solution:
    def twoRepeated(self,arr,N):
        c1=0
        c2=0
        z=[0]*(N+1)
        res=[]
        for i in range(len(arr)):
            x=arr[i]
            z[x]+=1
            if z[x]==2:
                res.append(x)
                if c1==0:
                    c1=i
                elif c2==0:
                    c2=i
        print(res,c1,c2)
        ans=[]
        if c1<=c2:
            ans.append(res[0])
            ans.append(res[1])
        else:
            ans.append(res[1])
            ans.append(res[0])
        return ans

if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # N=int(input())
        # A=list(map(int,input().split()))
        # N=2
        # A=[1,2,2,1]
        N=4
        A=[1,2,1,3,4,3]
        obj=Solution()
        ans=obj.twoRepeated(A,N)
        print(ans[0],ans[1])
        T-=1