'''
Given an Array of size N and a value K, around which we need to right
rotate the array.

Input: Array[] = {1,3,5,7,9} , k=2
Output: 7 9 1 3 5

Explanation:
After 1st rotation - {9,1,3,5,7}
After 2nd rotation - {7,9,1,3,5}

Input:Array[] = {1,2,3,4,5}, k=4
Output:2 3 4 5 1
'''

def right(arr,k):
    x=len(arr)
    arr1=arr
    for i in range(k):
        lst=[]
        z=arr1.pop(x-1)
        lst.append(z)
        arr1.insert(0,z)
    return arr1




if __name__ == '__main__':
    arr=list(map(int,input().split()))
    k=int(input())
    result=right(arr,k)
    print(*result)