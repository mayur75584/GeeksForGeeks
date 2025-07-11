'''
Minimum number of Coins

Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 }
and a target value N.
Find the minimum number of coins and/or notes needed to make the change for Rs N.
You must return the list containing the value of coins required.


Example 1:

Input: N = 43
Output: 20 20 2 1
Explaination:
Minimum number of coins and notes needed
to make 43.


Example 2:

Input: N = 1000
Output: 500 500
Explaination: minimum possible notes
is 2 notes of 500.


Your Task:
You do not need to read input or print anything.
Your task is to complete the function minPartition()
which takes the value N as input parameter and returns a list of integers in decreasing order.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 106

'''
class Solution:
    def minPartition(self,N):

        a=[1,2,5,10,20,50,100,200,500,2000]
        i=len(a)-1
        res=[]
        while(N>0):
            if(N>=a[i]):
                N=N-a[i]
                res.append(a[i])
            else:
                i-=1
        return res
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # N=43
        N=1000
        ob=Solution()
        arr=ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=' ')
        print()