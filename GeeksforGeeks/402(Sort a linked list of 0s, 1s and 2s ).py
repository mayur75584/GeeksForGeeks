'''
Sort a linked list of 0s, 1s and 2s

Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only. Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.

Examples:

Input: head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2

Output: 0 → 1 → 1 → 2 → 2 → 2 → 2 → 2

Explanation: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between.
Input: head = 2 → 2 → 0 → 1

Output: 0 → 1 → 2 → 2

Explanation: After arranging all the 0s, 1s and 2s in the given format, the output will be 0 → 1 → 2 → 2.
Constraints:
1 ≤ no. of nodes ≤ 106
0 ≤ node->data ≤ 2

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
'''

class Solution:
    def segregate(self,head):
        count1=0
        count2=0
        count3=0
        while(head is not None):
            # print(head.data)
            if head.data==0:
                count1+=1
            elif head.data==1:
                count2+=1
            elif head.data==2:
                count3+=1
            head=head.next
        print(count1,count2,count3)
        # sum1=count1+count2+count3
        arr0=[0]*count1
        arr1=[1]*count2
        arr2=[2]*count3
        arr0.extend(arr1)
        arr0.extend(arr2)
        # print(arr0)
        head=None
        if arr0:
            head=Node(arr0[0])
            tail=head
            for value in arr0[1:]:
                tail.next = Node(value)
                tail = tail.next
        return head


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printList(node):
    while node:
        print(node.data,end=" ")
        node=node.next
    print()


if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # arr=list(map(int,input().split()))
        arr=[1,2,2,1,2,0,2,2]
        head=None
        if arr:
            head=Node(arr[0])
            tail=head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next
        printList(Solution().segregate(head))
        t-=1
