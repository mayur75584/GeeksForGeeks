'Airport Security/ Sorting'


n=int(input())
arr=[]
for i in range(n):
    z=int(input())
    arr.append(z)
arr0=[]
arr1=[]
arr2=[]
for i in arr:
    if i==0:
        arr0.append(i)
    elif i==1:
        arr1.append(i)
    elif i==2:
        arr2.append(i)
z=arr0+arr1+arr2
print(*z)