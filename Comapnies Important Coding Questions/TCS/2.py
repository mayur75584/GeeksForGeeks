'''
Given a list numberList[] of integer numbers that have size N and one another
number N2, also given the size S(integer number) of the subset. The task is to
find the number N2 present in every non overlapping subset of size S in
numberList[]. If number N2 is present in every subset print 1 otherwise
print 0.

Example1:

Input:
12
20
1
6
8
13
20
1
7
20
13
16
20

-> Each value separated by a new line

20 -> Value of N2

3  -> value of S i.e size of subset

Output:
1

Explanation:

numberList[]=20,1,6,8,13,20,1,7,20,13,16,20
Subset Size=3

Non overlapping  subsets of size 3 are:
{20,1,6} {8,3,20} {1,7,20} {13,16,20}.
20 is present in every subset.
Hence output is 1.
'''
### Try this not done
# # import itertools
# # from itertools import combinations
# numberList=[]
# N=int(input())
# for i in range(N):
#     a=list(map(int,input()))
#     numberList.append(a)
# N2=int(input())
# S=int(input())
# print(numberList)
# # list1=list(map(set,itertools.combinations(numberList,S)))



