'''
Height of Binary Tree

Given a binary tree, find its height.


Example 1:

Input:
     1
    /  \
   2    3
Output: 2

Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3


Your Task:
You don't need to read input or print anything.
Your task is to complete the function height()
which takes root node of the tree as input parameter and
returns an integer denoting the height of the tree.
If the tree is empty, return 0.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105

'''
'''
Algorithm

1) Traverse the tree in level order traversal from root.
    1.1) Initialize an empty queue Q, a variable depth and push root into Q and
        push Null into Q.
    1.2) Run a while loop till Q is not empty.
        1.2.1) Store the front element of Q and pop out front element.
        1.2.2) If front of Q is Null then increment depth by one and if
               if queue is not empty then push Null into the q.
        1.2.3) Else if the element is not Null then check for its left and right children
               and if they are not Null push them into Q.
2) Return depth.
'''
class Solution:
    def height(self,root):
        if root is None:
            return -1
        depth=0
        q=[]

        # appending first level element along with None
        q.append(root)
        q.append(None)
        while(len(q)>0):
            node=q[0]
            q=q[1:]

            # When None encountered, increment the value
            if(node==None):
                depth+=1

            # If None not encountered, keep moving
            if(node!=None):
                if(node.left):
                    q.append(node.left)

                if(node.right):
                    q.append(node.right)
            # If queue still have elements left,
            # append None again to the queue.
            elif(len(q)>0):
                q.append(None)
        return depth


from collections import deque
class Node:
    def __init__(self,val):
        self.left=None
        self.data=val
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
        s='2 N 1 3'
        # s='1 2 3'
        root=buildTree(s)
        ob=Solution()
        print(ob.height(root))