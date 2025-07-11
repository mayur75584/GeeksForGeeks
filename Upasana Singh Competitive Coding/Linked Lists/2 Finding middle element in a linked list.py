'''
Finding middle element in a linked list

Given a singly linked list of N nodes.
The task is to find the middle of the linked list.
For example, if the linked list is
1-> 2->3->4->5, then the middle node of the list is 3.
If there are two middle nodes(in case, when N is even), print the second middle element.
For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.

Example 1:

Input:
LinkedList: 1->2->3->4->5
Output: 3
Explanation:
Middle of linked list is 3.

Example 2:

Input:
LinkedList: 2->4->6->7->5->1
Output: 7
Explanation:
Middle of linked list is 7.

Your Task:
The task is to complete the function getMiddle() which takes a head reference as the only argument
and should return the data at the middle node of the linked list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 5000
'''
class Solution:
    def findMid(self,head):
        z=head
        if z is None:
            return -1
        else:
            count1=1
            while(z.next is not None):
                count1+=1
                z=z.next
            if count1==1:
                return head.data
            if count1==2:
                return head.next.data
            x=0
            x=count1//2+1
            count2=1
            while(head.next is not None):
                if count2==x:
                    return head.data
                count2+=1
                head=head.next

class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next
def printlist(head):
    temp=head
    while(temp is not None):
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
        # n=5
        # values=[1,2,3,4,5]
        # n=6
        # values=[2,4,6,7,5,1]
        # n=1
        # values=[37]
        n=2
        values=[69,55]
        for i in values:
            list1.insert(i)
        ob=Solution()
        print(ob.findMid(list1.head))