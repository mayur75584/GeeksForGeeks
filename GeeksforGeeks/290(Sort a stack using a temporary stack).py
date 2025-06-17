'Note-> Below question is not in practice part of gfg'
'''
Sort a stack using a temporary stack

Given a stack of integers, sort it in ascending order using another temporary stack.

Examples:

Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]
'''
'''
We follow this algorithm.  

Create a temporary stack say tmpStack.
While input stack is NOT empty do this: 
Pop an element from input stack call it temp
while temporary stack is NOT empty and top of temporary stack is greater than temp, 
pop from temporary stack and push it to the input stack
push temp in temporary stack
The sorted numbers are in tmpStack
Here is a dry run of the above pseudo code.  

input: [34, 3, 31, 98, 92, 23]

Element taken out: 23
input: [34, 3, 31, 98, 92]
tmpStack: [23]

Element taken out: 92
input: [34, 3, 31, 98]
tmpStack: [23, 92]

Element taken out: 98
input: [34, 3, 31]
tmpStack: [23, 92, 98]

Element taken out: 31
input: [34, 3, 98, 92]
tmpStack: [23, 31]

Element taken out: 92
input: [34, 3, 98]
tmpStack: [23, 31, 92]

Element taken out: 98
input: [34, 3]
tmpStack: [23, 31, 92, 98]

Element taken out: 3
input: [34, 98, 92, 31, 23]
tmpStack: [3]

Element taken out: 23
input: [34, 98, 92, 31]
tmpStack: [3, 23]

Element taken out: 31
input: [34, 98, 92]
tmpStack: [3, 23, 31]

Element taken out: 92
input: [34, 98]
tmpStack: [3, 23, 31, 92]

Element taken out: 98
input: [34]
tmpStack: [3, 23, 31, 92, 98]

Element taken out: 34
input: [98, 92]
tmpStack: [3, 23, 31, 34]

Element taken out: 92
input: [98]
tmpStack: [3, 23, 31, 34, 92]

Element taken out: 98
input: []
tmpStack: [3, 23, 31, 34, 92, 98]

final sorted list: [3, 23, 31, 34, 92, 98]
'''
class Solution:
    def sorted(self,stack):
        tempStack=[]
        while(self.isEmpty(stack)==False):
            tmp=self.top(stack)
            self.pop(stack)
            # while temporary stack is not
            # empty and top of stack is
            # greater than temp
            while(self.isEmpty(tempStack)==False and int(self.top(tempStack))>int(tmp)):
                # pop from temporary stack and
                # push it to the input stack
                self.push(stack,self.top(tempStack))
                self.pop(tempStack)
            # push temp in temporary of stack
            self.push(tempStack,tmp)
        return tempStack

    def createStack(self):
        stack=[]
        return stack
    def isEmpty(self,stack):
        return len(stack)==0
    #Function to get top item of stcak
    def top(self,stack):
        p=len(stack)
        return stack[p-1]
    def pop(self,stack):
        if(self.isEmpty(stack)):
            # print("Stack Underflow")
            return -1
        return stack.pop()
    def push(self,stack,item):
        stack.append(item)
if __name__ == '__main__':
    ob=Solution()
    stack=ob.createStack()
    ob.push(stack,34)
    ob.push(stack,3)
    ob.push(stack,31)
    ob.push(stack,98)
    ob.push(stack,92)
    ob.push(stack,23)
    sortedstack=ob.sorted(stack)
    print(*sortedstack)