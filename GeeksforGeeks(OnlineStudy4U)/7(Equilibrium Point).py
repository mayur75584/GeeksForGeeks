'''
Equilibrium point

Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array.
Equilibrium position in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow.
First line of each test case contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array A.

Output:
For each test case in a new  line print the position at which the elements are at equilibrium if no equilibrium point exists print -1.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= Ai <= 108

Example:
Input:
2
1
1
5
1 3 5 2 2

Output:
1
3

Explanation:
Testcase 1: Since its the only element hence its the only equilibrium point.
Testcase 2: For second test case equilibrium point is at position 3 as elements below it (1+3) = elements after it (2+2).

'''
'Note-> you were not able to submit the solution and you havent seen the solution in onlinestudy4U '
'Try to submit the solution and if Login is done and solution is not submited see the video of onlinestudy4u'

# t=int(input())
t=1
for i in range(t):
    # n=int(input())
    # lst=list(map(int,input().split()))
    n=5
    lst=[1,3,5,2,2]
    if n==1:
        print(1)
    else:
        for i in range(n):
            a=sum(lst[i+1:])
            b=sum(lst[:i])
            if a==b:
                print(i+1)

