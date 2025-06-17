'''
  Khaled has an array A of N elements. It is guaranteed that N is even. He wants to choose at most N/2 elements from array A. It is not necessary to choose             consecutive elements.  Khaled is interested in XOR of all the elements he chooses. Here, XOR denotes the bitwise XOR operation.

   For example:

If A=[2,4,6,8], then khaled can choose the subset [2,4,8] to achieve XOR=(2 XOR 4 XOR 8)=14.
   Khaled wants to maximize the XOR of all the elements he chooses. Your task is to help khaled to find the max XOR of a subset that he can achieve by choosing     at most N/2 elements?

   Input format:

The first line contains an integer, N, denoting the number of elements in A.
Each line i of the N subsequent lines(where 0<=i<=N) contains an integer describing Ai.
   Constraints

1<=N<=120
1<=A[i]<=10^6
   Sample Input 1

   2

   1

   2

   Sample Output 1

   2

   Explanation:

   N=2,  A=[1,2] khaled can choose the subset[2].
   The xor of the elements in the subset is 2.
   And the number of elements in the subset is 1 which is less than N/2.

   Sample Input 2

   4

   1

   2

   4

   7

   Sample Output 2

   7

   Explanation:

   N=4,  A=[1,2,4,7] Khaled can choose the subset [7]. The xor of the elements in the subset is 7, and the number of elements in the subset is 1 which is less than       N/2.


'''
'Not confirmed whether given solution comes under specific time complexity'
from itertools import combinations
def subarray(z,A):

    subarrays=[]
    for i in range(1,z+1):
        subarrays.extend(combinations(A,i))
    return subarrays

def func(N,A):
    x=subarray(N//2,A)
    print(x)
    max1=0
    for i in x:
        xor=0
        for j in list(i):
            xor^=j
        if max1<xor:
            max1=xor
    print(max1%(10**9))




# N=int(input())
# A=[]
# for i in range(N):
#     A.append(int(input()))
# N=4
# A=[1,2,4,7]
# N=2
# A=[1,2]
N=4
A=[2,4,6,8]
func(N,A)