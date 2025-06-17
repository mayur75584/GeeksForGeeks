input_num=input()
length_num=len(input_num)
result=""
for i in range(1,length_num,2):
    result+=str(int(input_num[i])**2)
print(result[:4])


