'''
Sorting Elements of an Array by Frequency

Given an array of integers, sort the array according to frequency of elements.
That is elements that have higher frequency come first.
If frequencies of two elements are same, then smaller number comes first.

Example 1:
Input:
N = 5
A[] = {5,5,4,6,4}
Output: 4 4 5 5 6
Explanation: The highest frequency here is
2. Both 5 and 4 have that frequency. Now
since the frequencies are same then
smallerelement comes first. So 4 4 comes
firstthen comes 5 5. Finally comes 6.
The output is 4 4 5 5 6.

Example 2:
Input:
N = 5
A[] = {9,9,9,2,5}
Output: 9 9 9 2 5
Explanation: The highest frequency here is
3. The element 9 has the highest frequency
So 9 9 9 comes first. Now both 2 and 5
have same frequency. So we print smaller
element first.
The output is 9 9 9 2 5.

Your Task:
You only need to complete the function sortByFreq that takes arr,
and n as parameters and returns the sorted array.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 105
1 ≤ Ai ≤ 105
'''
class Solution:
    def sortByFreq(self,A,n):
        dict1 = {}
        for i in A:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        dict1 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        res = []
        ans = []
        f = dict1[0][1]
        for i in dict1:
            if f == i[1]:
                ans.extend([i[0]] * i[1])
            else:
                res.extend(sorted(ans))
                ans = []
                ans.extend([i[0]] * i[1])
                f = i[1]
        res.extend(sorted(ans))
        return res

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # a=list(map(int,input().split()))
        # n=5
        # a=[5,5,4,6,4]
        # n=5
        # a=[9,9,9,2,5]
        n=6
        a=[8,9,1,2,3,1]
        l=Solution().sortByFreq(a,n)
        print(*l)