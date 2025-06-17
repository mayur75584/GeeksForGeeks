'''
Fix errors
https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1?page=1&status[]=unsolved&category[]=Tree&sortBy=submissions
'''
'''
Update as:-
Left child, level-1 of parent
Right child, level+1 of parent

Using Level order traversal , queue and hash table

Algorithm:
1- Enqueue root
2- Update level for root as 0.
3- Add level=0 in Hash Table and root as the value.
4- While(queue is not empty):
    Dequeue and
    a) Check for left and right child and update level in hash table.
    b) Enqueue the left and right child.

'''

class Solution:
    def verticalOrder(self,root):
        if root is not None:
            dict1={}
            node_dict={} #for temporary storage
            queue=[]
            queue.append(root)
            node_dict[root.data]=0
            while(len(queue)>0):
                temp=[]
                curr=queue.pop(0)
                if curr is not None:
                    level=node_dict[curr.data]
                    if level in dict1:
                        temp=dict1.get(level)
                        temp.append(curr.data)
                    else:
                        temp.append(curr.data)
                        dict1[level]=temp

                    if curr.left is not None:
                        queue.append(curr.left)
                        node_dict[curr.left.data]=node_dict[curr.data]-1
                    if curr.right is not None:
                        queue.append(curr.right)
                        node_dict[curr.right.data]=node_dict[curr.data]+1
        else:
            return []
        # print(dict1)
        # min1=min(dict1.keys())
        # max1=max(dict1.keys())
        # print(min1,max1)
        # res=[]
        # for i in range(min1,max1+1):
        #     res.extend(dict1[i])
        # return res
        res=[]
        for j in sorted(dict1.keys()):
            res.extend(dict1.get(j))
        return res
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
    for i in range(t):
        # s=input()
        # s='1 2 3 4 5 6 7 N N N N N 8 N 9'
        s='1 2 3 4 5 N 6'
        root=buildTree(s)
        res=Solution().verticalOrder(root)
        for i in res:
            print(i,end=' ')
        print()
