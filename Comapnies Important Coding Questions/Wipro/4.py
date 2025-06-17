'''
4.
A Pythagorean triplet is a set of three integers a, b and c such that a^2+ b^2 = c^2
.
Given a limit, generate all Pythagorean Triples with values smaller than given limit.
Input : limit = 20
Output :
 3 4 5
 8 6 10
 5 12 13
 15 8 17
 12 16 20
'''


#### Not correct
num1=int(input())
for i in range(1,num1+1):
    for j in range(1,num1+1):
        for k in range(1,num1+1):
            if (i**2)+(j**2)==(k**2):


                print(i,' ',j,' ',k)

