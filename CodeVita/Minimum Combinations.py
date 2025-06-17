'''
If in a question we have two or more unknown variables then those equation are
called Diophantine Equation.

Euclidean Algorithm for GCD

x and y are results for inputs a and b, a*x +b*y = gcd

Diophantine equation is a polynomial equation, usually in two or more unknowns, such that only
the integer solutions are sought or studied(an integer solution is such that
all the unknowns take integer values). A linea Diophantine equation equates the sum
of two or more monomials, each of degree 1 in one of the variables to a constant.
'''

def gcd(n1,n2):
    if n2==0:
        return n1
    return gcd(n2,n1%n2)

t=int(input())
result=[]
for i in range(t):
    n1,n2=map(int,input().split())
    # n1,n2=[int(x) for x in input().split()]#using list comprehension
    result.append(gcd(n1,n2))
for i in result:
    print(i,end=" ")
