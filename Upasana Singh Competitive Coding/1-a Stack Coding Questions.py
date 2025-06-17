'''
Find the nearest smaller numbers on left side in an array

Given an array of integers, find the nearest smaller number for
every element such that the smaller element is on left side.

Input: arr[]=[1,6,4,10,2,5]
Output: [_,1,1,4,1,2]

Input: arr[]=[1,3,0,2,5]
Output: [_,1,_,0,2]
'''


def printPrevSmaller(arr,n):
    stack=[]
    for i in range(n):
        while(len(stack)!=0 and stack[-1]>=arr[i]):
            stack.pop(-1)
        if(len(stack)==0):
            print("_",end=' ')
        else:
            print(stack[-1],end=",")

        stack.append(arr[i])

if __name__ == '__main__':
    arr=[1,3,0,2,5]
    n=len(arr)
    printPrevSmaller(arr,n)
