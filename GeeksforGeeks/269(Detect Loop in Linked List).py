'''
Detect Loop in linked list

Given a linked list of N nodes.
The task is to check if the linked list has a loop.
Linked list can contain self loop.

Example 1:

Input:
N = 3
value[] = {1,3,4}
x(position at which tail is connected) = 2
Output: True
Explanation: In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop.

Example 2:

Input:
N = 4
value[] = {1,8,3,4}
x = 0
Output: False
Explanation: For N = 4 ,x = 0 means
then lastNode->next = NULL, then
the Linked list does not contains
any loop.

Your Task:
The task is to complete the function detectloop() which contains reference to the head as only argument.
This function should return true if linked list contains loop, else return false.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 104
1 ≤ Data on Node ≤ 103
'''
'''
Problem solution Explanation

slow pointer is moving only one step
and fast pointer is moving twice steps

so for 1,3,4

1st iteration
slow=slow.next i.e slow=3
fast=fast.next.next i.e fast=4

As at x=2 we have a loop so
2nd iteration
slow=slow.next i.e slow=4
fast=fast.next.next i.e fast =  4->3->4

As slow==fast i.e if if get slow and fast address same so it means there is a cycle
As here slow==fast it means there is a cycle or loop hence we written true
'''
class Solution:
    def detectLoop(self,head):
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
        # n=3
        # arr=[1,3,4]
        n=4
        arr=[1,8,3,4]
        LL=LinkedList()
        for i in arr:
            LL.insert(i)
        # x=int(input())
        # x=2
        x=0
        LL.loopHere(x)
        print(Solution().detectLoop(LL.head))