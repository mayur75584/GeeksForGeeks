'Minimal Sum'

def func(arr,n):
    if sorted(arr)==sorted(set(arr)):
        return sum(arr)
    else:
        lst=[]
        lst1=[]
        for i in arr:
            if i not in lst:
                lst.append(i)
            else:
                lst1.append(i)
        for i in lst1:
            # while i+1 not in lst:
            while True:
                if i+1 not in lst:
                    lst.append(i+1)
                    break
                else:
                    i+=1
        print(lst)
        return sum(lst)




if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input()))
    while True:
        z=input()
        if z.isdigit():
            arr.append(int(z))
        else:
            break
    if len(arr)!=n:
        print('Wrong Input')
    else:
        result=func(arr,n)
        print(result)