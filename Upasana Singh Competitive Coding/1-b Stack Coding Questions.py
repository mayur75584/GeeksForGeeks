'''
Stock Span Problem

The stock span problem is a financial problem where we have
a series of n daily price quotes for a stock and we need to calculate span
of stocks price for all n days.

The span Si of the stock's price on a given day i is defined as the
maximum number of consecutive days just before the given day, for which the price
of the stock on the current day is less than its price on the given day.

For example, if an array of 7 days prices is given as [100,80,60,70,60,75,85]
then the span values for corresponding 7 days are [1,1,1,2,1,4,6].


'''

def calculateSpan(price,n,S):
    stack=[]
    stack.append(0)
    S[0]=1
    for i in range(1,n):
        while(len(stack)!=0 and price[stack[-1]]<=price[i]):
            stack.pop(-1)
        if len(stack)==0:
            S[i]=i+1
        else:
            S[i]=i-stack[-1]

        stack.append(i)

def printArray(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
if __name__ == '__main__':
    # price=[10,4,5,90,120,80]
    price=[100,80,60,70,60,75,85]
    n=len(price)
    S=[0]*n

    calculateSpan(price,n,S)

    printArray(S,n)
