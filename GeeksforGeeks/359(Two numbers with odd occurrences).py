'''
Two numbers with odd occurrences

Given an unsorted array, Arr[] of size N and that contains even number of occurrences
for all numbers except two numbers. Find the two numbers in decreasing order which has odd occurrences.

Example 1:

Input:
N = 8
Arr = {4, 2, 4, 5, 2, 3, 3, 1}
Output: {5, 1}
Explaination: 5 and 1 have odd occurrences.


Example 2:

Input:
N = 8
Arr = {1 7 5 7 5 4 7 4}
Output: {7, 1}
Explaination: 7 and 1 have odd occurrences.


Your Task:
You don't need to read input or print anything.
Your task is to complete the function twoOddNum() which takes the array Arr[]
and its size N as input parameters and returns the two numbers in decreasing order which have odd occurrences.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
2 ≤ N ≤ 106
1 ≤ Arri ≤ 1012

'''
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        dict1={}
        res=[0,0]
        for i in Arr:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        x,y=0,0
        count1=1
        for i,j in dict1.items():
            if(j%2!=0 and count1==1):
                x=i
                count1+=1
            elif(j%2!=0 and count1==2):
                y=i
                count1+=1
        print(x,y)
        if(x>=y):
            res[0]=x
            res[1]=y
        else:
            res[0]=y
            res[1]=x
        return res

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # Arr=list(map(int,input().split())
        N=42
        Arr=[34 ,52 ,45 ,15 ,23 ,23 ,22 ,22 ,34 ,52 ,15 ,9 ,34 ,23 ,22 ,43 ,9 ,23 ,23 ,23 ,23 ,45 ,9 ,34 ,22 ,22 ,22 ,52 ,34 ,23 ,34 ,43 ,23 ,23 ,34 ,22 ,22 ,9 ,52 ,43 ,27 ,34]
        ob=Solution()
        ans=ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
