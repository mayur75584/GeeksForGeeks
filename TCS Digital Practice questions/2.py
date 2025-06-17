s=input()
num=''
s1=''
for i in s:
    if i.isnumeric():
        num+=i
    else:
        s1+=i
if int(num)==len(s1):
    print('TRUE',end=' ')
    print(len(s1))
else:
    print('FALSE',end=' ')
    print(len(s1))


