'''
Delete N nodes after M nodes of a linked list

Given a linked list, delete N nodes after skipping M nodes of a linked list
until the last of the linked list.

Input:
First line of input contains number of testcases T. For each testcase,
first line of input contains number of elements in the linked list
and next M and N respectively space separated.
The last line contains the elements of the linked list.

Output:
Function should not print any output to stdin/console.

User Task:
The task is to complete the function linkdelete() which should modify
the linked list as required.

Example:
Input:
2
8
2 1
9 1 3 5 9 4 10 1
6
6 1
1 2 3 4 5 6

Output:
9 1 5 9 10 1
1 2 3 4 5 6

Explanation:
Testcase 1: Deleting one node after skipping the M nodes each time, we have list as 9-> 1-> 5-> 9-> 10-> 1.
'''

class Solution:
    def skipMdeleteN(self,head,M,N):
        n = head
        while (n):
            for i in range(1, M):
                if n is None:
                    return
                n = n.next
            if n is None:
                return
            t = n.next
            for i in range(1, N + 1):
                if t is None:
                    break
                t = t.next
            n.next = t
            n = t


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
        print("")

if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        llist=LinkedList()
        # n=int(input())
        # m,p=list(map(int,input().split()))
        # values=input().split()
        n=8
        # m,p=2,1
        m,p=1,1
        values=[9,1,3,5,9,4,10,1]
        for i in reversed(values):
            llist.push(i)
        Solution().skipMdeleteN(llist.head,m,p)
        llist.printList()
        t-=1