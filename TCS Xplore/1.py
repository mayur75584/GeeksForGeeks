'Valid String and Invalid String'

def validInvalid(n,arr):
    count1=0
    count2=0
    for i in arr:
        z=i.replace(' ','')
        if z.isalpha():
            count1+=1
        else:
            count2+=1
    print('Count of Valid Strings=',count1)
    print('Count of Invalid Strings=',count2)





if __name__ == '__main__':
    n=int(input())
    arr=[]
    for i in range(n):
        s=input()
        arr.append(s)
    # n=4
    # arr=['Hello Good Morning','abcd123Fghy','India','progoti.c']
    validInvalid(n,arr)