'''
Nth node from end of linked list

Given a linked list consisting of L nodes and given a number N.
The task is to find the Nth node from the end of the linked list.

Example 1:

Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output: 8
Explanation: In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end os 8.

Example 2:

Input:
N = 5
LinkedList: 10->5->100->5
Output: -1
Explanation: In the second example, there
are 4 nodes in the linked list and we
need to find 5th from the end. Since 'n'
is more than the number of nodes in the
linked list, the output is -1.

Your Task:
The task is to complete the function getNthFromLast() which takes two arguments:
reference to head and N and you need to return Nth from the end or -1 in case node doesn't exist..

Note:
Try to solve in single traversal.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= L <= 106
1 <= N <= 106
'''
def getNthFromLast(head,n):
    count1=1
    z=head
    if z is None:
        return -1
    else:
        while(z.next is not None):
            count1+=1
            z=z.next
        # print(count1)
        x=(count1-n)+1
        if x<=0:
            return -1
        else:
            count2=1
            while(head is not None):
                if count2==x:
                    return head.data
                count2+=1
                head=head.next


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n,nth_node=map(int,input().split())
        a=LinkedList()
        # nodes_a=list(map(int,input().split()))
        n,nth_node=9,2
        nodes_a=[1,2,3,4,5,6,7,8,9]
        # n,nth_node=4,5
        # nodes_a=[10,5,100,5]
        for x in nodes_a:
            a.append(x)
        print(getNthFromLast(a.head,nth_node))