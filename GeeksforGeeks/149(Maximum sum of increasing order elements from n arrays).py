'''
Maximum sum of increasing order elements from n arrays

Given n arrays of size m each. Find maximum sum obtained by selecting a number from each array such that
the element selected from the i-th array is more than the element selected from (i-1)-th array.
If maximum sum cannot be obtained then return 0.

Example 1:
â€‹Input : arr[ ] = {{1,7,4,3}, {4,2,5,1}, {9,5,1,8}}
Output : 18
Explanation:
We can select 4 from the first array,
5 from second array and 9 from the third array.


â€‹Example 2:
Input : arr[ ] = {{9,8,7}, {6,5,4}, {3,2,1}}
Output :  0
Your Task:
This is a function problem.
The input is already taken care of by the driver code.
 You only need to complete the function maximumSum() that takes number of row N, a number of Column M, 2-d array (arr),
 and return the maximum sum if cannot be obtained then return 0. The driver code takes care of the printing.

Expected Time Complexity: O(N*M).
Expected Auxiliary Space: O(1).
'''

def maximumSum(n,m,arr):
    arr=arr[::-1]
    print(arr)
    sum1=0
    z=[9999]
    count1=0
    for i in arr:
        x=sorted(i,reverse=True)
        for j in x:
            if z[-1]>j:
                sum1+=j
                z.append(j)
                count1+=1
                break
    if count1==len(arr):
        return sum1
    else:
        return 0
if __name__ == '__main__':
    # n,m=map(int,input().split())
    # arr=[]
    # for i in range(n):
    #     l=list(map(int,input().split()))
    #     arr.append(l)
    n,m=3,4
    arr=[[1,7,4,3],[4,2,5,1],[9,5,1,8]]
    # n,m=3,3
    # arr=[[9,8,7],[6,5,4],[3,2,1]]
    ans=maximumSum(n,m,arr)
    print(ans)