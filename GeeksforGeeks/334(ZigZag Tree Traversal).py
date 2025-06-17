'''
ZigZag Tree Traversal

Given a Binary Tree. Find the Zig-Zag Level Order Traversal of the Binary Tree.



Example 1:

Input:
        1
      /   \
     2     3
    / \   /  \
   4   5 6    7
Output:
1 3 2 4 5 6 7

Example 2:

Input:
           7
        /     \
       9       7
     /  \     /
    8    8   6
   /  \
  10   9
Output:
7 7 9 8 8 6 9 10



Your Task:
You don't need to read input or print anything.
Your task is to complete the function zigZagTraversal()
which takes the root node of the Binary Tree as its input and
returns a list containing the node values as they appear
in the Zig-Zag Level-Order Traversal of the Tree.



Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).



Constraints:
1 <= N <= 104
'''
class Solution:
    def zigzagTraversal(self,root):
        if root is None:
            return [-1]
        q=[]
        q.append(root)
        q.append(None)
        depth=0
        while(len(q)>0):
            node=q[0]
            q=q[1:]

            if(node==None):
                depth+=1
            if(node!=None):
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            elif(len(q)>0):
                q.append(None)
        queue = []
        lst = []
        count1 = 0
        queue.append(root)
        queue.append(None)
        count1 += 1
        lst.append(root.data)
        x = []
        dict1 = {1: [root.data]}
        while (len(queue) > 0):
            node=queue[0]
            queue=queue[1:]
            if(node==None):
                count1+=1
                if(count1%2!=0):
                    # lst+=x[::-1]
                    dict1[count1]=x[::-1]
                    x=[]
                else:
                    lst+=x
                    dict1[count1]=x
                    x=[]
                # count1+=1
            if (node != None and count1 % 2 == 0):
                a=None
                b=None
                if (node.right is not None):
                    queue.append(node.right)
                    a=node.right.data
                if (node.left is not None):
                    queue.append(node.left)
                    b=node.left.data
                # count1+=1
                if a!=None:
                    x.append(a)
                if b!=None:
                    x.append(b)
            elif (node != None and count1 % 2 != 0):
                c=None
                d=None
                if (node.right is not None):
                    queue.append(node.right)
                    c=node.right.data
                if (node.left is not None):
                    queue.append(node.left)
                    d=node.left.data
                # count1+=1
                if c!=None:
                    x.append(c)
                if d!=None:
                    x.append(d)
            elif(len(queue)>0):
                queue.append(None)
            # queue.pop(0)
            val=list(dict1.values())
            # print(val)
            if len(val)==depth:
                break
        print(dict1)
        val=list(dict1.values())
        print(val)
        ans=[]
        for i in val:
            ans+=i
        return ans

from collections import defaultdict
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
        s='1 2 3 4 5 6 7'
        # s='7 9 7 8 8 6 N 10 9'
        root=buildTree(s)
        ob=Solution()
        res=ob.zigzagTraversal(root)
        for i in range(len(res)):
            print(res[i],end=' ')
        print()