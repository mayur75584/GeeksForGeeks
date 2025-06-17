'''
Check for BST

Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.



Example 1:

Input:
   2
 /    \
1      3
Output: 1
Explanation:
The left subtree of root node contains node
with key lesser than the root nodes key and
the right subtree of root node contains node
with key greater than the root nodes key.
Hence, the tree is a BST.

Example 2:

Input:
  2
   \
    7
     \
      6
       \
        5
         \
          9
           \
            2
             \
              6
Output: 0
Explanation:
Since the node with value 7 has right subtree
nodes with keys less than 7, this is not a BST.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function isBST() which
takes the root of the tree as a parameter and
returns true if the given binary tree is BST, else returns false.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the BST).

Constraints:
0 <= Number of edges <= 100000

'''
class Solution:
    def isBST(self,root,l=None,r=None): #This l=None and r=None is done by me not predefined
        # An empty tee is BST
        if root==None:
            return True
        if(l!=None and root.data<=l.data):
            return False
        if(r!=None and root.data>=r.data):
            return False
        return self.isBST(root.left,l,root) and self.isBST(root.right,root,r)


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
        s='2 1 3'
        root=buildTree(s)
        if Solution().isBST(root):
            print(1)
        else:
            print(0)