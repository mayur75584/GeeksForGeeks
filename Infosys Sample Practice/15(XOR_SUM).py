'''
Wael is well-known for how much he loves the bitwise XOR operation, while kaito is well known for how much he loves to sum numbers, so their friend Resli          decided to make up a problem that would enjoy both of them. Resil wrote down an array A of length N, an integer K and he defined a new function called  Xor-        sum as follows

Xor-sum(x)=(x XOR A[1])+(x XOR A[2])+(x XOR A[3])+…………..+(x XOR A[N])
    Can you find the integer x in the range [0,K] with the maximum Xor-sum (x) value?

    Print only the value.

    Input format

 The first line contains integer N denoting the number of elements in A.
The next line contains an integer, k, denoting the maximum value of x.
Each line i of the N subsequent lines(where 0<=i<=N) contains an integer describing Ai.
   Constraints

1<=N<=10^5
0<=K<=10^9
0<=A[i]<=10^9
   Sample Input 1

   1

   0

   989898

   Sample Output 1

   989898

   Explanation:

   Xor_sum(0)=(0^989898)=989898

   Sample Input 2

   3

   7

   1

   6

   3

   Sample Output 2

   14

   Explanation

    Xor_sum(4)=(4^1)+(4^6)+(4^3)=14.

    Sample Input 3

     4

     9

     7

    4

    0

    3

   Sample Output 3

   46

   Explanation:

   Xor_sum(8)=(8^7)+(8^4) +(8^0)+(8^3)=46.
'''
def XOR_Sum(i,A):
    sum1=0
    for j in A:
        sum1+=(i^j)
    return sum1

def func(N,K,A):

    max1=0
    for i in range(0,K+1):
        z=XOR_Sum(i,A)
        if max1<z:
            max1=z
    print(max1%(10**9))




# N=int(input())
# K=int(input())
# A=[]
# for i in range(N):
#     A.append(int(input()))
# N=3
# K=7
# A=[1,6,3]
# N=1
# K=0
# A=[989898]
N=4
K=9
A=[7,4,0,3]
func(N,K,A)
