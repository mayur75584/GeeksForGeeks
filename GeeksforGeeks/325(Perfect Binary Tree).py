'''
Perfect Binary Tree

Given a Binary Tree, write a function to check whether the given Binary Tree is a prefect Binary Tree or not.
A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.

Example 1:

Input:
          7
      /  \
     4    9
Output: YES
Explanation:
As the root node 7 has two children and
two leaf nodes 4 and 9 are at same level
so it is a perfect binary tree.

Example 2:

Input:
                   7
              /   \
             3     8
           /   \     \
          2     5     10
        /
       1
Output: NO

Your task:

You don't need to read input or print anything.
Your task is to complete the function isPerfect() which takes root node of the tree
as input parameter and returns a boolean value.If the tree is a perfect binary tree return true other wise return false.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1<=T<=10^5
1<=N<=10^5
1<=data of node<=10^5

'''

class Solution:
    def findDepth(self,node):
        # Find depth and height
        d=0
        while(node!=None):
            d+=1
            node=node.left
        return d
    def perf(self,root,h,level=0):
        # An empty tree is perfect
        if root == None:
            return True

        # If leaf node, then its depth must be same as depth of all other leaves.
        if (root.left == None and root.right == None):
            return h==level+1
        # If internal node and one child is empty
        if (root.left == None or root.right == None):
            return False

        # Left and right subtree must be perfect
        return (self.perf(root.left,h, level + 1) and self.perf(root.right,h, level + 1))
    def isPerfect(self,root):
        h=self.findDepth(root)
        return self.perf(root,h)


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
    for i in range(t):
        # s=input()
        s='7 3 8 2 5 10 1 N N N N N N N N N'
        # s='7 4 1'
        root=buildTree(s)
        ob=Solution()
        res=ob.isPerfect(root)
        if res:
            print("YES")
        else:
            print("NO")