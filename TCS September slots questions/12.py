'''
A parking lot in a mall has RxC number of parking spaces. Each parking psace will either be  empty(0) or full(1). The status (0/1) of a parking space is represented as the element of the matrix. The task is to find index of the prpeinzta row(R) in the parking lot that has the most of the parking spaces full(1).

Note :

RxC- Size of the matrix

Elements of the matrix M should be only 0 or 1.

Example 1:

Input :

3   -> Value of R(row)

3        -> value of C(column)

[0 1 0 1 1 0 1 1 1] -> Elements of the array M[R][C] where each element is separated by new line.

Output :

3  -> Row 3 has maximum number of 1's

Example 2:

input :

4 -> Value of R(row)

3 -> Value of C(column)

[0 1 0 1 1 0 1 0 1 1 1 1] -> Elements of the array M[R][C]

Output :

4  -> Row 4 has maximum number of 1’s
'''



r=int(input())
c=int(input())
maxlst=[]
arr=[]
for i in range(r):
    z=[]
    for j in range(c):
        x=int(input())
        z.append(x)
    arr.append(z)
    x1=z.count(1)
    maxlst.append(x1)
result=maxlst.index(max(maxlst))
print(result+1)

'Prepinsta solution'
# r=int(input())
#
# c=int(input())
#
# sum=0
#
# m=0
#
# id=0
#
# for i in range(r):
#
#     for j in range(c):
#
#         sum+=int(input())
#
#     if sum>m:
#
#         m=sum
#
#         id=i+1
#
#     sum=0
#
# print(id)

