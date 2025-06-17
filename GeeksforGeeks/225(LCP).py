'''
LCP

Geek is at the geek summer carnival. He is given an array of N strings.
To unlock exclusive course discounts he needs to find the longest common prefix
among all strings present in the array. Can you help him ?

Example 1:

Input:
N = 4
ar[] = {geeksforgeeks, geeks, geek, geezer}

Output:
gee

Explanation:
Longest common prefix in all the given string is gee.


Example 2:

Input:
N = 3
ar[] = {apple, ape, april}

Output:
ap


Your Task:
You don't need to read input or print anything.
Complete the function LCP() that takes integer n and ar[] as input parameters
and return the LCP (in case there is no common prefix return -1).


Expected time complexity: O(NlogN)
Expected space complexity: O(string length)

Constraints:
1 <= N <= 10^3
1 <= String Length <= 100
'''
class Solution:
    def LCP(self,arr,n):
        arr.sort()
        # print(arr)
        a = arr[0]
        b = arr[-1]
        s1 = ''
        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 0:
            return -1
        elif len(list(set(arr))) == 1:
            return arr[0]
        else:
            i = 0
            leng = min(len(a), len(b))
            while (i < leng and a[i] == b[i]):
                s1 += a[i]
                i += 1
            if s1 == '':
                return -1
            else:
                return s1

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=[x for x in input().split()]
        # n=4
        # arr=["geeksforgeeks","geeks","geek","geezer"]
        # n=3
        # arr=["apple","ape","april"]
        # n=3
        # arr=["a","b","c"]
        n=4
        arr=["a","a","a","a"]
        obj=Solution()
        print(obj.LCP(arr,n))