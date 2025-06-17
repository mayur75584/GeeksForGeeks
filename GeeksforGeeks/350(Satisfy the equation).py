'''
Satisfy the equation

Given an array A[ ] of N of  integers, find the index of values
that satisfy A + B = C + D where A,B,C & D are integers values in the array.
Note: As there may be multiple pairs satisfying the equation
return lexicographically smallest order of  A, B, C and D and
return all as -1 if there are no pairs satisfying the equation.



Example 1:

Input:
N = 7
A[] = {3, 4, 7, 1, 2, 9, 8}
Output:
0 2 3 5
Explanation:
A[0] + A[2] = 3+7 = 10
A[3] + A[5] = 1+9 = 10

Example 2:

Input:
N = 4
A[] = {424, 12, 31, 7}
Output:
-1 -1 -1 -1
Explanation:
There are no pairs satisfying the equation.



Your Task:
You don't need to read input or print anything.
Your task is to complete the function satisfyEqn()
which takes an Integer N and an array A[] of size N as input
and returns a vector of 4 integers denoting A, B, C, and D respectively.



Expected Time Complexity: O(N2*logN2)
Expected Auxiliary Space: O(N2)



Constraints:
1 <= N <= 500
1 <= A[i] <= 105

'''
class Solution:
    def satisfyEqn(self,A,N):
        dict1 = {}
        for i in range(N - 1):  # Here give N-1 bcz for last value of N we dont want to iterate the loop as it will be waste for j
            for j in range(i + 1, N):
                sum1 = A[i] + A[j]
                if sum1 not in dict1:
                    dict1[sum1] = [i, j]
                else:
                    x = dict1[sum1]
                    if len(x) < 4 and i not in x and j not in x:
                        dict1[sum1].extend([i, j])
        # print(dict1)
        dict2 = {}
        for i in dict1.items():
            if len(i[1]) == 4:
                dict2[i[0]] = i[1]
        # print(dict2)
        s = sorted(dict2.items(), key=lambda x: x[1])
        # print(s)
        if len(s) != 0:
            return s[0][1]
        else:
            return [-1, -1, -1, -1]


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # A=list(map(int,input().split()))
        # N=7
        # A=[3,4,7,1,2,9,8]
        # N=4
        # A=[424,12,31,7]
        N=22
        A=[684,931,873,347,748,68,810,604,333,291,68,422,684,39,756,485,215,7,217,690,758,476]
        ob=Solution()
        ptr=ob.satisfyEqn(A,N)
        print(*ptr)