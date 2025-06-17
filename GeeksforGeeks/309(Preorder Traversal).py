'''
Preorder Traversal

Given a binary tree, find its preorder traversal.

Example 1:

Input:
        1
      /
    4
  /    \
4       2
Output: 1 4 4 2

Example 2:

Input:
       6
     /   \
    3     2
     \   /
      1 2
Output: 6 3 1 2 2

Your Task:
You just have to complete the function preorder()
which takes the root node of the tree as input and
returns an array containing the preorder traversal of the tree.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 104
0 <= Data of a node <= 105

'''
def preorderUtil(root ,res):
    if root is None:
        return
    res.append(root.data)
    preorderUtil(root.left ,res)
    preorderUtil(root.right ,res)

def preOrder(root):

    # code here
    res =[]
    preorderUtil(root ,res)
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
    #Push the root to the queue
    q.append(root)
    size=size+1

    i=1
    while(size>0 and i<len(lst)):
        currNode=q[0]
        q.popleft()
        size=size-1

        currVal=lst[i]
        #if the left child is not null
        if(currVal!="N"):
            #create the left child for the current node
            currNode.left=Node(int(currVal))
            q.append(currNode.left)
            size=size+1

        #For right child
        i+=1
        if(i>=len(lst)):
            break
        currVal=lst[i]

        #if right child is not Null
        if(currVal!="N"):
            currNode.right=Node(int(currVal))

            q.append(currNode.right)
            size=size+1
        i+=1
    return root

if __name__ == '__main__':
    # t=int(input())
    t = 1
    for _ in range(t):
        # s=input()
        s = '1 4 N 4 2'
        root = buildTree(s)
        res = preOrder(root)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
