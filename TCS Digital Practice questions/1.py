


s=input()
a=s
b=s[::-1]
# xf=''
# xb=''
z=s[0]
s1=a.replace(z,'',1)
xb=s1+z
z1=s[-1]
s2=b.replace(z1,'',1)
xf=z1+s2[::-1]
print(xf)
print(xb)
if xf==xb:
    print(1)
else:
    print(0)
