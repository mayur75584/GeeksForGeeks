'''
Longest Common Prefix in an Array

Given a array of N strings, find the longest common prefix among all strings present in the array.


Example 1:

Input:
N = 4
arr[] = {geeksforgeeks, geeks, geek,
         geezer}
Output: gee
Explanation: "gee" is the longest common
prefix in all the given strings.

Example 2:

Input:
N = 2
arr[] = {hello, world}
Output: -1
Explanation: There's no common prefix
in the given strings.


Your Task:
You don't need to read input or print anything. Your task is to complete the function longestCommonPrefix() which takes the string array arr[] and its size N as inputs and returns the longest common prefix common in all the strings in the array. If there's no prefix common in all the strings, return "-1".


Expected Time Complexity: O(N*max(|arri|)).
Expected Auxiliary Space: O(max(|arri|)) for result.


Constraints:
1 ≤ N ≤ 103
1 ≤ |arri| ≤ 103
'''
class Solution:
    def longestCommonPrefix(self,arr,n):
        if n == 0:
            return -1
        if n == 1:
            return arr[0]
        a = sorted(arr)
        first = a[0]
        last = a[-1]
        leng = min(len(first), len(last))
        i = 0
        while (i < leng and first[i] == last[i]):
            i += 1
        x = first[:i]
        if len(x) > 0:
            return x
        else:
            return -1




if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=list(map(int,input().split()))

        ob=Solution()
        print(ob.longestCommonPrefix(arr,n))