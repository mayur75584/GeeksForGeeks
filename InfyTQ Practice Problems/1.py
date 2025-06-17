L1=list(map(int,input().split(',')))
num1=sum((L1[:L1.index(4)]))+sum((L1[L1.index(7)+1:]))
lst=L1[L1.index(4):L1.index(7)+1]
print(lst)
num2=''
for i in lst:
    num2+=str(i)
print(int(num2)+num1)

### Below code is for if we want to add num1 and num2 as integers both
# L1=list(map(int,input().split(',')))
# num1=sum(L1[:L1.index(4)])+sum(L1[L1.index(7)+1:])
# num2=sum(L1[L1.index(4):L1.index(7)+1])
# print(num1+num2)
