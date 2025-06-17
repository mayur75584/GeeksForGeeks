'''
Construct list using given q XOR queries


Given a list s that initially contains only a single value 0. There will be q queries of the following types:

0 x: Insert x in the list
1 x: For every element a in s, replace it with a ^ x. ('^' denotes the bitwise XOR operator)
Return the sorted list after performing the given q queries.

Example 1:

Input:
q = 5
queries[] = {{0, 6}, {0, 3}, {0, 2}, {1, 4}, {1, 5}}
Output:
1 2 3 7
Explanation:
[0] (initial value)
[0 6] (add 6 to list)
[0 6 3] (add 3 to list)
[0 6 3 2] (add 2 to list)
[4 2 7 6] (XOR each element by 4)
[1 7 2 3] (XOR each element by 5)
The sorted list after performing all the queries is [1 2 3 7].
Example 2:
Input:
q = 3
queries[] = {{0, 2}, {1, 3}, {0, 5}}
Output :
1 3 5
Explanation:
[0] (initial value)
[0 2] (add 2 to list)
[3 1] (XOR each element by 3)
[3 1 5] (add 5 to list)
The sorted list after performing all the queries is [1 3 5].

Your Task:
You don't need to read input or print anything.
Your task is to complete the function constructList() which takes an integer q the number of queries and queries[] a list of lists of length 2 denoting the queries as input parameters and returns the final constructed list.


Expected Time Complexity: O(q*log(q))
Expected Auxiliary Space: O(l), where l is only used for output-specific requirements.


Constraints:
1 ≤ q ≤ 105
'''
'''
Optimized approch will be

to traverse list of list from right to left and keep a variable xor=0.
So, when you start traversing from right to left , if you get 0 then
append xor ans of 2nd index value of sublist ^ xor.
if you get 1 then update xor i.e xor ^ 2nd index value of sublist.

At end append updated value of xor in answer list.
Return sorted answer list.
'''

from typing import List


class Solution:
    def constructList(self,q,queries):
        res=[]
        xor=0
        for i in range(q-1,-1,-1):
            x,y=queries[i][0],queries[i][1]
            if x==0:
                res.append(y^xor)
            elif x==1:
                xor=xor^y
        res.append(xor)
        # print(res)
        return sorted(res)


class IntMatrix:
    def __init__(self):
        pass
    def Input(self,n,m):
        matrix=[]
        for i in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()

class IntArray:
    def __init__(self):
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # q=int(input())
        # queries=IntMatrix().Input(q,2)
        q=5
        queries=[[0,6],[0,3],[0,2],[1,4],[1,5]]
        # q=3
        # queries=[[0,2],[1,3],[0,5]]
        obj=Solution()
        res=obj.constructList(q,queries)

        IntArray().Print(res)