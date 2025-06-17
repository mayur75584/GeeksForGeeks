
'Full question is given in chats of Adity Kubde on Instagram'
def func(s):
    s1=''
    s2=''
    for i in s:
        if i.isalpha():
            s1+=i
        elif i!=i.isalnum():
            if i.isdigit():
                pass
            else:
                s2+=i
    return s1+s2


if __name__ == '__main__':
    s=input()
    result=func(s)
    print(result)