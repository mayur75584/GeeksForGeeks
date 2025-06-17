'''
Input: arr[] = {1, 5, 3, 4, 2}, k = 3
Output: 2
There are 2 pairs with difference 3, the pairs are {1, 4} and {5, 2}

Input: arr[] = {8, 12, 16, 4, 0, 20}, k = 4
Output: 5
There are 5 pairs with difference 4, the pairs are {0, 4}, {4, 8},
{8, 12}, {12, 16} and {16, 20}
'''
'Not able to solve this question'

def func(arr,k):
    count=0
    arr.sort()
    l=0
    r=0
    n=len(arr)
    while r<n:
        if arr[r]-arr[l]==k:
            count+=1
            l+=1
            r+=1
        elif arr[r]-arr[l]>k:
            l+=1
        else:
            r+=1
    return count



if __name__ == '__main__':
    # arr=list(map(int,input().split()))
    # k=int(input())
    arr=[1,5,3,4,2]
    k=3
    # arr=[8,12,16,4,0,20]
    # k=4
    result=func(arr,k)
    print(result)

