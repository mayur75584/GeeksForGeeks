'''
Delete Middle of Linked List

Given a singly linked list, delete middle of the linked list.
For example, if given linked list is 1->2->3->4->5 then linked list
should be modified to 1->2->4->5.
If there are even nodes, then there would be two middle nodes,
we need to delete the second middle element. For example,
if given linked list is 1->2->3->4->5->6 then it should be
modified to 1->2->3->5->6.
If the input linked list is NULL or has 1 node, then it should return NULL

Example 1:

Input:
LinkedList: 1->2->3->4->5
Output: 1 2 4 5

Example 2:

Input:
LinkedList: 2->4->6->7->5->1
Output: 2 4 6 5 1

Your Task:
The task is to complete the function deleteMid() which should delete
the middle element from the linked list and return the head of the modified
linked list. If the linked list is empty then it should return NULL.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 1000
1 <= value <= 1000
'''
def deleteMid(head):
    n=head
    x=head
    count1=0
    if n.next==None:
        count1=1
    else:
        while(n is not None):
            count1+=1
            n=n.next
        print(count1)
        if count1%2==0:
            z=count1//2
            print(z)
        else:
            z=count1//2
            print(z)
        count2=1
        while(head.next is not None):
            if count2==z:
                head.next=head.next.next
                break
            count2+=1
            head=head.next
        return x

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Llist:
    def __init__(self):
        self.head = None
    def insert(self,data,tail):
        node=Node(data)

        if not self.head:
            self.head=node
            return node
        tail.next=node
        return node
def printList(head):
    while(head):
        print(head.data,end=' ')
        head=head.next
    print()

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr1=[int(x) for x in input().split()]
        n=5
        arr1=[1,2,3,4,5]
        # n=6
        # arr1=[2,4,6,7,5,1]
        ll=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll.insert(nodeData,tail)
        res=deleteMid(ll.head)
        printList(res)