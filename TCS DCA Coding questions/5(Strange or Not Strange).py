'''
    Numbers are everywhere around us. We deal with different types of numbers on a daily basis
    There are numbers, whole numbe natural numbers, etc. Another kind a numbers is called strange numbers,
    which the following properties :
    A strange number is an integer number N’ which has factors that are prime numbers.

    The square root of the number ‘N’ should be less than the greatest prime factor of ‘N’.

    The task here is to find out if the given number ‘N’ is strange or Not Strange.

    Example 1:
    Input:
    15 - Value of N
    Output:
    Strange

    Explanation:
    From the inputs given above N=15
    The prime factors of N are 5,3
    The greatest prime factor if 5.
    The square root of 15 is 3.87 and 3.87<5(The greatest prime factor)

    Hence the output is Strange.

    Example2:
    Input:
    25- Value of N
    Output:
    Not Strange

    Explanation:
    From the inputs given above:
    N=25
    The prime factor of N is 5.
    The greatest prime factor is 5.Hence, the output is
    Not Strange.
    The Square root of 25 is 5 which is not less than 5 the greatest prime factor
    of N
    Hence the output is not Strange.

    Constraints
    0<N<100
    The input format for testing. The candidate has to write the code to accept 1 input.

    Output: Should be string check above example 1 and 2.
'''
import math
def isprime(p):
    flag=False
    for i in range(2,p):
        if (p%i)==0:
            flag=True
            break
    if flag==True:
        return False
    else:
        return True

def func(n):
    z=[]
    for i in range(2,n):
        if n%i==0:
            if isprime(i):
                z.append(i)
    max1=max(z)
    sq=math.sqrt(n)
    if sq<max1:
        return "Strange"
    else:
        return "Not Strange"


if __name__ == '__main__':
    n=int(input())
    # n=15
    # n=25
    # n=49
    # n=56
    res=func(n)
    print(res)


'''
import math
def PrimeFactor(num):
    while num % 2 == 0:
        max_Prime = 2
        num /= 10
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            max_Prime = i
            num = num / i
    if num > 2:
        max_Prime = num
    return int(max_Prime)


# num = int(input())
num=56
# num=5
prime = PrimeFactor(num)
if prime > math.sqrt(num):
    print("Strange")
else:
    print("Not Strange")

'''