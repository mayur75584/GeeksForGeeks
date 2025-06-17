'''
Stock span problem

The stock span problem is a financial problem where we
have a series of n daily price quotes for a stock and
we need to calculate the span of stocks price for all n days.
The span Si of the stocks price on a given day i is defined
as the maximum number of consecutive days just before the given day,
for which the price of the stock on the current day is less than or
equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

Example 1:
Input:
N = 7, price[] = [100 80 60 70 60 75 85]
Output:
1 1 1 2 1 4 6
Explanation:
Traversing the given input span for 100
will be 1, 80 is smaller than 100 so the
span is 1, 60 is smaller than 80 so the
span is 1, 70 is greater than 60 so the
span is 2 and so on. Hence the output will
be 1 1 1 2 1 4 6.

Example 2:
Input:
N = 6, price[] = [10 4 5 90 120 80]
Output:
1 1 2 4 5 1
Explanation:
Traversing the given input span for 10
will be 1, 4 is smaller than 10 so the
span will be 1, 5 is greater than 4 so
the span will be 2 and so on. Hence, the
output will be 1 1 2 4 5 1.

User Task:
The task is to complete the function calculateSpan() which takes two parameters,
an array price[] denoting the price of stocks,
and an integer N denoting the size of the array and number of days.
This function finds the span of stock's price for all N days
and returns an array of length N denoting the span for the i-th day.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 105
1 ≤ C[i] ≤ 105


'''
class Solution:
    def calculateSpan(self,a,n):
        stack=[]
        stack.append(0)
        S=[0]*n
        S[0]=1
        for i in range(1,n):
            while(len(stack)!=0 and a[stack[-1]]<=a[i]):
                stack.pop(-1)
            if(len(stack)==0):
                S[i]=i+1
            else:
                S[i]=i-stack[-1]
            stack.append(i)
        return S

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # a=list(map(int,input().split()))
        # n=7
        # a=[100,80,60,70,60,75,85]
        n=6
        a=[10,4,5,90,120,80]
        obj=Solution()
        ans=obj.calculateSpan(a,n)
        for i in range(n):
            print(ans[i],end=' ')
        print()