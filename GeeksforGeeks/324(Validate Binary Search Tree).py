'''
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.



Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.



Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1


'''
class Solution:
    def isValidBST(self,root,l=None,r=None): #This l=None and r=None is done by me not predefined
        if root==None:
            return True
        if(l!=None and root.data<=l.data):
            return False
        if(r!=None and root.data>=r.data):
            return False
        return self.isValidBST(root.left,l,root) and self.isValidBST(root.right,root,r)

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
        # s='2 1 3'
        s='5 1 4 N N 3 6'
        root=buildTree(s)
        if Solution().isValidBST(root):
            print('true')
        else:
            print('false')