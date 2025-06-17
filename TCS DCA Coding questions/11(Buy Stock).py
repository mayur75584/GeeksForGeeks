'''
You are given an array prices where prices[i] is the price of a given
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one
stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.If you cannot
achieve any profit, return 0.

Example1:
Input: prices=[7,1,5,3,6,4]
Output: 5
Explanation:
Buy on day 2(price=1) and sell on day 5(price=6), profit=6-1=5.
Note that buying on day 2 and selling on day1 is not allowed because
you must buy before you sell.

Example2:
Input : prices=[7,6,4,3,1]
Output: 0
Explanation: In this, case no transaction are done and the max profit=0.
'''

# prices=list(map(int,input().split()))
# prices=[7,1,5,3,6,4]
prices=[7,6,4,3,1]
n=len(prices)
profit=0
for i in range(n):
    mx=0
    for j in range(i+1,n):
        if(prices[j]>prices[i]):
            mx=max(mx,prices[j])
    profit=max(profit,mx-prices[i])
print(profit)