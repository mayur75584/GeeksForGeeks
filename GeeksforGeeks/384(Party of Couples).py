'''
Party of Couples

You are given an integer array arr[] of size n, representing n number of people in a party, each person is denoted by an integer.
Couples are represented by the same number ie: two people have the same integer value, it means they are a couple.
Find out the only single person in the party of couples.

NOTE: It is guarantee that there exist only one single person in the party.

Example 1:

Input:
n = 5
arr = {1, 2, 3, 2, 1}
Output:
3
Explaination: Only the number 3 is single.
Example 2:

Input:
n = 11
arr = {1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6}
Output:
4
Explaination: 4 is the only single.
Your Task:
You do not need to read input or print anything. Your task is to complete the function findSingle() which takes the size of the array n and the array arr[] as input parameters and returns the only single person.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 104
1 ≤ arr[i] ≤ 106


'''
class Solution:
    def findSingle(self,n,arr):
        x=0
        for i in arr:
            x = x ^ i
        # The number remaining at the end will be the single number
        # which doesn't have it's pair to make it 0
        return x


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # arr=list(map(int,input().split()))
        # N=5
        # arr=[1,2,3,2,1]
        N=11
        arr=[1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6]
        ob=Solution()
        print(ob.findSingle(N,arr))