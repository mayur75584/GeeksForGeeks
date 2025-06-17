'''
Delete a Node in Single Linked List

Given a singly linked list and an integer x.
Delete xth node from the singly linked list.

Example 1:

Input: 1 -> 3 -> 4
       x = 3
Output: 1 -> 3
Explanation:
After deleting the node at 3rd
position (1-base indexing), the
linked list is as 1 -> 3.

Example 2:

Input: 1 -> 5 -> 2 -> 9
x = 2
Output: 1 -> 2 -> 9
Explanation:
After deleting the node at 2nd
position (1-based indexing), the
linked list is as 1 -> 2 -> 9.


Your task: Your task is to complete the method deleteNode()
which takes two arguments: the address of the head of the linked list
and an integer x. The function returns the head of the modified linked list.

Constraints:
1 <= T <= 300
2 <= N <= 100
1 <= x <= N
'''
def delNode(head,k):
    count1=1

    if head is None:
        return -1
    if count1==k:
        head=head.next
        return head
    n=head

    while((n.next is not None)):
        if count1+1==k:
            break
        n=n.next
        count1+=1
    if n.next is None:
        return head
    else:
        n.next=n.next.next
        return head

class Node:
    def __init__(self):
        self.data=None
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None

    def insert(self,data):
        if self.head==None:
            self.head=Node()
            self.head.data=data
        else:
            new_node=Node()
            new_node.data=data
            new_node.next=None
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
def printlist(head):
    temp=head
    while(temp):
        print(temp.data,end=' ')
        temp=temp.next
    print('')
if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        list1=Linked_List()
        # n=int(input())
        # values=list(map(int,input().split()))
        # k=int(input())
        n=3
        values=[1,3,4]
        k=3
        # n=4
        # values=[1,5,2,9]
        # k=2
        for j in values:
            list1.insert(j)
        newhead=delNode(list1.head,k)
        printlist(newhead)