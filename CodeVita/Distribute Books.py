'''
Concept is De-arrangment in Permutations and Combinations

https://tutorialspoint.dev/algorithm/mathematical-algorithms/count-derangements-permutation-such-that-no-element-appears-in-its-original-position
Link for de-arrangement in permutations and combinations to understand

Formula -

D(n) = (n-1)*(D(n-1)+D(n-2))
where D will be function name
'''
'Dynamic Programming'

def countDer(n):

    D=[0 for i in range(n+1)]

    #Base conditions
    D[0]=1
    D[1]=0
    D[2]=1

    for i in range(3,n+1):
        D[i] = (i-1)*(D[i-1] + D[i-2])

    return D[n]

n=int(input())
print(countDer(n)%1000000007)







'Recursive'

# def D(n):
#     #Base conditons
#     if (n==1):
#         return 0
#     if (n==0):
#         return 1
#     if (n==2):
#         return 1
#
#     # Formula D(n) = (n-1)*(D(n-1)+D(n-2))
#     return (n-1)*(D(n-1) + D(n-2))
#
#
#
#
#
# n=int(input())
# print(D(n)%1000000007)