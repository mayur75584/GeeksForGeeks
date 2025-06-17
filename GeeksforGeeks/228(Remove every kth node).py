'''
Remove every k'th node

Given a singly linked list, your task is to remove every kth node from the linked list.

Input:
The first line of input contains number of test cases T. Then T test cases follow.
Every test case contains 3 lines. First line of every test case contains an integer N
denoting the size of the linked list . The second line contains N space separated values of the linked list.
The third line contains an integer K.

Output:
Output for each test case will be space separated values of the nodes of the new transformed linked list.

User Task:
The task is to complete the function deleteK() which should delete every kth nodes from the linked list.

Constraints:
1 <= T <= 50
1 <= N <= 100
1 <= element of linked list <= 1000
0 <= k <= 100

Example:
Input:
2
8
1 2 3 4 5 6 7 8
3
4
1 2 3 4
2

Output:
1 2 4 5 7 8
1 3

Explanation:
Testcase 1: After removing every 3rd element from the linked list,
we have updated list as 1, 2, 4, 5, 7 and 8, and the elements which
are removed are 3 and 6.
'''
def deleteK(head,k):
    if k==1:
        return None
    if k==0:
        return head
    count1=1
    n=head
    z=head
    count2=1
    while(z.next is not None):
        count2+=1
        z=z.next
    if head is None:
        return
    i=1
    while(i!=count2):
        if (count1+1)%k==0:
            if count1+1==count2:
                head.next=None
                break
            else:
                head.next=head.next.next
                count1+=1
                i+=1
        count1+=1
        head=head.next
        i+=1
    return n
class node:
    def __init__(self):
        self.data=None
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None

    def get_head(self):
        return self.head

    def insert(self,data):
        if self.head==None:
            self.head=node()
            self.head.data=data
        else:
            new_node=node()
            new_node.data=data
            new_node.next=None
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
def printlist(ptr):
    while(ptr!=None):
        print(ptr.data,end=' ')
        ptr=ptr.next


if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        llist=Linked_List()
        # n=int(input())
        # values=list(map(int,input().split()))
        # k=int(input())
        # n=8
        # values=[1,2,3,4,5,6,7,8]
        # k=3
        # n=4
        # values=[1,2,3,4]
        # k=2
        # n=5
        # values=[1,2,3,4,5]
        # k=1
        n=5
        values=[1,2,3,4,5]
        k=0
        for j in values:
            llist.insert(j)
        head=deleteK(llist.get_head(),k)
        printlist(head)
        print('')