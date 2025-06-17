'''
isBeautifulString

A string is said to be beautiful if each letter in the string
appears at most as many times as the previous letter in the alphabet
within the string i.e b occurs no more times than a;
c occurs no more times than b;etc.

i/p-1
bbbaacdafe
o/p-
True
Exp:
string contains 3 a,3 b,1 c,1 d,1 e and 1 f
3>=3>=1>=1>=1>=1

i/p-2
aabbb
o/p
False
Exp:
string contains 3 b and 2 a
as a<3

'''
# n=input()
n='bbbaacdafe'
out=[0]*26
for i in n:
    out[ord(i)-ord('a')]+=1
print(out)
for j in range(1,len(out)):
    if out[j-1]<out[j]:
        print('False')
        break
else:
    print('True')

