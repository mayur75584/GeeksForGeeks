'''
Max and min element in Binary Tree

Given a Binary Tree, find maximum and minimum elements in it.

Example 1:

      2
    /   \
   7     5
    \      \
    6       9
    / \     /
    1  11   4
Input:

Output: 11 1
Explanation:
 The maximum and minimum element in
this binary tree is 11 and 1 respectively.

Example 2:

Input:
           6
        / \
       5   8
      /
     2
Output: 8 2

Your Task:
You don't need to read input or print anything.
Your task is to complete findMax() and findMin() functions
which take root node of the tree as input parameter and
return the maximum and minimum elements in the binary tree respectively.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105

'''
class Solution:
    def findMax(self,root):
        # print(root.data)
        current=root
        while(current.right):
            current=current.right
        return current.data
    def findMin(self,root):
        # print(root.data)
        current1=root
        while(current1.left):
            current1=current1.left
        return current1.data

from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def buildTree(s):
    if len(s)==0 or s[0]=="N":
        return None
    lst=list(map(str,s.split()))

    root=Node(int(lst[0]))
    size=0
    q=deque()

    q.append(root)
    size=size+1

    i=1
    while(size>0 and i<len(lst)):
        currNode=q[0]
        q.popleft()
        size=size-1

        currVal=lst[i]

        if(currVal!="N"):
            currNode.left=Node(int(currVal))
            q.append(currNode.left)
            size=size+1

        i+=1
        if(i>=len(lst)):
            break
        currVal=lst[i]

        if(currVal!="N"):
            currNode.right=Node(int(currVal))
            q.append(currNode.right)
            size=size+1
        i+=1
    return root

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # s=input()
        s='6 5 8 2'
        root=buildTree(s)
        ob=Solution()
        mx=ob.findMax(root)
        mn=ob.findMin(root)
        print(mx,mn)