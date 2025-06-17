'English school teacher/ Maximum word from sentence'

'With special charcaters'

s=input()
max=0
count=0
for i in range(len(s)):
    if s[i]==' ':
        if max<count:
            max=count
        count=0
    else:
        count+=1
if max<count:
    max=count
print(max)

'Without special characters'
# s=input()
# # s='Knowledge is the greatest gift'
# # s='er45 ghj&& ghjy'
# max=0
# count=0
# for i in range(len(s)):
#     # if s[i]==' ':
#     #     if max<count:
#     #         max=count
#     #     count=0
#     if (s[i]!=' ') and ((s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<'Z')):
#         count+=1
#     else:
#         if max<count:
#             max=count
#         count=0
# if max<count:
#     max=count
# print(max)
