'''
Rotate Array

Given an unsorted array arr[] of size N.
Rotate the array to the left (counter-clockwise direction) by D steps,
where D is a positive integer.

Example 1:
Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.

Example 2:
Input:
N = 10, D = 3
arr[] = {2,4,6,8,10,12,14,16,18,20}
Output: 8 10 12 14 16 18 20 2 4 6
Explanation: 2 4 6 8 10 12 14 16 18 20
when rotated by 3 elements, it becomes
8 10 12 14 16 18 20 2 4 6.

Your Task:
Complete the function rotateArr() which takes the array,
D and N as input parameters and rotates the array by D elements.
The array must be modified in-place without using extra space.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 106
1 <= D <= 106
0 <= arr[i] <= 105
'''
class Solution:
    def rotateArr(self,A,D,N):
        if D<N:
            x=[]
            x.extend(A[:D])
            del A[:D]
            A.extend(x)
            return A
        elif D==N:
            return A
        else:
            while(D!=0):
                z=abs(N-D)
                if z==0:
                    return A
                else:
                    x=[]
                    x.extend(A[:z])
                    del A[:z]
                    A.extend(x)
                D-=z
            return A
if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # N,D=map(int,input().split())
        # A=list(map(int,input().split()))
        # N,D=5,2
        # A=[1,2,3,4,5]
        # N,D=10,3
        # A=[2,4,6,8,10,12,14,16,18,20]
        N,D=47,77
        A=[25,6,20,55,69,5,50,63,61,41,87,80,2,96,77,70,12,43,31,8,64,41,68,18,95,79,52,74,1,98,3,26,3,74,32,23,79,81,37,39,21,24,18,22,71,47,44]
        ob=Solution()
        ob.rotateArr(A,D,N)
        for i in A:
            print(i,end=' ')
        print()
        T-=1