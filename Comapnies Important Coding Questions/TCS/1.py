'''
Write a program to find whether two strings contain equal set of characters or not.

Example1:

Input:-
elbow
below

Output:-
1

Example2:

Input:-
nice
china

Output:-
0
'''

str1= input()
str2 = input()
occ={}
occ1={}
for i in str1:
    occ[i]=occ.get(i,0)+1
# print(occ)
for j in str2:
    occ1[j]=occ1.get(j,0)+1
# print(occ1)

## Logic to compare two dictionary
# flag=0
# for x in occ:
#     if occ[x] != occ1[x]:
#         flag = 1
#         break
# if flag==0:
#     print(1)
# else:
#     print(0)

if(occ==occ1):
    print(1)
else:
    print(0)


######################################

# n1='nice'
# n2='china'
# n1=sorted(n1)
# n2=sorted(n2)
#
# d1={}
# d2={}
# for i in range(len(n1)):
#     d1[str(i)].app
# print(d1)
