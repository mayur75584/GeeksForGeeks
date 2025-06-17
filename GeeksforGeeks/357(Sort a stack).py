'''
Sort a stack

Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Example 1:

Input:
Stack: 3 2 1
Output: 3 2 1

Example 2:

Input:
Stack: 11 2 32 3 41
Output: 41 32 11 3 2

Your Task:
You don't have to read input or print anything.
Your task is to complete the function sort() which sorts the elements present in the given stack.
(The sorted stack is printed by the driver's code by popping the elements of the stack.)

Expected Time Complexity: O(N*N)
Expected Auxilliary Space: O(N) recursive.

Constraints:
1<=N<=100

'''
'''
Algorithm

We can use the below algorithm to sort stack elements:

sortStack(stack S)
    if stack is not empty:
        temp = pop(S);
        sortStack(S);
        sortedInsert(S, temp);

Below algorithm is to insert element is sorted order:

sortedInsert(Stack S, element)
    if stack is empty OR element > top element
        push(S, elem)
    else
        temp = pop(S)
        sortedInsert(S, element)
        push(S, temp)
'''
class Solution:
    def sortedInsert(self,s,temp):
        if(len(s)==0 or temp>s[-1]):
            s.append(temp)
        else:
            temp1=s.pop(-1)
            self.sortedInsert(s,temp)
            s.append(temp1)
    def sorted(self,s):
        if(len(s)!=0):
            temp=s.pop(-1)
            self.sorted(s)
            self.sortedInsert(s,temp)

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=5
        arr=[11,2,32,3,41]
        # n=3
        # arr=[2,1,3]
        ob=Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(),end=' ')
        print()