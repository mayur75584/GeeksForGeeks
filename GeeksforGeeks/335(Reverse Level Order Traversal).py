'''
Reverse Level Order Traversal

Given a binary tree of size N, find its reverse level order traversal.
ie- the traversal must begin from the last level.

Example 1:

Input :
        1
      /   \
     3     2

Output: 3 2 1
Explanation:
Traversing level 1 : 3 2
Traversing level 0 : 1

Example 2:

Input :
       10
      /  \
     20   30
    / \
   40  60

Output: 40 60 20 30 10
Explanation:
Traversing level 2 : 40 60
Traversing level 1 : 20 30
Traversing level 0 : 10


Your Task:
You dont need to read input or print anything.
Complete the function reverseLevelOrder()
which takes the root of the tree as input parameter and
returns a list containing the reverse level order traversal of the given tree.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 10^4

'''
def reverseLevelOrder(root):
    dict1={}
    depth=0
    q=[]
    if root is None:
        return [-1]
    q.append(root)
    q.append(None)
    # count1=1
    dict1[depth]=[root.data]
    x=[]
    while(len(q)>0):
        node=q[0]
        q=q[1:]

        if(node==None):
            depth+=1
            dict1[depth]=x
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
    print(dict1)
    lst=list(dict1.values())
    res=[]
    for i in range(len(lst)-1,-1,-1):
        res+=lst[i]
    return res

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
        # s='1 3 2'
        s='10 20 30 40 60'
        # s='10 20 30 40 50 60 70 80 90 100 110 120 130 140'
        root=buildTree(s)
        ans=reverseLevelOrder(root)
        for i in ans:
            print(i,end=' ')
        print()