'''
2. Count of K digits:-
e.g. [1,2,22,3,34,899,112,3,44,552]
If K = 2:- toh 2 length wale numbers find krne hai(22,34,44) or iski length print
krwani ha i.e. 3(kyuki teen elements the)
'''

# list1=list(map(int,input().split(',')))
#
# list2=[]
# k=int(input())
# for i in list1:
#     if len(str(i))==k:
#         list2.append(i)
# print(len(list2))

###########################################################################

# list1=list(map(int,input().split()))

list1=[1,2,22,3,34,899,112,3,44,552]
k=2

counter=0
for i in list1:
    if len(str(i))==k:
        counter+=1
print(counter)