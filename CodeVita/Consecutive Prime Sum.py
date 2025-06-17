t=int(input())
# t=1
for i in range(t):
    n=int(input())
    # n=20
    # n=1000
    # n=100
    lst=[]
    #Logic to generate prime number list
    for j in range(2,n):
        for k in range(2,j):
            if j%k==0:
                break
        else:
            lst.append(j)
    # print(lst)
    sum1=0
    count=0
    #Logic to find out those prime numbers whose consecutive sum of prime number is that prime number
    for i in range(1,len(lst)):
        for j in range(len(lst)):
            sum1+=lst[j]
            if sum1>lst[i]: #this if condition is used to reduced complexity without this answer will be same
                break
            if sum1==lst[i]:
                # print(sum1)
                count+=1
                break
        sum1=0
    print(count)

########### Mam's Solution
# n=int(input())
# primes=[]
# count=0
# #List comprehension to find primes numbers upto given number
# primes=[i for i in range(2,n+1) if all(i%j !=0 for j in range(2,int(i**0.5)+1))]
#
# for i in range(2,len(primes)):
#     sum=0
#     for j in primes:
#         sum+=j
#         if sum == primes[i]:
#             count+=1
#             break
#         if sum>primes[i]:
#             break
# print(count)



