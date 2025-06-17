'''
Delete Digit

Given some integer, find the maximal number you can obtain by deleteing
exactly one digit of the given number.

i/p-1

n=152,
o/p
52

i/p-2
n=1001
o/p
101

i/p-3
n=748541
o/p-
78541
'''

# n=int(input())
# n='152'
# n='1001'
n='748541'
a=[]
for i in range(len(n)):
    a.append(int(n[:i]+n[i+1:]))
print(a)
print(max(a))

