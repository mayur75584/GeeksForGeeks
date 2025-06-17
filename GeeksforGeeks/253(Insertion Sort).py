'''
Insertion Sort

The task is to complete the insert() function which is used to implement
Insertion Sort.


Example 1:

Input:
N = 5
arr[] = { 4, 1, 3, 9, 7}
Output:
1 3 4 7 9

Example 2:

Input:
N = 10
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output:
1 2 3 4 5 6 7 8 9 10


Your Task:
You don't have to read input or print anything.
Your task is to complete the function insert() and insertionSort()
where insert() takes the array, it's size and an index i and
insertionSort() uses insert function to sort the array in ascending order
using insertion sort algorithm.


Expected Time Complexity: O(N*N).
Expected Auxiliary Space: O(1).


Constraints:
1 <= N <= 1000
1 <= arr[i] <= 1000
'''
class Solution:
    def insert(self,alist,index,i):
        x=alist.pop(index)
        alist.insert(i,x)
        return alist

    def insertionSort(self,alist,n):
        for i in range(n):
            min1=i
            for j in range(i+1,n):
                if alist[min1]>alist[j]:
                    min1=j
            alist=self.insert(alist,min1,i)


if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # n=5
        # arr=[4,1,3,9,7]
        n=10
        arr=[10,9,8,7,6,5,4,3,2,1]
        Solution().insertionSort(arr,n)
        for i in range(n):
            print(arr[i],end=' ')
        print()