'https://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list/#:~:text=Given%20a%20singly%20linked%20list,function%20to%20swap%20elements%20pairwise.&text=For%20example%2C%20if%20the%20linked,function%20should%20change%20it%20to.'
'https://practice.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1#'
class Solution:
    def pairWiseSwap(self,head):
        temp=head
        if temp is None:
            return
        # Traverse furthethr only if there are at least two
        # left
        while(temp and temp.next):
            # If both nodes are same,
            # no need to swap data
            if(temp.data!=temp.next.data):
                # Swap data of node with its next node's data
                temp.data,temp.next.data=temp.next.data,temp.data
            # Move temp by 2 to the next pair
            temp=temp.next.next
        return head
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,val):
        if self.head is None:
            self.head=Node(val)
            self.tail=self.head
        else:
            self.tail.next=Node(val)
            self.tail=self.tail.next
def printList(n):
    while(n):
        print(n.data,end=' ')
        n=n.next
    print()

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=8
        arr=[1,2,2,4,5,6,7,8]

        lis=LinkedList()
        for i in arr:
            lis.insert(i)
        dict1={}
        temp=lis.head
        while(temp):
            dict1[temp]=temp.data
            temp=temp.next
        failure=LinkedList()
        failure.insert(-1)
        head=Solution().pairWiseSwap(lis.head)
        temp=head
        f=0
        while(temp):
            if(dict1[temp]!=temp.data):
                f=1
            temp=temp.next
        if(f):
            print(-1)
        else:
            printList(head)