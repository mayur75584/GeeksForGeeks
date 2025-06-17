

'''
Problem statement
You are given two polynomials. You have to multiply them and print the result.

You are given the coefficients of the first and second polynomials denoted by array A and array B respectively. You have to return the coefficient of the resulting polynomials.

Example:-
A = [1,2,3]
B = [3,2,1]

ANSWER:- The answer should be [3,8,14,8,3] as the polynomials are x^2 + 2x + 3 and 3x^2 + 2x + 1.On multiplying we get 3x^4 + 8x^3 + 14x^2 + 8x + 3 and hence the answer is [3, 8, 14, 8, 3].
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 10
1 <= N <= 10^4
1 <= A[i] <= 500
1 <= B[i] <= 500
Time Limit = 1 sec

Sample Input 1 :
2
3
1 0 1
2 1 0
1
1
1
Sample Output 1 :
2 1 2 1 0
1
Explanation for Sample Output 1 :
In the first test case, the polynomials are x^2 + 1 and 2x^2 + x. On multiplying we get 2x^4 + x^3 + 2x^2 + x and hence the answer is [2, 1, 2, 1, 0].
In the second test case, the polynomials are 1 and 1. On multiplying we get 1 and hence the answer is [1].
Sample Input 2 :
1
2
1 1
1 1
Sample Output 2 :
1 2 1

'''

def func(a,b,c):
    """
        if c==1:
            return [a[0]*b[0]]
        else:
            lst=[]
            for i in a:
                sub_lst=[]
                for j in b:
                    sub_lst.append(i*j)
                lst.append(sub_lst)
            ans={}
            for i in range(len(lst)):
                for j in range(len(lst[i])):
                    if i+j not in ans:
                        ans[i+j]=lst[i][j]
                    else:
                        ans[i+j]+=lst[i][j]
            return list(ans.values())
            return lst
            """
    # Optimal Solution
    if c == 1:
        return [a[0] * b[0]]
    else:

        n = len(a)
        m = len(b)
        result = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                result[i + j] += (a[i] * b[j])
        return result
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # c=int(input())
        # a=list(map(int,input().split()))
        # b=list(map(int,input().split()))
        c=14
        a=[1 ,44 ,26 ,15 ,5 ,40 ,26 ,39 ,37 ,22 ,5 ,11 ,4 ,39]
        b=[16 ,23 ,20 ,12 ,4 ,37 ,19 ,16 ,9,28,25,29,48,28]
        ans=func(a,b,c)
        print(ans)