'''
Find all pairs with a given sum

Given two unsorted arrays A of size N and B of size M of distinct elements,
the task is to find all pairs from both arrays whose sum is equal to X.

Note: All pairs should be printed in increasing order of u.
For eg. for two pairs (u1,v1) and (u2,v2), if u12 then
(u1,v1) should be printed first else second.

Example 1:

Input:
A[] = {1, 2, 4, 5, 7}
B[] = {5, 6, 3, 4, 8}
X = 9
Output:
1 8
4 5
5 4
Explanation:
(1, 8), (4, 5), (5, 4) are the
pairs which sum to 9.

Example 2:

Input:
A[] = {-1, -2, 4, -6, 5, 7}
B[] = {6, 3, 4, 0}
X = 8
Output:
4 4
5 3


Your Task:
You don't need to read input or print anything.
Your task is to complete the function allPairs() which takes the array A[], B[],
its size N and M respectively, and an integer X as inputs
and returns the sorted vector pair values of all the pairs u,v
where u belongs to array A and v belongs to array B.
If no such pair exists return empty vector pair.


Expected Time Complexity: O(NLog(N))
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N, M ≤ 106
-106 ≤ X, A[i], B[i] ≤ 106

'''
class Solution:
    def allPairs(self,A,B,N,M,X):
        dict1={}
        for i in A:
            x=X-i
            if x in B:
                dict1[(i,x)]=1
        print(dict1)
        d=sorted(dict1.items(),key=lambda x:x[0])
        print(d)
        ans=[]
        for i in d:
            ans.append(i[0])
        return ans
if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # N,M,X=map(int,input().split())
        # A=list(map(int,input().split()))
        # B=list(map(int,input().split()))
        N,M,X=5,5,9
        A=[1,2,4,5,7]
        B=[5,6,3,4,8]
        ob=Solution()
        answer=ob.allPairs(A,B,N,M,X)
        sz=len(answer)
        if sz==0:
            print(-1)
        else:
            for i in range(sz):
                if i==sz-1:
                    print(*answer[i])
                else:
                    print(*answer[i],end=', ')
        T-=1