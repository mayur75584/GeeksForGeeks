'''
Next Greater element to right

Given an array, print the Next Greater Element(NGE) for every element.
The next greater element for an element x is the first greater element on the right
side of x in the array. Elements for which no greater element exist, consider the next greater
element as -1.

Element NGE
4 5 2 25

4-->5
5-->25
2-->25
25-->-1

13 7 6 12
13-->-1
7-->12
6-->12
12-->-1
'''

def printNGE(arr,n):
    stack=[]
    res=[0]*n
    # print(res)
    for i in range(n-1,-1,-1):
        if(len(stack)!=0):
            while(len(stack)!=0 and stack[-1]<=arr[i]):
                stack.pop()
        if(len(stack)==0):
            res[i]=-1
        else:
            res[i]=stack[-1]
        stack.append(arr[i])
    for i in range(n):
        print(arr[i],"-->",res[i])

if __name__ == '__main__':
    arr=[11,13,21,3]
    n=len(arr)
    printNGE(arr,n)

