

'''
Brute Force Approch for Buy and Sell Problem

Time Complexity of O(N^2)
'''
'''
First Buy
Second Sell
You need to Buy the Stock Before Selling
MAX Profit should be there
'''


def bruteforce(A):
    n=len(A)
    maxprofit = 0
    for i in range(n): #buy
        for j in range(i+1,n): #sell
            if A[j]>A[i]:
                maxprofit = max(maxprofit, A[j]-A[i])
    print(maxprofit)


testcase=[7,1,5,3,6,4]
bruteforce(testcase)