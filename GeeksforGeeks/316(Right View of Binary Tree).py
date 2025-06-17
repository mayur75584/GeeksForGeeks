'''
Right View of Binary Tree

Given a Binary Tree, find Right view of it.
Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

Right view of following tree is 1 3 7 8.

          1
       /     \
     2        3
   /   \      /    \
  4     5   6    7
    \
     8

Example 1:

Input:
       1
    /    \
   3      2
Output: 1 2

Example 2:

Input:
     10
    /   \
  20     30
 /   \
40  60
Output: 10 30 60

Your Task:
Just complete the function rightView() that takes node as parameter
and returns the right view as a list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105

'''

class Solution:
    def rightView(self,root):

        if root is None:
            return []
        queue=[]
        lst=[]
        queue.append(root)
        while(len(queue)>0):
            n=len(queue)
            for i in range(n,0,-1):
                tmp=queue[0]
                queue.pop(0)

                if(i==n):
                    lst.append(tmp.data)
                if (tmp.right != None):
                    queue.append(tmp.right)

                if (tmp.left != None):
                    queue.append(tmp.left)

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
        # s='1 2 3 4 5 6 7 N 8'
        # s='1 3 2'
        s='10 20 30 40 60'
        root=buildTree(s)
        result=Solution().rightView(root)
        for value in result:
            print(value,end=' ')
        print()