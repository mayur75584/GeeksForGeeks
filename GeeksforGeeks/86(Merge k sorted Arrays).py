'''
Merge k Sorted Arrays

Given K sorted arrays arranged in the form of a matrix of size K*K. The task is to merge them into one sorted array.
Example 1:

Input:
K = 3
arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
Output: 1 2 3 4 5 6 7 8 9
Explanation:Above test case has 3 sorted
arrays of size 3, 3, 3
arr[][] = [[1, 2, 3],[4, 5, 6],
[7, 8, 9]]
The merged list will be
[1, 2, 3, 4, 5, 6, 7, 8, 9].

Example 2:

Input:
K = 4
arr[][]={{1,2,3,4}{2,2,3,4},
         {5,5,6,6},{7,8,9,9}}
Output:
1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9
Explanation: Above test case has 4 sorted
arrays of size 4, 4, 4, 4
arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4],
[5, 5, 6, 6]  [7, 8, 9, 9 ]]
The merged list will be
[1, 2, 2, 2, 3, 3, 4, 4, 5, 5,
6, 6, 7, 8, 9, 9 ].

Your Task:
You do not need to read input or print anything. Your task is to complete mergeKArrays() function which takes 2 arguments, an arr[K][K] 2D Matrix containing K sorted arrays and an integer K denoting the number of sorted arrays, as input and returns the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python)

Expected Time Complexity: O(K2*Log(K))
Expected Auxiliary Space: O(K)

Constraints:
1 <= K <= 100
'''
class Solution:
    def mergeKArrays(self,arr,k):
        result=[]
        for i in arr:
            z=sorted(i)
            result+=z
        # print(result)
        # print(sorted(result))
        return sorted(result)

if __name__ == '__main__':
    t=int(input())
    # t=1
    for _ in range(t):
        n=int(input())
        numbers=[[0 for _ in range(n)] for _ in range(n)]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j] = int(line[i*n+j])
        # n=4
        # numbers=[[1,2,3,4],[2,2,3,4],[5,5,6,6],[7,8,9,9]]
        ob=Solution()
        # ob.mergeKArrays(numbers,n)
        merged_list = ob.mergeKArrays(numbers,n)
        for i in merged_list:
            print(i,end=' ')
        print()