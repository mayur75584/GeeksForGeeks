'''
Level order traversal in spiral form

Complete the function to find spiral order traversal of a tree.
For below tree, function should return 1, 2, 3, 4, 5, 6, 7.
                            1
                          /  \
                         2    3
                        / \   / \
                       7   6  5  4

Example 1:

Input:
      1
    /   \
   3     2
Output:1 3 2

Example 2:

Input:
           10
         /     \
        20     30
      /    \
    40     60
Output: 10 20 30 60 40

Your Task:
The task is to complete the function findSpiral()
which takes root node as input parameter and
returns the elements in spiral form of level order traversal as a list.
The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
0 <= Number of nodes <= 105
0 <= Data of a node <= 105

'''
def findSpiral(root):
    if root==None:
        return []
    q=[]
    dict1={}
    count1=0
    dict1[count1]=[root.data]
    q.append(root)
    q.append(None)
    x=[]
    while(len(q)>0):
        node=q[0]
        if(node!=None):
            x.append(node.data)
        q=q[1:]
        if(node==None):
            if(count1%2==0):
                x=x[::-1]
                dict1[count1]=x
                x=[]
            else:
                dict1[count1]=x
                x=[]
            count1+=1
        if(node!=None):
            if(node.left):
                q.append(node.left)
                # x.append(node.left.data)
            if(node.right):
                q.append(node.right)
                # x.append(node.right.data)
        elif(len(q)>0):
            q.append(None)
    # print(dict1)
    val=list(dict1.values())
    res=[]
    for i in val:
        res+=i
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
        # s='1 2 3 7 6 5 4'
        s='10 20 30 40 60'
        root=buildTree(s)
        result=findSpiral(root)
        for value in result:
            print(value,end=' ')
        print()