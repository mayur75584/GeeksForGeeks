'''
Symmetric Tree

Given a Binary Tree. Check whether it is Symmetric or not, i.e.
whether the binary tree is a Mirror image of itself or not.

Example 1:

Input:
         5
       /   \
      1     1
     /       \
    2         2
Output: True
Explanation: Tree is mirror image of
itself i.e. tree is symmetric

Example 2:

Input:
         5
       /   \
      10     10
     /  \     \
    20  20     30
Output: False

Your Task:
You don't need to read input or print anything.
Your task is to complete the function isSymmetric()
which takes the root of the Binary Tree as its input and
returns True if the given Binary Tree is the same as the Mirror image of itself.
Else, it returns False.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
0<=Number of nodes<=100

'''
class Solution:
    def left1(self,queue1):
        res=[]
        while(len(queue1)>0):
            res.append(queue1[0].data)
            node=queue1.pop(0)
            if(node.right is not None):
                queue1.append(node.right)
            if(node.left is not None):
                queue1.append(node.left)
        return res
    def right1(self,queue2):
        res=[]
        while(len(queue2)>0):
            res.append(queue2[0].data)
            node=queue2.pop(0)
            if(node.left is not None):
                queue2.append(node.left)
            if(node.right is not None):
                queue2.append(node.right)
        return res
    def isSymmetric(self, root):
        # Your Code Here
        if root is None:
            return True
        queue1=[]
        queue2=[]
        if root.left is not None and root.right is None:
            return False
        if root.left is None and root.right is not None:
            return False
        if root.left is None and root.right is None:
            return True
        if root.left is not None:
            queue1.append(root.left)
        if root.right is not None:
            queue2.append(root.right)
        l=self.left1(queue1)
        r=self.right1(queue2)
        # print(l)
        # print(r)
        if l==r:
            return True
        else:
            return False

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
        # s='5 1 1 2 N N 2'
        # s='5 10 10 20 20 N 30'
        # s='42 8 8 4 10 10 4 6 4 8 5 5 8 4 6 7 N N N N N N N N N N N N N N 7'
        s=''
        root=buildTree(s)
        ob=Solution()
        if ob.isSymmetric(root):
            print("True")
        else:
            print("False")