'''
Count BST nodes that lie in a given range

Given a Binary Search Tree (BST) and a range l-h(inclusive),
count the number of nodes in the BST that lie in the given range.

    The values smaller than root go to the left side
    The values greater and equal to the root go to the right side

Example 1:

Input:
      10
     /  \
    5    50
   /    /  \
  1    40  100
l = 5, h = 45
Output: 3
Explanation: 5 10 40 are the node in the
range

Example 2:

Input:
     5
    /  \
   4    6
  /      \
 3        7
l = 2, h = 8
Output: 5
Explanation: All the nodes are in the
given range.

Your Task:
This is a function problem. You don't have to take input.
You are required to complete the function getCountOfNode() that takes root, l ,h
as parameters and returns the count.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1 <= Number of nodes <= 100
1 <= l < h < 103

'''
class Solution:
    def getCount(self,root,l,h):
        ##Your code here
        count1=0
        if root is None:
            return 0
        q=[]
        lst=[]
        q.append(root)
        while(len(q)>0):
            lst.append(q[0].data)
            node=q.pop(0)
            if l<=node.data<=h:
                count1+=1
            if(node.left is not None):
                q.append(node.left)
            if(node.right is not None):
                q.append(node.right)
        return count1


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
        s='5 4 6 3 N N 7 1'
        root=buildTree(s)
        # l,r=map(int,input().split())
        l,r=1,5
        obj=Solution()
        print(obj.getCount(root,l,r))

