'''
Largest value in each level

Given a binary tree, find the largest value in each level.

Example 1:

Input :
        1
       / \
      2   3

Output : 1 3
Explanation :
There are two levels in the tree :
1. {1}, max = 1
2. {2, 3}, max = 3

Example 2:

Input :
        4
       / \
      9   2
     / \   \
    3   5   7

Output : 4 9 7
Explanation :
There are three levels in the tree:
1. {4}, max = 4
2. {9, 2}, max = 9
3. {3, 5, 7}, max=7

Your task :
You don't need to read input or print anything.
Your task is to complete the function largestValues()
which takes the root node of the tree as input and returns a vector containing the largest value in each level.

Expected Time Complexity : O(n) , where n = number of nodes
Expected Auxiliary Space : O(n) , where n = number of nodes

Constraints :
1 ≤ Number of nodes ≤ 10^5

'''
class Solution:
    def largestValues(self,root):
        'Getting TLE for below solution'
        # if root==None:
        #     return -1
        # q=[]
        # lst=[root.data]
        # q.append(root)
        # q.append(None)
        # depth=0
        # x=[]
        # while(len(q)>0):
        #     node=q[0]
        #     q=q[1:]
        #
        #     if(node==None):
        #         depth+=1
        #         if len(x)!=0:
        #             lst.append(max(x))
        #         x=[]
        #
        #     if(node!=None):
        #         if(node.left):
        #             q.append(node.left)
        #             x.append(node.left.data)
        #         if(node.right):
        #             q.append(node.right)
        #             x.append(node.right.data)
        #     elif(len(q)>0):
        #         q.append(None)
        # # print(lst)
        # return lst
        'Recursive Solution gives solution in correct time limit'
        res=[]
        self.helper(res,root,0)
        return res
    def helper(self,res,root,depth):

        if(not root):
            return

        if(depth==len(res)):
            res.append(root.data)
        else:
            #Storing largest value from each level
            res[depth]=max(res[depth],root.data)

        #Recursively traverse left and right subtree to find largest value from each level
        self.helper(res,root.left,depth+1)
        self.helper(res,root.right,depth+1)



from collections import deque
class Node:
    def __init__(self,val):
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


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # s=input()
        # s='4 9 2 3 5 N 7'
        s='1 2 3'
        root=buildTree(s)
        ob=Solution()

        ans=ob.largestValues(root)
        for key in ans:
            print(key,end=' ')
        print()