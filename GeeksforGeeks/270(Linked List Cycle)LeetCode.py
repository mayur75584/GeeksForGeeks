'''
Linked List Cycle

Given head, the head of a linked list,
determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer. Internally,
pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.



Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.



Follow up: Can you solve it using O(1) (i.e. constant) memory?

'''

class Solution:
    def hasCycle(self,head):
        slow=head
        fast=head
        while(slow!=None and fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False

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

    def loopHere(self,pos):
        if pos==0:
            return
        walk=self.head
        for i in range(1,pos):
            walk=walk.next
        self.tail.next=walk

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=4
        # arr=[3,2,0,-4]
        # n=2
        # arr=[1,2]
        n=1
        arr=[1]
        LL=LinkedList()
        for i in arr:
            LL.insert(i)
        # pos=int(input())
        # pos=1
        # pos=0
        pos=-1
        LL.loopHere(pos)
        print(Solution().hasCycle(LL.head))