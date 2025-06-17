
'''
Apporach

First index value we will be adding +k only and last index value will be adding -k.

So we want to find minimum difference between smallest and largest tower, so
for smallest we will check minimum between first index value i.e 0th index + k, and rest index value ith index -k.
And for largest we will check maximum between last index value i.e n-1th index -k and rest index value i.e i-1th index +1.

So we will take difference between largest and smallest and find out the minimum difference.
'''

'''
Minimize the Heights I
Difficulty: MediumAccuracy: 26.16%Submissions: 86K+Points: 4
Given a positive integer k and an array arr[] denoting heights of towers, 
you have to modify the height of each tower either by increasing or decreasing them by k only once.
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.

Note: A slight modification of the problem can be found here. 

Examples:

Input: k = 2, arr[] = [1, 5, 8, 10]
Output: 5
Explanation: The array can be modified as [3, 3, 6, 8]. The difference between the largest and the smallest is 8 - 3 = 5.
Input: k = 3, arr[] = [3, 9, 12, 16, 20]
Output: 11
Explanation: The array can be modified as [6, 12, 9, 13, 17]. The difference between the largest and the smallest is 17 - 6 = 11. 
Constraints
1 ≤ k ≤ 104
1 ≤ number of towers ≤ 105
0 ≤ arr[i] ≤ 105
'''
class Solution:
    def getMinDiff(self,k,arr):
        arr.sort()
        print(arr)
        n=len(arr)
        min_res=arr[n-1]-arr[0]
        print(min_res)
        for i in range(1,n):
            min1=min(arr[0]+k,arr[i]-k)
            max1=max(arr[n-1]-k,arr[i-1]+k)
            # print(max1-min1)
            min_res=min(min_res,max1-min1)
            # print(min_res)
        return min_res
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # k=int(input())
        # arr=list(map(int,input().split()))
        # k=80
        # arr=[-70,-59,83,16,61,19]
        # k=2
        # arr=[1,5,8,10]
        k=3
        arr=[3,9,12,16,20]
        solution=Solution()
        res=solution.getMinDiff(k,arr)
        print(res)
        print("~")