'''
A non-empty array A consisting of N integers is given. This array contains a
decimal representation of a number V i.e element A[k] contains the k-th
least significant digit of the decimal representation of V.
For example, array A such that:
A[0]=3
A[1]=5
A[2]=1
represents the number V = 153.
Write a function int solution(vector<int> &A);
that, given an array A consisting of N integers specifying a decimal representation
of a number V, returns the sum of the digits in the decimal representation
of the number 17*V.
For example, given array A such that
A[0]=3
A[1]=5
A[2]=1
the function should return 9,because
array A represents the number 153
17*153=2601
the sum of the digits in the decimal representation of 2601 is 2+6+0+1=9.
Write an efficient algorithm for the following assumptions.
'''

'Note-> Dont know whether solution is completely correct or not'
if __name__ == '__main__':
    # A=list(map(int,input().split()))
    A=[3,5,1]
    z=A[::-1]
    val=0
    for i in z:
        val=(val*10)+i
    print(val)
    new_val=17*val
    print(new_val)
    ans=0
    for i in str(new_val):
        ans+=int(i)
    print(ans)