'''
Write a program to find the smallest integer value 'b' for the given
value of 'a'. If we multiply the digits of 'b', we should get the exact
value of 'a'. Result 'b' must contain more than one digit.

Constraints:
1<=a<=10000

examples:

Input:10
Output:25
Expla: 2*5=10

Input1:56
Output:78
Expla:7*8=56

Input2:150
Output:556
Expla:5*5*6=150

Input3:13
Output:Not Posiible

'''

def prime(n):
    for i in range(2,int(n/2)+1):
        if (n%i)==0:
            return False
    else:
        return True

def small(n):


    if n<10:
        print(n+10)
        exit()
    elif prime(n):
        print('NOT POSSIBLE')
        exit()
    else:
        lst=[]
        for i in range(9,1,-1):
            while(n%i==0):
                n=n//i
                lst.append(i)
        if n>10:
            print('NOT POSSIBLE')
            exit()
        return lst[::-1]




if __name__ == '__main__':
    # n=int(input())
    n=55
    # n=100
    # n=7
    # n=13
    # n=36
    result=small(n)
    s1=''
    for i in result:
        s1+=str(i)
    print(int(s1))