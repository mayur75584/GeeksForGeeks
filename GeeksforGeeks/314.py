'''
https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1?page=1&difficulty[]=0&difficulty[]=1&difficulty[]=2&status[]=unsolved&company[]=Amazon&sortBy=submissions
'''
'Getting TLE'
class Solution:
    def isIdentical(self,root1,root2):
        if root1==None or root2==None:
            return False
        queue1=[]
        queue2=[]
        lst1=[]
        lst2=[]
        queue1.append(root1)
        queue2.append(root2)
        flag=False
        if queue1[0].data!=queue2[0].data:
            return False
        while(len(queue1)>0 and len(queue2)>0):

            if list(set(queue1))==[None] and list(set(queue2))==[None]:
                break
            elif(list(set(queue1))==[None] or list(set(queue2))==[None]):
                flag=True
                break
            if queue1[0]!=None and queue2[0]!=None:
                lst1.append(queue1[0].data)
                lst2.append(queue2[0].data)
                node1=queue1.pop(0)
                node2=queue2.pop(0)
                print(node1.data,node2.data)

                if(lst1!=lst2):
                    return False
                else:
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                if(lst1!=lst2):
                    return False
                else:
                    queue1.append(node1.right)
                    queue2.append(node2.right)
            else:
                queue1.pop(0)
                queue2.pop(0)

        if flag==True:
            return False
        else:
            return True

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
        # s1=input()
        # s2=input()
        # s1='1 2 3'
        # s2='1 3 2'
        # s1='1 2 3'
        # s2='1 2 3'
        # s1='177'
        # s2='177 N 140 N 182 N 83'
        s1='7 334 337 374 237 301 150 13 281 164 229 23 158 330 256 154 365 242 23 111 331 26 56 134 319 172 330 20 186 N 131 19 303 125 5 11 348 242 383 8 161 332 222 309 208 197 48 114 196 28 257 280 380 333 282 328 232 161 298 N 189 139 246 380'
        s2='7 334 337 374 237 301 150 13 281 164 229 23 158 330 256 154 365 242 23 111 331 26 56 134 319 172 330 20 186 N 131 19 303 125 5 11 348 242 383 8 161 332 222 309 208 197 48 114 196 28 257 280 380 333 282 328 232 161 298 N 189 139 246 380'
        head1=buildTree(s1)
        head2=buildTree(s2)
        if Solution().isIdentical(head1,head2):
            print("Yes")
        else:
            print("No")