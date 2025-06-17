'''
Kth Largest Factor of number N

Given two positive integers N and K, the task is to print the Kth
largest factor of N.

Input: N=30,K=2
Output: 15
Explanation: The factors of 30 are {1,2,3,5,6,10,15,30} and the 2nd
largest factor is 15.
'''

def KthLargestFactor(N,K):
    if K==1:
        return 1

    for i in range(N//2,-1,-1):
        if(N%i==0):
            K-=1

        if(K==1):
            return i
    return -1


if __name__ == '__main__':
    # N,K=map(int,input().split())
    # N,K=30,2
    # N,K=30,3
    # N,K=30,7
    N,K=30,8
    print(KthLargestFactor(N,K))


