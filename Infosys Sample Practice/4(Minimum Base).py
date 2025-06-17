'''
Given a number M in its decimal representation, your task is find
the minimum base B such that in the representation of M at
base B all digits are the same.

Input Format:
The first line contains an integer, M , denoting the number given

Constratints

1<=M<= 10^12

Sample Input1:
41

Sample Output1:
40

Explanation:

Here 41 in base 40, will be 11 so it has all digits the same, and there
is no smaller base satisfying the requirements.

Sample Input2:
34430

Sample Output2:
312

Explanation:

Here 34430 in base 312 will have all digits the same and there
is no smaller base satisfying the requirements.

Sample Input3:
35

Sample Output3:
6

Sample Input4:
4524

Sample Output4:
77
'''

def sameDigitsOrNot(number,base):
    rem=number%base
    number=number//base

    while(number>=base and number%base==rem):
        number=number//base

    if number==rem:
        return True
    else:
        return False




if __name__ == '__main__':

    number=int(input())
    base=2

    while(not sameDigitsOrNot(number,base)):
        base=base+1
    print(base)

