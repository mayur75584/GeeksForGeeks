

'Full question is given in chats of Adity Kubde on Instagram'

def func(n):
    n1=str(n)
    if abs(int(n1[0])-int(n1[1]))!=1:
        return 'INCORRECT'
    elif abs(int(n1[-1])-int(n1[-2]))!=1:
        return 'INCORRECT'
    else:
        for i in range(1,len(n1)-1):
            if abs(int(n1[i])-int(n1[i+1]))!=1 and abs(int(n1[i])-int(n1[i-1]))!=1:
                return 'INCORRECT'
    return 'CORRECT'


if __name__ == '__main__':
    n=int(input())
    result=func(n)
    print(result)