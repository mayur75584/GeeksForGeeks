'''
One kind of numbers is called strange numbers, which has the following
properties:

1- A strange number is an integer number 'N' which has factors that are
prime numbers.
2- The square root of the number 'N' should be less than the
greatest prime factor of 'N'.

The task here is to find out if the given number 'N' is 'Strange'
or 'Not Strange'.

Example1:

Input:
15-Value of N
Output:
Strange

Input:
25
Output:
Not Strange
'''
def func(n):
    z=n**0.5
    maxp=0
    prime=2

    while n>1:
        if n%prime==0:
            n=n//prime
            maxp=max(maxp,prime)
        else:
            prime+=1
    if z<maxp:
        return 'Strange'
    else:
        return 'Not Strange'


if __name__ == '__main__':
    n=int(input())
    result=func(n)
    print(result)