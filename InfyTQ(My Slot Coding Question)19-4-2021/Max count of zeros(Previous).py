

def func1(innum,inbase):
    output=''
    while innum>0:
        d=int(innum%inbase)
        if d<10:
            output+=str(d)
        else:
            output+=chr(ord('A')+d-10)
        innum=innum//inbase
    output=output[::-1]
    return output


#Driver code

# innum=int(input())
# inbase=int(input())
innum=68
inbase=2
ans=func1(innum,inbase)

counter=0

for i in range(len(ans)-1):
    if ans[i]=='0' and ans[i+1]=='0':
        counter+=1
if counter==0:
    print('-1')
else:
    print(counter)