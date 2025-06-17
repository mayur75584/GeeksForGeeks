'''
Program to reverse a string after removing duplicates.

Input:
infosys

Output:
ysofni

Input:
google

Output:
elog
'''
# s1=input()
# out_str=''
#
# for i in s1:
#     if i not in out_str:
#         out_str+=i
# print(out_str[::-1])

##########################################################3
'not complete see mams code'
a='google'
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=i

a = list(d.keys)

