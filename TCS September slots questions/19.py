
'''
Ab ‘N’ number of customers are waiting at a restaurant that is recently opened. After every ‘M’ minutes , a new customer arrives at the restaurant. Due to the huge crowd, customers have to wait for their table at the restaurant. Only one customer is allowed at a time. The manager at the reception desk asks each customer to wait for ‘X‘ minutes to get their table. The task is to calculate the duration (in minutes) the last customer arrived needs to wait.

Example 1:

5      Value of N

3      Value of M

10     Value of X

Output :

28

Explanation:

Customers


Customer 1


Customer 2


Customer 3


Customer 4


Customer 5

Arrival time


0


3


6


9


12

Duration (min) customer can enter




10


20


30


40

Waiting time


0


7


14


21


28

The lasṭ customer arrives at the restauraṉt at the 12th minute, and he gets a table at 40 minutes. So, the total duration the last customer waited to get a table is 40-12=28 minutes.

Hence, the output is 28.

Example 2:

Input :

3     Value of N

5     Value of M

5    Value of X

Output :

0

Explanation:

Customers


Customer 1


Customer 2


Customer 3

Arrival time


0


5


10

Duration(min) customer can enter


0


5


10

Waiting time


0


0


0

The last customer arrives at the restaurant at the 10th minute, and he gets a table after 10 minutes. So, the total duration the last customer waited to get a table is 10-10=0. I.e. no need to wait.

Hence , the output is 0.

Constraints:

0<N<=50

0<M<=60

0<X<=60
'''

n=int(input())
m=int(input())
x=int(input())
a=[]
s=0
a.append(0)
z=0
x1=0
for i in range(1,n):
    z+=m
    x1+=x
    a.append(x1-z)
print(a[-1])

