'''
Get minimum element from stack

You are given N elements and your task is to Implement a Stack in
which you can get minimum element in O(1) time.

Example 1:

Input:
push(2)
push(3)
pop()
getMin()
push(1)
getMin()
Output: 3 2 1
Explanation: In the first test case for
query
push(2)  the stack will be {2}
push(3)  the stack will be {2 3}
pop()    poped element will be 3 the
         stack will be {2}
getMin() min element will be 2
push(1)  the stack will be {2 1}
getMin() min element will be 1

Your Task:
You are required to complete the three methods push() which take
one argument an integer 'x' to be pushed into the stack,
pop() which returns a integer poped out from the stack and getMin()
which returns the min element from the stack. (-1 will be returned
if for pop() and getMin() the stack is empty.)

Expected Time Complexity : O(1) for all the 3 methods.
Expected Auixilliary Space : O(1) for all the 3 methods.

Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100
'''
class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        self.s.append(x)

    def pop(self):
        if len(self.s)!=0:
            z=self.s.pop()
            return z
        else:
            return -1
    def getMin(self):
        if len(self.s)!=0:
            x=min(self.s)
            return x
        else:
            return -1

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # q=int(input())
        # arr=[int(x) for x in input().split()]
        # q=6
        # arr=[1,2,1,3,2,3,1,1,3]
        q=33
        arr=[2,1,16,3,2,2,1,50,2,3,2,3,2,3,2,1,27,2,2,3,3,1,30,3,3,3,2,2,2,3,1,23,1,70,1,94,2,2,2,1,74]
        stk=stack()
        qi=0
        qn=1
        while(qn<=q):
            qt=arr[qi]
            if qt==1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()
