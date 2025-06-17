'''
Occurence of an integer in a Linked List

Given a singly linked list and a key, count the number of occurrences of given
key in the linked list.

Example 1:

Input:
N = 7
Link List = 1->2->1->2->1->3->1
search_for = 1
Output: 4
Explanation:1 appears 4 times.

Example 2:

Input:
N = 5
Link List = 1->2->1->2->1
search_for = 3
Output: 0
Explanation:3 appears 0 times.

Your Task:
You dont need to read input or print anything. Complete the function count() which
takes the head of the link list and search_for i.e- the key as input parameters
and returns the count of occurrences of the given key.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
0 ≤ N ≤ 10^4
'''
class Solution:
    def count(self,head,search_for):
        n=head
        if(n==None):
            return -1
        else:
            count1=0
            while(n is not None):
                if n.data==search_for:
                    count1+=1
                n=n.next
            return count1
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
        print()

if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        llist=LinkedList()
        # n=int(input())
        # values=list(map(int,input().split()))
        # m=int(input())
        # n=7
        # values=[1,2,1,2,1,3,1]
        # m=1
        n=5
        values=[1,2,1,2,1]
        m=3
        for i in reversed(values):
            llist.push(i)
        # llist.printList()
        k=Solution().count(llist.head,m)
        print(k)
        t-=1



