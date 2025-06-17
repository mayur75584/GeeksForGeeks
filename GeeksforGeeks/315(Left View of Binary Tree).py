'''
Left View of Binary Tree

Given a Binary Tree, print Left view of it.
Left view of a Binary Tree is set of nodes visible when tree is visited from Left side.
The task is to complete the function leftView(),
which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8

Example 1:

Input:
   1
 /  \
3    2
Output: 1 3

Example 2:

Input:
   10
 /   \
20   30
/ \
40 60
Output: 10 20 40

Your Task:
You just have to complete the function leftView()
that returns an array containing the nodes that are in the left view.
    The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
0 <= Number of nodes <= 100
1 <= Data of a node <= 1000

'''

def LeftView(root):

    if root is None:
        return []
    queue=[]
    queue.append(root)
    lst=[]
    while(len(queue)>0):
        n=len(queue)
        for i in range(1,n+1):
            tmp=queue[0]
            queue.pop(0)

            #Print the left most element at the level
            if(i==1):
                lst.append(tmp.data)

            #Add left node to queue
            if(tmp.left!=None):
                queue.append(tmp.left)
            #Add right node to queue
            if(tmp.right!=None):
                queue.append(tmp.right)
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
        # s='10 20 30 40 60'
        s='1 2 3 4 5 6 7 N 8'
        # s='1 3 2'
        # s='3 4 N 2 7 N 2 1 N 9 1' # 3 4 2 2 9
        # s='10 5 5 N 1 9 7 N 7 8 7' #10 5 1 7
        # s='4 5 2 N N 3 1 6 7' #4 5 3 6
        root=buildTree(s)
        result=LeftView(root)
        for value in result:
            print(value,end=' ')
        print()