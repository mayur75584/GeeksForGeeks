'''
Reverse a linked list

Given a linked list of N nodes. The task is to reverse this list.

Example 1:

Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list,
elements are 6->5->4->3->2->1.

Example 2:

Input:
LinkedList: 2->7->8->9->10
Output: 10 9 8 7 2
Explanation: After reversing the list,
elements are 10->9->8->7->2.

Your Task:
The task is to complete the function reverseList() with head reference
as the only argument and should return new head after reversing the list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 104
'''

class Solution:
    def reverseList(self,head):
        if head is None:
            return -1
        else:
            prev=None
            curr=head
            while(curr is not None):
                next1=curr.next
                curr.next=prev
                prev = curr
                curr = next1
            head=prev
            return head

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
def printList(head):
    temp=head
    while(temp):
        print(temp.data,end=' ')
        temp=temp.next
    print()


if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr=[int(x) for x in input().split()]
        n=6
        arr=[1,2,3,4,5,6]

        lis=Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().reverseList(lis.head)
        printList(newHead)