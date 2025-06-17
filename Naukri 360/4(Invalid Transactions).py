'''
 Invalid Transactions
Moderate
80/80
Average time to solve is 30m
Contributed by
Asked in company
Problem statement
You are the manager of a bank. You have seen the database of the bank and have seen ‘N’ transactions. Each transaction has a customer id, transaction amount, time of the transaction, and the city code of the transaction. Now a transaction is invalid if the transaction amount exceeds Rs 1000 or the transaction occurs within 60 minutes of another transaction with the same customer id but in a different city. Find the number of invalid transactions.

Example:-
N = 3
TRANSACTIONS = [(1,20,100,1),(2,30,24,1),(1,60,90,2)]  [For the first transaction, customer_id is 1, the time of transaction is 20 minutes, the amount of transaction is Rs 100 and the city code where the transaction took place is 1, so the tuples are in the form (customer_id, time_fo_transaction, amount_of_transaction, city_code)].

ANSWER:- The invalid transactions are [(1,20,100,1),(1,60,90,2)] as the transactions are under the same customer id and have occurred in different cities within 60 minutes
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 10
1 <= N <= 10^3
1 <= CUST_ID <=10^9
1 <= TIME <= 10^9
1 <= AMOUNT <= 10^9
1 <= CITY <= 10^9

Time Limit = 1 sec
Sample Input 1 :
2
2
1 20 800 1
1 30 1200 1
2
2 30 1500 1
1 20 500 2
Sample Output 1 :
1 30 1200 1
2 30 1500 1
Explanation for Sample Output 1 :
In the first test case, the second transaction is invalid because the transaction amount exceeds Rs 1000.
 In the first test case, the first transaction is invalid because the transaction amount exceeds Rs 1000.
Sample Input 2 :
1
2
1 30 1500 1
1 20 500 2
Sample Output 2 :
1 30 1500 1
1 20 500 2
'''

from sys import *
from collections import *
from math import *

from typing import *

def invalid_transactions(transactions: List[Tuple[int,int,int,int]], n: int) -> List[int]:

# -> List[(int,int,int,int)]:
    # Write your code here.
    dict1={}
    ans=[]
    for i in transactions:
        if i[2]>1000:
            ans.append(i)
        if i[0] not in dict1:
            dict1[i[0]]=[i]
        else:
            x=dict1[i[0]][-1]
            # print("x",x)

            if x[-1]!=i[-1]:
                if x[1]>i[1]:
                    diff=x[1]-i[1]
                    if diff<=60:
                        ans.append(i)
                else:
                    diff=i[1]-x[1]
                    if diff<=60:
                        ans.append(i)
            dict1[i[0]].append(i)
    # print(dict1)
    return ans


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # n=2
        # transactions=[(1,20,800,1),(1,30,1200,1)]
        # n=2
        # transactions=[(2,30,1500,1),(1,20,500,2)]
        n=2
        transactions=[(1,30,1500,1),(1,20,500,2)]
        ans=invalid_transactions(transactions,n)
        print(ans)
