'''
Move Last Element to Front of a Linked List

You are given the head of a Linked List.
You have to move the last element to the front of the Linked List
and return the list.


Example 1:

Input:
N = 5
List = {2,5,6,2,1}
Output:
{1,2,5,6,2}
Explanation:
In the given linked list, the last element is 1,
after moving the last element to the front the
linked list will be {1,2,5,6,2}.



Example 2:

Input:
N = 1
List = {2}
Output:
{2}
Explanation:
Here 2 is the only element so, the linked list
will remain the same.



Your Task:

You don't need to read input or print anything.
Your task is to complete the function moveToFront() which takes
the address of the head of the linked list and returns the modified linked list.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 105
0 <= Elements of List <= 109
Sum of N over all test cases doesn't exceeds 106
'''
class Solution:
    def moveToFront(self,head):
        temp=head
        if temp.data is None:
            return -1
        elif temp.next is None:
            return head
        else:
            n=head
            while(n.next.next is not None):
                n=n.next
            z=n.next.data
            n.next=None
            new_node=Node(z)
            new_node.next=head
            head=new_node
            return head

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def printList(node):
    while(node!=None):
        print(node.data,end=' ')
        node=node.next
    print()

def inputList():
    # n=int(input())
    # data=[int(i) for i in input().split()]
    # n=3
    # data=[3,5,4]
    # n=5
    # data=[2,5,6,2,1]
    n=1
    data=[2]
    head=Node(data[0])
    tail=head
    for i in range(1,n):
        tail.next=Node(data[i])
        tail=tail.next
    return head

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        head=inputList()

        obj=Solution()
        res=obj.moveToFront(head)

        printList(res)