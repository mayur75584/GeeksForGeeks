'''
Find the largest number


Find the largest number
Medium Accuracy: 54.12% Submissions: 1261 Points: 4

Given an integer N the task is to find the largest number which is smaller or equal to it and has its digits in non-decreasing order.


Examples 1:

Input:
N = 200
Output:
199
Explanation:
If the given number
is 200, the largest
number which is smaller
or equal to it having
digits in non decreasing
order is 199.

Example 2:

Input:
N = 139
Output:
139
Explanation:
139 is itself in
non-decresing order.


Your Task:
You don't need to read input or print anything. Your task is to complete the function find() which takes one integer value N,
as input parameter and return the largest number which is smaller or equal to it and has its digits in non-decreasing order.


Expected Time Complexity: O(N)
Expected Space Complexity: O(1)


Constraints:
1<=N<=105

'''



class Solution:
    def find(self,N):
        for i in range(N,0,-1):
            if i<=N:
                z=sorted(str(i))
                if str(i)==''.join(z):
                    return i


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # N=200
        N=139
        ob=Solution()
        print(ob.find(N))