'''
File Naming
Taken screenshot

names=["doc","doc","image","doc(1)","doc"],
o/p
filename(names) = ["doc","doc(1)","images","doc(1)(1)","doc(2)"]
'''
# names=list(map(str,input().split()))
names=["doc","doc","image","doc(1)","doc"]
for i in range(len(names)):
    if names[i] in names[:i]:
        j=1
        while((names[i] + '(' + str(j) + ')') in names[:i]):
            j+=1

        names[i] = names[i]+'('+str(j)+')'
print(names)


