'''
3. Autobiographical Number
e.g. If Input is Null print 0,
 Else print the length of distinct elements of a string
Input = ‘Anchal’
Distinct elements = a,n,c,h,l = no of elements = 5
Output = 5
'''
#
# str1=input()
# str2=''
# str1=str1.lower()
# # print(str1)
# if str1=='':
#     print(0)
#     exit()
# else:
#     for i in str1:
#         if i not in str2:
#             str2+=i
# print(len(str2))

##############################################################
'In python Null is not there , in python Null means None'
a = input()
if a==None:
    print(0)
    exit()
else:
    print(len(set(a.lower())))

