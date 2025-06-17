'''
Stack using two queues

Implement a Stack using two queues q1 and q2.

Example 1:

Input:
push(2)
push(3)
pop()
push(4)
pop()
Output: 3 4
Explanation:
push(2) the stack will be {2}
push(3) the stack will be {2 3}
pop()   poped element will be 3 the
        stack will be {2}
push(4) the stack will be {2 4}
pop()   poped element will be 4

Example 2:

Input:
push(2)
pop()
pop()
push(3)
Output: 2 -1

Your Task:

Since this is a function problem, you don't need to take inputs.
You are required to complete the two methods push() which takes
an integer 'x' as input denoting the element to be pushed into
the stack and pop() which returns
the integer poped out from the stack(-1 if the stack is empty).

Expected Time Complexity: O(1) for push() and O(N) for pop() (or vice-versa).
Expected Auxiliary Space: O(1) for both push() and pop().

Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100
'''

def push(x):
    global queue_1
    global queue_2
    queue_1.append(x)

def pop():
    global queue_1
    global queue_2
    if len(queue_1)==0:
        return -1
    else:
        queue_2.append(queue_1.pop(-1))
        return queue_2[-1]

queue_1=[]
queue_2=[]

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # a=list(map(int,input().split()))
        # n=5
        # a=[1,2,1,3,2,1,4,2]

        i=0
        while(i<len(a)):
            if(a[i]==1):
                push(a[i+1])
                i+=1
            else:
                print(pop(),end=' ')
            i+=1
        #clear both the queues
        queue_1=[]
        queue_2=[]
        print()