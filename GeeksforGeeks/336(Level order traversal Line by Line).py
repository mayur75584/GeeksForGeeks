'''
Level order traversal Line by Line

Given a Binary Tree, your task is to find its level order traversal.
For the below tree the output will be 1 $ 2 3 $ 4 5 6 7 $ 8 $.

          1
       /     \
     2        3
   /    \     /   \
  4     5   6    7
    \
     8

Example 1:

Input:
          1
        /
       4
     /   \
    4     2
Output:1 $ 4 $ 4 2 $

Example 2:

Input:
            10
          /    \
        20      30
     /     \
    40     60
Output: 10 $ 20 30 $ 40 60 $

Your Task:
This is a function problem. You don't need to read input.
Just complete the function levelOrder() that
takes nodes as parameter and returns level order traversal as a 2D list.

Note: The driver code prints the levels '$' separated.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of edges <= 1000
0 <= Data of a node <= 100

'''
def levelOrder(root):
    lst=[]
    x=[]
    if root is None:
        return [-1]
    q=[]
    q.append(root)
    q.append(None)
    lst.append([root.data])
    while(len(q)>0):
        node=q[0]
        q=q[1:]

        if node==None:
            if(len(x)!=0):
                lst.append(x)
                x=[]
        if(node!=None):
            if(node.left):
                q.append(node.left)
                x.append(node.left.data)
            if(node.right):
                q.append(node.right)
                x.append(node.right.data)
        elif(len(q)>0):
            q.append(None)
    return lst

from collections import deque
class Node:
    def __init__(self,val):
        self.right = None
        self.data=val
        self.left=None


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
        s='10 20 30 40 60'
        # s='1 4 N 4 2'
        root=buildTree(s)
        result=levelOrder(root)
        for values in result:
            for value in values:
                print(value,end=' ')
            print("$",end=' ')
        print()