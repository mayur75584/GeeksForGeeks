'''
The King of Codeland is a very modern king and is ready to
bring about the digital revolution in his kingdom. He has started
distributing mobile phones to his people. Along with the mobile
phone,he needs to distribute SIM cards to people,
so that they can use the phones to communicate with each other.

But the phone number needs to be unique. He finally decides to keep
the mobile number of N digits.

The king has found a unique solution to this problem. He will take
a string S of length N+2 made up of the digits 0 9.
He will then extract all distinct subsequences of length N from
this string to use a mobile numbers.

Recall that a subsequence is obtained by dropping some letters
from the original sequence without disturbing the order.

The task is to find out how many distinct subsequneces of length N
can be formed from a given string s of length N+2.

As the result can be very large, you should print the value modulo
((10**9)+7) (the remainder when divided by ((10**9)+7).

Example1:
Input:
"15025"   -> String s
Output:
10

Explanation:
All unique subsequnce of length (5-2) are:
"025","525",505","502","125","105","102","155","152","150".:arg

Example2:
Input:
"781484"   -> String s
Output:
14
Explanation:
All unique subsequnce of length(6-2)=4 are:
"1484","8484","8184","8144",8148","7484","7184","7144",
"7148","7884","7844","7848","7814","7818".

Constraints:
0<=s[i]<=9
2<=Length(s)<=100000

The input format for testing:
First Line: String s of length N+2
The Output format for testing:
Output the single line denoting the number of unique sub sequence
of string s can be formed modulo ((10**9)+7).
Additional messages in output will cause the failure of test cases.
'''
'Correct Solution'
import itertools
def func(s):
    n=len(s)-2
    z=list(itertools.combinations(s,n))
    print(z)
    x=[]
    for i in z:
        if ''.join(i) not in x:
            x.append(''.join(i))
    print(x)
    ans=len(x)%((10**9)+7)
    return ans
if __name__ == '__main__':
    # s=input()
    # s='15025'
    s='781484'
    res=func(s)
    print(res)

