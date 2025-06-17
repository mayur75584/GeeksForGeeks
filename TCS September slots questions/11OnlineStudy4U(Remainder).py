'Remainder'


'''
Given a string Str, contains digits only. The task is to find
the remainder of Str when n is divided by k

Constraints:
Size of Str>=10<=100
1<k<20

Example1:
Input:
2345434534665
6
Output:
3

Example2:
Input:
23454345346653434454543
3

Output:
0
'''

n=input()
k=int(input())
print(int(n)%k)