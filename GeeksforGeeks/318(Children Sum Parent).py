'''
Children Sum Parent

Given a Binary Tree. Check whether all of its nodes have the value equal
to the sum of their child nodes.


Example 1:

Input:
     10
    /
  10
Output: 1
Explanation: Here, every node is sum of
its left and right child.

Example 2:

Input:
       1
     /   \
    4     3
   /  \
  5    N
Output: 0
Explanation: Here, 1 is the root node
and 4, 3 are its child nodes. 4 + 3 =
7 which is not equal to the value of
root node. Hence, this tree does not
satisfy the given conditions.


Your Task:
You don't need to read input or print anything.
Your task is to complete the function isSumProperty() that takes
the root Node of the Binary Tree as input and returns 1 if all
the nodes in the tree satisfy the following properties. Else, it returns 0.
For every node, data value must be equal to the sum of
data values in left and right children. Consider data value as 0 for NULL child.
Also, leaves are considered to follow the property.


Expected Time Complexiy: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= N <= 105
1 <= Data on nodes <= 105

'''

class Solution:
    def isSumProperty(self,root):
        if root is None:
            return 0
        queue=[]
        queue.append(root)
        while(len(queue)>0):
            node=queue.pop(0)
            if node.left is not None or node.right is not None:
                x,y=0,0
                if node.left is not None:
                    x=node.left.data
                    queue.append(node.left)
                if node.right is not None:
                    y=node.right.data
                    queue.append(node.right)
                if x+y!=node.data:
                    return 0
        return 1


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
        # s='10 10'
        s='1 4 3 5 N'
        root=buildTree(s)
        ob=Solution()
        print(ob.isSumProperty(root))
