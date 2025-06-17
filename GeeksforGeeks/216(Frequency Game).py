'''
Frequency Game
Given an array A of size N. The elements of the array consists of
positive integers. You have to find the largest element with minimum frequency.

Input Format: First line of input contains number of testcases T.
For each testcase there will be two lines. First line contains N,
next line contains N elements separated by spaces.

Output Format: For each testcase, print the largest element with minimum frequency.

User Task:
Your task is to complete the provided function LargButMinFreq(A, n)
which accepts array A and n. Hence you have to return the largest element
with minimum frequency.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
1
5
2 2 5 50 1

Output:
50

Explanation :
Testcase 1: All elements are having frequency 1 except 2.
50 is the maximum element with minimum frequency.
'''
def LargButMinFreq(arr,n):
    dict1={}
    for i in arr:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    x=sorted(dict1.items(),key=lambda x:x[0],reverse=True)
    print(x)
    return x[0][0]


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        n=5
        arr=[2,2,5,50,1]
        print(LargButMinFreq(arr,n))