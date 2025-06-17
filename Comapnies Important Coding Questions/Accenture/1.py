'''
1. Find all the continues combinations
e.g. 1215598
1, 12, 121, 1215, 12155, 121559, 1215598,
2, 21, 215, 2155, 21559, 215598,
1, 15, 155, 1559, 15598,
5, 55, 559, 5598,
5, 59, 598,
9, 98,
8
'''

n=int(input())
n=str(n)
m=len(n)
for i in range(1,m+1):
    s1 , s = '' , ''
    for j in range(i-1,m):
        s1=s+n[j]
        s =s1
        print(s,end=", ")
    print(end="\n")

##################################

'Below Output was needed means real question was to add those elements who is divided by 2 in list.'
# arr='1215598'
# list1=[]
# for i in range(0,len(arr)):
#     comb=''
#     for j in range(i,len(arr)):
#         comb = comb + arr[j]
#         if int(comb)%2==0:
#             list1.append(int(comb))
# print(list1)





