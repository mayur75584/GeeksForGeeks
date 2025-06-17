'''
Queries on Strings

Given a string str you have to answer several queries on that string.
In each query you will be provided two values L and R and you have
to find the number of distinct characters in the sub string from
index L to index R (inclusive) of the original string.


Example 1:
Input: str = "abcbaed",
Query = {{1,4},{2,4},{1,7}}
Output: {3,2,5}
Explanation: For the first query distinct
characters from [1, 4] are a, b and c.
For the second query distinct characters from
[2, 4] are b and c.
For the third query distinct characters from
[1, 7] are a, b, c, d and e.

Your Task:
You don't need to read or print anyhting.
Your task is to complete the function SolveQueries() which takes str
and Query as input parameter and returns a list containing answer for each query.


Expected Time Complexity: O(max(length of str, 26 * No of queries))
Expected Space Complexity: O(26 * length of str)

Constraints:
1 <= |str| <= 105
1 <= No of Queries <= 104
1 <= Li <= Ri <= |str|
'''

class Solution:
    def SolveQueries(self,s,Query):
        res=[]
        for i in Query:
            l,r=i[0],i[1]
            x=set(s[l-1:r])
            res.append(len(x))
        return res
if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # s=input()
        # q=int(input())
        # Query=[]
        # for i in range(q):
        #     a=list(map(int,input().split()))
        #     Query.append(a)

        s='abcbaed'
        Query=[[1,4],[2,4],[1,7]]

        obj=Solution()
        ans=obj.SolveQueries(s,Query)
        for _ in ans:
            print(_,end=' ')
        print()