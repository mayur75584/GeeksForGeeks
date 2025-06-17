'''
Is Binary Tree Heap

Given a binary tree. The task is to check whether the given tree follows the max heap property or not.
Note: Properties of a tree to be a max heap - Completeness and Value of node greater than or equal to its child.

Example 1:

Input:
      5
    /  \
   2    3
Output: 1
Explanation: The given tree follows max-heap property since 5,
is root and it is greater than both its children.

Example 2:

Input:
       10
     /   \
    20   30
  /   \
 40   60
Output: 0


Your Task:
You don't need to read input or print anything.
Your task is to complete the function isHeap()
which takes the root of Binary Tree as parameter returns True if
the given binary tree is a heap else returns False.

Expected Time Complexity: O(N)
Expected Space Complexity: O(N)

Constraints:
1 ≤ Number of nodes ≤ 100
1 ≤ Data of a node ≤ 1000


'''
class Solution:
    def isHeap(self,root):
        queue=[]
        queue.append(root)
        nullish=False
        while(len(queue)>0):
            node=queue[0]
            queue=queue[1:]
            if(node.left):
                if(nullish==True or node.left.data>node.data):
                    return False
                queue.append(node.left)
            else:
                nullish=True
            if(node.right):
                if(nullish==True or node.right.data>node.data):
                    return False
                queue.append(node.right)
            else:
                nullish=True
        return True

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
        # s='10 20 30 40 60'
        # s='5 2 3'
        # s='10 9 8 7 6 9 5'
        s='1000 950 946 46 38 39 N'
        root=buildTree(s)
        ob=Solution()
        if ob.isHeap(root):
            print(1)
        else:
            print(0)