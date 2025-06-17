'''
Subset Sums

Given a list arr of N integers, print sums of all subsets in it.

Example 1:

Input:
N = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then
Sum = 2+3 = 5.

Example 2:

Input:
N = 3
arr = {5, 2, 1}
Output:
0 1 2 3 5 6 7 8

Your Task:
You don't need to read input or print anything.
Your task is to complete the function subsetSums() which takes a list/vector
and an integer N as an input parameter and return the list/vector of all the subset sums.

Expected Time Complexity: O(2N)
Expected Auxiliary Space: O(2N)

Constraints:
1 <= N <= 15
0 <= arr[i] <= 104

'''

class Solution:
    def solve(self,ind,arr,n,ans,sum):
        if(ind==n):
            ans.append(sum)
            return ans
        self.solve(ind+1,arr,n,ans,sum+arr[ind]) #Include
        self.solve(ind+1,arr,n,ans,sum) #Exclude
    def subsetSums(self,arr,n):
        ans=[]
        self.solve(0,arr,n,ans,0)
        return ans

if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # N=int(input())
        # arr=list(map(int,input().split()))
        # N=3
        # arr=[5,2,1]
        N=2
        arr=[2,3]
        ob=Solution()
        ans=ob.subsetSums(arr,N)
        ans.sort()
        for x in ans:
            print(x,end=' ')
        print()