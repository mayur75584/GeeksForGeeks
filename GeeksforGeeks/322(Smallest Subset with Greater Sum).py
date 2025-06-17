'''
Smallest Subset with Greater Sum

You are given an array Arr of size N containing non-negative integers.
Your task is to choose the minimum number of elements such that their
sum should be greater than the sum of the rest of the elements of the array.

Example 1:

Input:
N = 4
Arr[] = {2, 17, 7, 3}
Output:
1
Explanation:
If we only select element 17, the sum of the
rest of the elements will be (2+3+7)=12.
So the answer will be 1.

Example 2:

Input:
N = 4
Arr = {20, 12, 18, 4}
Output:
2
Explanation:
If we select 12 and 18 from the array,
the sum will be (12+18) = 30 and the sum of
the rest of the elements will be (20+4) = 24.
So, the answer will be 2. We can also
select 20 and 18 as well.



Your Task:

You don't need to read input or print anything.
Your task is to complete the function minSubset() which takes the array Arr[]
and its size N as inputs and returns the minimum number of elements to be selected.



Expected Time Complexity: O(N log N)
Expected Auxiliary Space: O(1)



Constraints:
1 <= N <= 105
1 <= Arr[i] <= 109
Array may contain duplicate elements.

'''

class Solution:
    def minSubset(self,A,N):
        sum1=sum(A)
        A.sort()
        sum2=0
        count1=0
        for i in range(N-1,-1,-1):
            sum2+=A[i]
            sum1-=A[i]
            count1+=1
            if(sum2>sum1):
                return count1
        return count1


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # A=list(map(int,input().split()))
        # N=4
        # A=[2,17,7,3]
        N=4
        A=[20,12,18,4]
        ob=Solution()
        ans=ob.minSubset(A,N)
        print(ans)