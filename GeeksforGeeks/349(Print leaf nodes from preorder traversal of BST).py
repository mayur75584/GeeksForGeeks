'''
Print leaf nodes from preorder traversal of BST

Given a preorder traversal of a BST, find the leaf nodes of the tree
without building the tree.


Example 1:

Input:
N = 2
arr = {2,1}
Output: {1}
Explaination: 1 is the only leaf node.


Example 2:

Input:
N = 3
Arr = {3, 2, 4}
Output: {2, 4}
Explaination: 2, 4 are the leaf nodes.


Your Task:
You don't need to read input or print anything.
Your task is to complete the function leafNodes() which takes
the array arr[] and its size N as input parameters
and returns the leaf nodes of the tree.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 103
1 ≤ arr[i] ≤ 103

'''
'''
Value greater than last, Last is a leaf node.
Lets say we have BST like
           8
          / \
         3   10
        / \    \
       1   6    14
          / \   /
         4  7   13
                  root   left       right
PreOrder traversal - 8 3 1 6 4 7  10 14 13
                       R L  Right  R
Here when we see 1,6
as 1<6 then 1 is a leaf node.
For 4,7 as 4<7
4 as leaf node.
For 7,10 as 7<10
7 as leaf node.
And n-1 i.e 13.

             890
            /   \
           325   965
           /  \
        290   530

'''

class Solution:
    def leafNodes(self,a,n):
        ans=[]
        stack=[]
        stack.append(a[0])
        for i in range(1,n):
            if(a[i]<stack[-1]):
                stack.append(a[i])
            else:
                #a[i]>stacl[-1] #stack top
                tmp=stack[-1]
                stack.pop(-1)
                if(len(stack)!=0 and a[i]>stack[-1]):
                    while(len(stack)!=0 and a[i]>stack[-1]):
                        stack.pop(-1)
                    ans.append(tmp)
                stack.append(a[i])
        ans.append(a[n-1])
        return ans

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # arr=list(map(int,input().split()))
        # N=3
        # arr=[3,2,4]
        # N=5
        # arr=[890,325,290,530,965] #290 530 965
        N=9
        arr=[8,3,1,6,4,7,10,14,13]
        ob=Solution()
        ans=ob.leafNodes(arr,N)
        for i in range(len(ans)):
            print(ans[i],end=' ')
        print()