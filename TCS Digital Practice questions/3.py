
n=int(input())
z=str(n**2)
print(z)
# print(z)
x=len(str(n))
print(z[-x:])
if n==int(z[-x:]):
    print('Yes')
else:
    print('NO')

