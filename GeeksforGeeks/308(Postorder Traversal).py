'''
Postorder Traversal

Given a binary tree, find the Postorder Traversal of it.
For Example, the postorder traversal of the following tree is:
5 10 39 1

        1
     /     \
   10     39
  /
5



Example 1:

Input:
        19
     /     \
    10      8
  /    \
 11    13
Output: 11 13 10 8 19

Example 2:

Input:
          11
         /
       15
      /
     7
Output: 7 15 11

Your Task:
You don't need to read input or print anything.
Your task is to complete the function postOrder()
that takes root node as input and returns an array containing
the postorder traversal of the given Binary Tree.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 105
0 <= Data of a node <= 106
'''

def postOrderUtil(root,res):
    if root is None:
        return
    postOrderUtil(root.left,res)
    postOrderUtil(root.right,res)
    res.append(root.data)


def postOrder(root):
    res=[]
    postOrderUtil(root,res)
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
    t=1
    for _ in range(t):
        # s=input()
        s='19 10 8 11 13'
        root=buildTree(s)
        res=postOrder(root)
        for i in range(len(res)):
            print(res[i],end=" ")
        print()
