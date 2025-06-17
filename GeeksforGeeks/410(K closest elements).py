'''
K closest elements


You are given a sorted array arr[] of unique integers, an integer k, and a target value x.
Return exactly k elements from the array closest to x, excluding x if it exists.

An element a is closer to x than b if:


|a - x| < |b - x|, or
|a - x| == |b - x| and a > b (i.e., prefer the larger element if tied)


Return the k closest elements in order of closeness.

Examples:

Input: arr[] = [1, 3, 4, 10, 12], k = 2, x = 4
Output: 3 1
Explanation: 4 is excluded, Closest elements to 4 are: 3 (1), 1 (3). So, the 2 closest elements are: 3 1
Input: arr[] = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], k = 4, x = 35
Output: 39 30 42 45
Explanation: First closest element to 35 is 39.
Second closest element to 35 is 30.
Third closest element to 35 is 42.
And fourth closest element to 35 is 45.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ k ≤ arr.size()
1 ≤ x ≤ 106
1 ≤ arr[i] ≤ 106

Expected Complexities
Company Tags
AmazonOYO Rooms
'''


class Solution:
    def printKClosest(self,arr,k,x):
        dict1={}
        for i in arr:
            if i!=x:
                dict1[i]=abs(i-x)
        sorted_dict = sorted(dict1.items(),key=lambda x:(x[1],-x[0]))
        keys = [i[0] for i in sorted_dict]
        ans = keys[:k]
        return ans



if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # arr=list(map(int,input().split()))
        # k=int(input())
        # x=int(input())
        # arr=[14,15,22,54,58,75,112,114]
        # k=5
        # x=18
        # arr=[1,3,4,10,12]
        # k=2
        # x=4
        arr=[12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
        k=4
        x=35
        obj=Solution()
        ans=obj.printKClosest(arr,k,x)
        for i in ans:
            print(i,end=" ")
        print()
        t-=1