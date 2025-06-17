'''
Rotate a Linked List
Given a singly linked list of size N. The task is to left-shift the linked list
by k nodes, where k is a given positive integer smaller than or equal to
length of the linked list.

Example 1:

Input:
N = 5
value[] = {2, 4, 7, 8, 9}
k = 3
Output: 8 9 2 4 7
Explanation:
Rotate 1: 4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

Example 2:

Input:
N = 8
value[] = {1, 2, 3, 4, 5, 6, 7, 8}
k = 4
Output: 5 6 7 8 1 2 3 4


Your Task:
You don't need to read input or print anything.
Your task is to complete the function rotate() which takes a head reference as
the first argument and k as the second argument,
and returns the head of the rotated linked list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 103
1 <= k <= N
'''
class Solution:
    def rotate(self,head,k):
        'Getting TLE for below solution'
        # k1=k
        # n=head
        # z=0
        # while(k!=0):
        #
        #     if not head:
        #         return
        #     temp=head
        #     z=head.data
        #     head=head.next
        #     temp=None
        #     new_node=Node(z)
        #     if not head:
        #         head=new_node
        #     else:
        #         n1=n
        #         while(n1.next is not None):
        #             n1=n1.next
        #         n1.next=new_node
        #     k-=1
        # while(k1!=0):
        #     n=n.next
        #     k1-=1
        # return n

        'Optimized Solution'
        '''
        To rotate a linked list by k, we can first make the linked list circular 
        and then moving k-1 steps forward from head node, 
        making (k-1)th node’s next to null and make kth node as head.
        '''
        if(k==0):
            return
        curr=head
        # Traverse till the end.
        while(curr.next!=None):
            curr=curr.next
        curr.next=head
        curr=head
        # Traverse the linked list to k-1
        # position which will be last element
        # for rotated array.
        for i in range(k-1):
            curr=curr.next
        # Update the head_ref and last
        # element pointer to None
        head=curr.next
        curr.next=None
        return head

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
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

def printList(n):
    while(n):
        print(n.data,end=' ')
        n=n.next
    print()

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr=[int(x) for x in input().split()]
        # k=int(input())
        n=5
        arr=[2,4,7,8,9]
        k=3

        # n=8
        # arr=[1,2,3,4,5,6,7,8]
        # k=4
        lis=LinkedList()
        for i in arr:
            lis.insert(i)
        head=Solution().rotate(lis.head,k)
        printList(head)
