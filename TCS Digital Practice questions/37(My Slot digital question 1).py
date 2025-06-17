'''
Solution to the problem

https://www.geeksforgeeks.org/minimize-operations-to-reduce-n-to-0-by-replacing-n-by-its-divisor-at-each-step/?ref=gcse
'''
'''
Rahul, a mathematical genius, will be given a positive number N and he needs
to reduce it to 0(zero) by following operations mentioned as under:
Take one of the divisors of N - which is different from N itself- and
subtract it from N.
Perform the above operation till the original number is reduced to 0(zero).

The task here is to find the minimum number of steps Rahul needs to perform
such that N is reduced to 0(zero).

Note:
    If the N is 1 during the operation, then in order to reduce
    1 to 0(zero), subtract 1 from it.
    Is is shown in following examples 1,2 and 3.

Example:
Input:
5  -> Input integer N
Output:
4
Explanation:
Divisors of 5 are 1,5 but you cannot subtract 5 so then
subtract 1 from 5
The reduced number is 5-1=4
Divisors of 4 are 1,2 and 4 but you cannot subtract 4 so reduce it by
2, after reducing it by 2, number becomes 4-2=2
Divisors of 2 are 1,2 and after reducing it by 1,number becomes
2-1=1

You can subtract 1 by 1 and then the number becomes 0.
So, for N=5, the minimum number of steps are 4.

Example2:
Input:
8   ->Input integer, N
Output:
4
Explanation:
In first step, subtract 4 from 8, number becomes 8-4=4
In second step, subtract 2 from 4, number becomes 4-2=2
In third step subtract 1 from 2, number becomes 2-1=1
In fourth step, subtract 1 from 1, number becomes 1-1=0.

Example3:
Input:
6    ->Input integer, N
Output:
4
Explanation:
In first step, subtract 2 from 6, number becomes 6-2=4
In second step, subtract 2 from 4, number becomes 4-2=2
In third step, subtract 1 from 2 number becomes 2-1=1
In fourth step subtract 1 from 1 number becomes 1-1=0

Constraints:
1<=N<=500

The input format for testing
First Line: Contains a positive integer N.

The output format for testing:
Output a single integer denoting the minimum number of
steps to reduce the given number to 0(zero).

Additional message in output will cause the failure of test cases.

Instructions:
The system does not allow any kind of hard-coded input value/values.
Written program code by the candidate will be verified against the
inputs which are supplied from the system.
'''


'Not sure whether the code is correct or not but based on the observations is written the code'

def divisors(d):
    divs=[1]
    for i in range(2,int(d**0.5)+1):
        if d%i==0:
            divs.append(i)
            divs.append(d//i)
        # divs.append(d)
    return divs

def func(N):
    if N<0:
        return -1
    count1=0
    while(N!=0):
        z=divisors(N)
        z.sort(reverse=True)
        for i in range(len(z)):
            if z[i]!=N and z[i]%2==0:
                N-=z[i]
                count1+=1
                break
            elif len(z)==1 and z[0]==1:
                N-=z[0]
                count1+=1
                break
    return count1

if __name__ == '__main__':
    # N=int(input())
    # N=5
    # N=8
    N=6
    res=func(N)
    print(res)

'Correct Solution'


# Python3 program to minimize operations
# to reduce N to 0 by replacing N by its
# divisor at each step

# function to find the element
def findElement(N):
    i = 2
    while i * i <= N:
        if N % i == 0:
            return int(N / i)
        i += 1
    return 1


# function to count the min number of operations
def minOperations(N):
    if N < 0:
        return -1
    count = 0
    while N:
        divisor = findElement(N)
        N -= divisor
        count += 1
    return count


# Driver Code
N = 5
print(minOperations(N))

'Correct efficient solution'

# Python3 code to implement the above approach

MAX = 10000001


def makeSieve():
    sieve = [0] * MAX
    sieve[1] = 1
    for i in range(2, 1 + int(MAX ** 0.5)):
        if not sieve[i]:
            sieve[i] = i
            for j in range(i ** 2, MAX):
                if not sieve[j]:
                    sieve[j] = i
    for i in range(2, MAX):
        if not sieve[i]:
            sieve[i] = 1
        else:
            sieve[i] = (i // sieve[i])
    return sieve


def minOperations(N):
    if N < 0:
        return -1
    count = 0
    sieve = makeSieve()
    while N > 0:
        N -= (sieve[N])
        count += 1
    return count


# Driver Code
N = 8
print(minOperations(N))