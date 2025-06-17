'''
Buy and Sell Problem

Time Complexity - O(N)
'''

def optimal(A):
    n=len(A)
    maxprofit = 0
    minprice = float('inf')

    for i in range(n):
        minprice = min(minprice, A[i]) # to maintain min price
        maxprofit = max(maxprofit, A[i]-minprice) # to maintain max profit
    print(maxprofit)

testcase = [7,1,5,3,6,4]
optimal(testcase)