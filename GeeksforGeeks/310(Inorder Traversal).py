'''
Inorder Traversal

Given a Binary Tree, find the In-Order Traversal of it.

Example 1:

Input:
       1
     /  \
    3    2
Output: 3 1 2

Example 2:

Input:
        10
     /      \
    20       30
  /    \    /
 40    60  50
Output: 40 20 60 10 50 30

Your Task:
You don't need to read input or print anything.
Your task is to complete the function inOrder()
that takes root node of the tree as input and
returns a list containing the In-Order Traversal of the given Binary Tree.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 105
0 <= Data of a node <= 105
'''
class Solution:
    def InOrderUtil(self,root,res):
        if root is None:
            return
        self.InOrderUtil(root.left,res)
        res.append(root.data)
        self.InOrderUtil(root.right,res)
    def InOrder(self,root):
        res=[]
        self.InOrderUtil(root,res)
        return res

from collections import deque
class Node:
    def __init__(self,val):
        self.right=None
        self.data=val
        self.left=None
def buildTree(s):
    if(len(s)==0 or s[0]=="N"):
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
        if(i>len(lst)):
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
        s='1 3 2'
        root=buildTree(s)
        res=Solution().InOrder(root)
        for i in range(len(res)):
            print(res[i],end=' ')
        print()