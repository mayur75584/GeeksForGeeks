'''
Convert an array to reduced form

Given an array with N distinct elements,
convert the given array to a reduced form where all elements are in range from 0 to N-1.
The order of elements is same, i.e., 0 is placed in place of smallest element, 1 is placed for second smallest element,
 … N-1 is placed for largest element.

Example 1:
Input:
N = 3
Arr[] = {10, 40, 20}
Output: 0 2 1
Explanation: 10 is the least element so it
is replaced by 0. 40 is the largest
element so it is replaced by 3-1 = 2. And
20 is the 2nd smallest element so it is
replaced by 1.

Example 2:
Input:
N = 5
Arr[] = {5, 10, 40, 30, 20}
Output: 0 1 4 3 2
Explanation: As 5 is smallest element,
it's replaced by 0. Then 10 is 2nd
smallest element, so it's replaced by 1.
Then 20 is 3rd smallest element, so it's
replaced by 2. And so on.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function convert() which takes the array of integers arr and n as parameters and
 returns an array of integers denoting the answer.

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 106
'''
class Solution:
    def convert(self,arr,n):
        z=[]
        z.extend(arr)
        print(z)
        l=arr.copy()
        # print(l)
        l.sort()
        dict={}
        for i in range(n):
            dict[l[i]]=i
        arr.clear()
        for j in range(n):
            arr.append(dict[z[j]])
if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=3
        arr=[10,40,20]

        ob=Solution()
        ob.convert(arr,n)
        for x in arr:
            print(x,end=' ')
        print()
        t-=1