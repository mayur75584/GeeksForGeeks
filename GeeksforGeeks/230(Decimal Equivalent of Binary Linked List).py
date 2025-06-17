'''
Decimal Equivalent of Binary Linked List

Given a singly linked list of 0s and 1s, the task is to find its decimal equivalent.
Decimal Value of an empty linked list is considered as 0.

Since the answer can be very large, answer modulo 1000000007 should be printed.

Input:
First line of input contains number of testcases T. For each testcase,
first line of input contains

Output:
The function should return should decimal equivalent modulo 1000000007.

User Task:
The task is to complete the function decimalValue() which should find the
decimal value of the given binary value in the linked list.

Constraints:
1 <= T <= 200
0 <= N <= 100
Data of Node is either 0 or 1

Example:
Input:
2
3
0 1 1
4
1 1 1 0

Output:
3
14

Explanation:
Testcase 1: 1*20 + 1*21 + 0*22 =  1 + 2 + 0 = 3.
'''


def decimalValue(head):
    MOD=10**9+7
    sum1=0
    if head is None:
        return 0
    else:
        count1=1
        z=head
        while(z.next is not None):
            count1+=1
            z=z.next
        # return count1
        count1-=1
        n=head
        while(n is not None):
            sum1+=((n.data)*2**count1)
            count1-=1
            # print(n.data)
            n=n.next
        return sum1%MOD

class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head==None:
            self.head = node()
            self.head.data = data
        else:
            new_node=node()
            new_node.data=data
            new_node.next=None
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node


if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        list1=Linked_List()
        # n=int(input())
        # values=list(map(int,input().split()))
        # n=3
        # values=[0,1,1]
        n=4
        values=[1,1,1,0]
        for i in values:
            list1.insert(i)
        print(decimalValue(list1.head))
