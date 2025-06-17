'''
    A man has money/coins in two different bags. He visits the market to buy some items.
    Bag A has N coins and bag B has M coins. The denominations of the money are given as array elements in a[] and b[].
    He can buy products of by paying an amount which is an even number by choosing money from both the bags.
    The task here is to find the number of ways the man can buy items such that the product of money from both the bags is an even number.

    The man has to pick one coin at least from each bag to make an even number product.

    Example1:
    Input:
    3-Value of N
    3-Value of M
    (1,2,3)-a[], Elements a[0] to a[N-1], where each input element is separated
    by new line.

    (5,6,7)-b[], Elements b[0] to b[N-1], where each input element is separated by
    new line.

    Output:
    5 - Number of ways
'''
def func(N,M,a,b):
    count1=0
    for i in a:
        for j in b:
            if (i*j)%2==0:
                count1+=1
    return count1



if __name__ == '__main__':
    N=int(input())
    M=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    res=func(N,M,a,b)
    print(res)