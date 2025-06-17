'''
https://practice.geeksforgeeks.org/problems/level-order-traversal-line-by-line/1?page=2&category[]=Tree&sortBy=submissions

For Input:
7 5 3 6 2 N 1 11 11 6 13 N 6 6 12
Your Code's output is:
7 $ 3 $ 6 $ 2 $ 1 $ 11 $ 11 $ 6 $ 13 $ 6 $ 12 $
It's Correct output is:
7 $ 5 3 $ 6 2 1 $ 11 11 6 13 6 $ 6 12 $
Output Difference
7 $ 5 3 $ 6 $ 2 $ 1 $ 11 $11 116 13 6 $ 6 $ 13 $ 6 $ 12 $
'''
def levelOrder(root):
    if root is None:
        return [[-1]]
    queue=[]
    ans=[]
    queue.append(root)
    res=[]
    node=None
    flag=False
    while(len(queue)>0):
        if len(queue)==2:
            res.append(queue[0].data)
            node=queue.pop(0)
            flag=True
        elif(len(res)==1 and len(queue)<2 and flag==True):
            res.append(queue[0].data)
            ans.append(res)
            res=[]
            node=queue.pop(0)
            flag=False
        else:
            ans.append([queue[0].data])
            node=queue.pop(0)
        if(node.left is not None):
            queue.append(node.left)
        if(node.right is not None):
            queue.append(node.right)
    return ans

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
        # s='1 4 N 4 2'
        s='10 20 30 40 60 N N'
        root=buildTree(s)
        result=levelOrder(root)
        for values in result:
            for value in values:
                print(value,end=' ')
            print("$",end=' ')
        print()
