'''
Power Of 2 and Subsequences

Given is an array A[] of size N.
Return the number of non-empty subsequences such that
the product of all numbers in the subsequence is Power of 2.
Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input:
N = 3
A[] = {1, 6, 2}
Output:
3
Explanation:
The subsequence that
can be chosen is {1},
{2} and {1,2}.

Example 2:

Input:
N = 3
A[] = {3, 5, 7}
Output:
0
Explanation:
No subsequences exist.

Your Task:

You don't need to read input or print anything.
Your task is to complete the function numberOfSubsequences()
which takes an integer N and an array A and returns the number of subsequences that exist.
As this number can be very large return the result under modulo 109+7.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= A[i] <= 109

'''

'''
First count the how many numbers are there in array who are in power of 2.
Then our answer will be 2**count of numbers from array who are power of 2 - 1.

for this we need to check which numbers are the power of 2 from the array.
Below is logic to check if a number is power of 2 or not.
So Binary Representation of 4 is 100
                            8 is 1000
                            2 is 10
if 4 &(Bitwise AND) 3 i.e 4&3 = 100
                                011 = 000 i.e 0
So for a number n if n&(n-1) == 0 then the number n is power of 2.

8&7 = 1000
      0111 = 0000 i.e 0 , So 8 is power of 2

'''
class Solution:
    def numberOfSubsequences(self,N,A):
        count1=0
        for i in A:
            if((i&(i-1))==0):
                count1+=1
        # ans=1
        # while(count1>0):
        #     ans=(ans*2)%((10**9)+7)
        #     count1-=1
        # return ans1-1
        'OR'
        return ((2**count1)-1)%((10**9)+7)

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # A=list(map(int,input().split()))
        # N=3
        # A=[1,6,2]
        N=3
        A=[3,5,7]
        ob=Solution()
        print(ob.numberOfSubsequences(N,A))
