'''
Level order traversal

Given a binary tree, find its level order traversal.
Level order traversal of a tree is breadth-first traversal for the tree.


Example 1:

Input:
    1
  /   \
 3     2
Output:1 3 2

Example 2:

Input:
        10
     /      \
    20       30
  /   \
 40   60
Output:10 20 30 40 60

Your Task:
You don't have to take any input.
Complete the function levelOrder() that takes the root node as
input parameter and returns a list of integers containing
the level order traversal of the given Binary Tree.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105

'''
'''
Method (Using queue)

Algorithm: For each node, first, the node is visited and then it’s child nodes are put in a FIFO queue. 

printLevelorder(tree)
1) Create an empty queue q
2) temp_node = root /*start from root*/
3) Loop while temp_node is not NULL
    a) print temp_node->data.
    b) Enqueue temp_node’s children 
      (first left then right children) to q
    c) Dequeue a node from q.
Implementation: Here is a simple implementation of the above algorithm. 
The queue is implemented using an array with a maximum size of 500. 
We can implement a queue as a linked list also. 
'''

class Solution:
    def levelOrder(self,root):
        if root is None:
            return [-1]
        queue=[]
        lst=[]
        queue.append(root)
        while(len(queue)>0):
            lst.append(queue[0].data)
            node=queue.pop(0)
            if(node.left is not None):
                queue.append(node.left)
            if(node.right is not None):
                queue.append(node.right)
        return lst

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
        # s='1 3 2'
        s='10 20 30 40 60'
        root=buildTree(s)
        res=Solution().levelOrder(root)
        for i in res:
            print(i,end=' ')
        print()
