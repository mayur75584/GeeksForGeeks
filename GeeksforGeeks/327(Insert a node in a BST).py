'''
Insert a node in a BST

Given a BST and a key K. If K is not present in the BST,
Insert a new Node with a value equal to K into the BST.
Note: If K is already present in the BST, don't modify the BST.


Example 1:

Input:
     2
   /   \
  1     3
K = 4
Output: 1 2 3 4
Explanation: After inserting the node 4
Inorder traversal will be 1 2 3 4.

Example 2:

Input:
        2
      /   \
     1     3
             \
              6
K = 4
Output: 1 2 3 4 6
Explanation: After inserting the node 4
Inorder traversal of the above tree
will be 1 2 3 4 6.


Your Task:
You don't need to read input or print anything.
Your task is to complete the function insert() which takes
the root of the BST and Key K as input parameters and
returns the root of the modified BST after inserting K.
Note: The generated output contains the inorder traversal of the modified tree.


Expected Time Complexity: O(Height of the BST).
Expected Auxiliary Space: O(Height of the BST).


Constraints:
1 <= Number of nodes <= 105
1 <= K <= 106

'''
def insert(root,Key):
    if root==None:
        root=Key
        return
    if root.data==Key:
        return
    if root.data>Key:
        if root.left:
            insert(root.left,Key)
        else:
            root.left=buildTree(str(Key))
    else:
        if root.right:
            insert(root.right,Key)
        else:
            root.right=buildTree(str(Key))

from collections import deque
class Node:
    def __init__(self,val):
        # self.data=val
        # self.left=None
        # self.right=None
        self.right=None
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

def inOrder(n):
    if n is None:
        return
    inOrder(n.left)
    print(n.data,end=' ')
    inOrder(n.right)

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # s=input()
        # s='2 1 3'
        s='2 1 3 N N N 6'
        root=buildTree(s)
        # k=int(input())
        k=4
        insert(root,k)
        inOrder(root)
        print()