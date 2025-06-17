'''
Recamans sequence

Given an integer n. Print first n elements of Recaman’s sequence.
It is basically a function with domain and co-domain as natural numbers and 0.
It is recursively defined as below:
Specifically, let a(n) denote the (n+1)-th term. (0 being already there).
The rule says:

a(0) = 0
a(n) = a(n-1) - n      if a(n-1) - n > 0 and is not already present in the sequence
       =  a(n-1) + n    otherwise.

Example 1:

Input: n = 6
Output: 0 1 3 6 2 7
Explaination: Follow the rule and this
will be the output.

Example 2:

Input: n = 3
Output: 0 1 3
Explaination: If the rule is followed,
it will produce this output.

Your Task:
You do not need to read input or print anything.
Your task is to complete the function recamanSequence()
which takes n as the input parameter and returns the sequence.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 100

'''
class Solution:
    def recamanSequence(self,n):
        a=[0]
        count1=0
        if n==1:
            return a
        a=[0]*(n)
        def rec(a,n,count1):
            if(count1>=n):
                return
            z=a[count1-1]-count1
            if(z>0 and z not in a):
                a[count1]=z
            else:
                x=a[count1-1]+count1
                a[count1]=x
            return rec(a,n,count1+1)

        rec(a,n,count1+1)
        return a

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # n=6
        n=3
        ob=Solution()
        ans=ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=' ')
        print()