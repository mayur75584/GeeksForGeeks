'''
Alternate positive and negative numbers
Given an unsorted array Arr of N positive and negative numbers.
Your task is to create an array of alternate positive and negative
numbers without changing the relative order of positive and negative
 numbers.
Note: Array should start with positive number.


Example 1:

Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2

Example 2:

Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0


Your Task:
You don't need to read input or print anything. Your task is to complete the function rearrange() which takes the array of integers arr[] and n as parameters. You need to modify the array itself.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 107
-106 ≤ Arr[i] ≤ 107
'''

class Solution:
    def rearrange(self,arr,n):
        ev=[]
        od=[]
        for i in arr:
            if i>=0:
                ev.append(i)
            else:
                od.append(i)
        arr.clear()
        i=0
        j=0
        k=0
        n1=max(len(ev),len(od))
        while(k!=n1):
            if len(ev)==0:
                arr.append(od[j])
                od.pop(j)
            elif len(od)==0:
                arr.append(ev[i])
                ev.pop(i)
            else:
                arr.append(ev[i])
                arr.append(od[j])
                ev.pop(i)
                od.pop(j)
            k+=1

if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=9
        # arr=[9,4,-2,-1,5,0,-5,-3,2]
        n=10
        arr=[-5,-2,5,2,4,7,1,8,0,-8]
        ob=Solution()
        ob.rearrange(arr,n)
        for x in arr:
            print(x,end=' ')
        print()
        t-=1