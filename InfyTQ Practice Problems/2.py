# input_str=input()
# out_str=''
# for i in input_str:
#     if i not in out_str:
#         out_str+=i
# print(out_str[::-1])

##Method2

input_str=input()
d=list(dict.fromkeys(input_str))
# print(d)
d.reverse()
print("".join(d))