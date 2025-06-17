'''
Minimum sum

Given an array Arr of size N such that each element is from the range 0 to 9.
Find the minimum possible sum of two numbers formed using the elements of the array.
All digits in the given array must be used to form the two numbers.

Example 1:
Input:
N = 6
Arr[] = {6, 8, 4, 5, 2, 3}
Output: 604
Explanation: The minimum sum is formed
by numbers 358 and 246.

Example 2:
Input:
N = 5
Arr[] = {5, 3, 0, 7, 4}
Output: 82
Explanation: The minimum sum is
formed by numbers 35 and 047.


Your Task:
You don't need to read input or print anything.
Your task is to complete the function solve() which takes arr[] and n as input parameters and returns the minimum possible sum.
As the number can be large, return string presentation of the number without leading zeroes.

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 107
0 ≤ Arri ≤ 9
'''

class Solution:
    def solve(self,arr,n):
        res=''
        res1=''
        arr.sort()
        print(arr)
        if len(arr)==1:
            return arr[0]
        for i in range(len(arr)):
            if i%2==0:
                res+=str(arr[i])
            else:
                res1+=str(arr[i])
        print(res,res1)
        return int(res)+int(res1)
if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=5
        # arr=[5,3,0,7,4]
        n=1 #Exceptional Test Case
        arr=[1]
        # n=6
        # arr=[6,8,4,5,2,3]
        ob=Solution()
        ans=ob.solve(arr,n)
        print(ans)

        t-=1