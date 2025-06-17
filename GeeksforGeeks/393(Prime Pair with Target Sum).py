'''
from math import sqrt

class Solution:

    # def isPrime(self,n):
    #     flag=False
    #
    #     if(n>1):
    #         for i in range(2,int(sqrt(n))+1):
    #             if(n%i==0):
    #                 flag=True
    #                 break
    #         if(flag==False):
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False
    def SieveOfEratosthenes(self,num):
        # prime = [True for i in range(num + 1)]
        prime=[True]*(num+1)
        prime[0]=prime[1]=False
        prime1=[]
        # boolean array
        p = 2
        while (p * p <= num):

            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):

                # Updating all multiples of p
                # for i in range(p * p, num + 1, p):
                #     prime[i] = False
                i=p*p
                while(i<=num):
                    prime[i]=False
                    i+=p
            p += 1

        # Print all prime numbers
        for p in range(2, num + 1):
            if prime[p]:
                prime1.append(p)
        return prime
    def getPrimes(self,n):
        # res=[]
        # if n>1:
        #     # for i in range(2,n+1):
        #         # if(self.isPrime(i)):
        #         #     a.append(i)
        #
        #     # print(a)
        #     # if n%2==0:
        #     for i in range(len(primes)):
        #         a1=primes[i]
        #         if n-a1 in primes[i+1:]:
        #             return [a1,n-a1]
        #     for i in range(len(primes)):
        #         a1=primes[i]
        #         if i==len(primes)-1:
        #             if(primes[i]+primes[i]==n):
        #                 res.append([primes[i],primes[i]])
        #         elif(n-a1 in primes[i+1:]):
        #             ans=[a1,n-a1]
        #             if ((ans not in res) and (ans[::-1] not in res)):
        #                 res.append(ans)
        #             return ans
        #         elif(a1+a1==n):
        #                 res.append([a1,a1])
        #     # res=sorted(res,key=lambda x:x[0])
        #     # print(res)
        #     if len(res)==0:
        #         return [-1,-1]
        #     return res[0]
        #
        # else:
        #     return [-1,-1]
'''
'''
Above solution will not passed all the test cases.
'''
class Solution:
    def SieveOfEratosthenes(self,num):
        # prime = [True for i in range(num + 1)]
        prime=[True]*(num+1)
        prime[0]=prime[1]=False
        prime1=[]
        # boolean array
        p = 2
        while (p * p <= num):

            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):

                # Updating all multiples of p
                # for i in range(p * p, num + 1, p):
                #     prime[i] = False
                i=p*p
                while(i<=num):
                    prime[i]=False
                    i+=p
            p += 1

        # Print all prime numbers
        for p in range(2, num + 1):
            if prime[p]:
                prime1.append(p)
        return prime
    def getPrimes(self,n):
        primes=self.SieveOfEratosthenes(n)
        # print(primes)
        for i in range(len(primes)):
            if(primes[i] and primes[n-i]):
                return [i,n-i]
        return [-1,-1]

class IntArray:
    def __init__(self):
        pass

    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]
        return arr

    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # n=10
        # n=8
        # n=3
        n=72
        obj=Solution()
        res=obj.getPrimes(n)

        IntArray().Print(res)