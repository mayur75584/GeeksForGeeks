'Not able to clear all test cases'
class Solution:
    # def detectLoop(self,head):
    #     slow=head
    #     fast=head
    #     while(slow!=None and fast!=None and fast.next!=None):
    #         if(slow.next==fast.next.next):
    #             fast=fast.next.next
    #             return fast
    #     return None
    def removeLoop(self,head):
        # fast=self.detectLoop(head)
        # curr=head
        # ptr=slow
        # while(ptr.next!=curr.next):
        #     ptr=ptr.next
        #     curr=curr.next
        # ptr.next=None
        # slow=head
        # fast=head
        # while(slow!=None and fast!=None and fast.next!=None):
        #     if(slow.next==fast.next.next):
        #         break
        #     else:
        #         slow=slow.next
        #         fast=fast.next.next
        # fast=head
        # slow.next=None
        # return fast
        slow = fast = head
        flag = False
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if (fast == slow):
                flag = True
                break
        if flag == False:
            return False
        slow=head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return slow
        # curr = head
        # # while (curr):
        # ptr = slow
        # while (ptr.next != slow and ptr.next != curr):
        #     ptr = ptr.next
        #     curr=curr.next
        # if (ptr.next == curr):
        #     ptr.next = None
        #     return
        # curr = curr.next
        # if curr.next==slow.next:
        #     slow.next=None
        #     while(curr!=None):
        #         curr=curr.next
        #     return head
        # while(curr.next!=slow.next):
        #     slow=slow.next
        #     curr=curr.next
        # slow.next=None

        # slow=head
        # fast=head
        # while(slow!=None and fast!=None and fast.next!=None):
        #     slow = slow.next
        #     fast = fast.next.next
        #     if(slow==fast):
        #         break
        #
        # if(slow==fast):
        #     fast=head
        # else:
        #     return None
        #
        # while(slow.next!=fast.next):
        #     slow=slow.next
        #     fast=fast.next
        # slow.next=None
        # fast=fast.next


class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def add(self,num):
        if self.head is None:
            self.head=Node(num)
            self.tail=self.head
        else:
            self.tail.next=Node(num)
            self.tail=self.tail.next
    def isLoop(self):
        if self.head is None:
            return False
        fast=self.head.next
        slow=self.head

        while(slow!=fast):
            if fast is None or fast.next is None:
                return False
            fast=fast.next.next
            slow=slow.next
        return True
    def loopHere(self,position):
        if position==0:
            return
        walk=self.head
        for _ in range(1,position):
            walk=walk.next
        self.tail.next=walk
    def length(self):
        walk=self.head
        ret=0
        while(walk):
            ret+=1
            walk=walk.next
        return ret

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # pos=int(input())
        # n=5
        # arr=[1,2,3,4,5]
        # pos=2
        # n=3
        # arr=[1,3,4]
        # pos=2
        # n=5
        # arr=[7,58,36,34,16]
        # pos=1
        n=10
        arr=[62,20,37,80,14,14,69,71,56,47]
        pos=3
        ll=linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)

        Solution().removeLoop(ll.head)

        if ll.isLoop() or ll.length()!=n:
            print(0)
            continue
        else:
            print(1)
