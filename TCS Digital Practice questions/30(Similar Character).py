'''
Similar Character Problem

Statement
Tahir and Mamta are working on a project in TCS. Tahir being a problem solver came up with an interesting problem for his friend Mamta.

The problem consists of a string of length N and contains only small case alphabets. It will be followed by Q queries, in which each query will contain an integer P (1<=P<=N) denoting a position within the string.

Mamta's task is to find the alphabet present at that location and determine the number of occurrences of the same alphabet preceding the given location P. You need to print the smallest lexicographic string made from the given string S.

Mamta is busy with her office work. Therefore, she asked you to help her.

Constraints
1 <= N <= 500000
S consisting of small case alphabets
1 <= Q <= 10000
1 <= P <= N

Input Format
First-line contains an integer N, denoting the length of the string.
Second-line contains string S itself consists of small case alphabets only ('a' - 'z').
The third line contains an integer Q denoting the number of queries that will be asked.
Next, Q lines contain an integer P (1 <= P <= N) for which you need to find the number occurrence of character present at the Pth location preceding P.

Output Format
For each query, print an integer denoting the answer on a single line.

Example:

Input
9
abacsddaa
2
9
3

Output
3
1

Explanation:
Here Q = 2 (Test Cases) For P=9, the character at the 9th location is 'a'. The number of occurrences of 'a' before P i.e., 9 is three. Similarly, for P=3, 3rd character is 'a'. The number of occurrences of 'a' before P. i.e., 3 is one.

Input -
n=12
s='upasanasingh'
q=1
p=8

Output-
1
'''
def func(n,s,p):
    z=s[p-1]
    res=s[:p-1].count(z)
    return res
if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        n=int(input())
        s=input()
        q=int(input())
        result=[]
        for i in range(q):
            p=int(input())
            res=func(n,s,p)
            result.append(res)
        for i in range(len(result)-1):
            print(result[i])
        print(result[-1],end=' ') #Use for i in range instead of for i in sequence to avoid presentation error in codevita
