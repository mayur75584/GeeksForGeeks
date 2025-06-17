'''
Occurences of 2 as a digit

Count the number of 2s as digit in all numbers from 0 to n.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains the input integer n.

Output:
Print the count of the number of 2s as digit in all numbers from 0 to n.

Constraints:
1<=T<=100
1<=N<=10^5

Example:
Input:
2
22
100

Output:
6
20
'''

def numberOf2sinRange(n):
    count=0
    for i in range(2,n+1):
        if '2' in str(i):
            z=str(i).count('2')
            count+=z
    return count

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        n=22
        print(numberOf2sinRange(n))