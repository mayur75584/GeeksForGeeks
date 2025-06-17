'''
There are ‘N’ number of houses in a village. Each house requires a voltage ‘V’ volts of electricity to power up their home appliances. In this context, the houses are arranged in the form of a matrix (row* columns) where ‘N’ is the order of the matrix. The amount of voltage supplied to each house is calculated as current(i)*voltage(r) where ‘i’ is the row number and ‘r’ is the column number. When the voltage supplied to the house (i*r) matches the value ‘V’, the appliances in the house can work. The task here is to find the number of houses whose voltage value(i*r) is the same as ‘V’. If none of the house’s value matches display a message “NO POWER”.

Example 1:

Input :

5      Value of N i.e. rows, columns=5

15    Value of V

Output :

2      number of houses whose i*r value matches

Explanation:

From the inputs given above

i=5, r=5

The below table represents values (i*r)

i/j


1


2


3


4


5

1


1


2


3


4


5

2


2


4


6


8


10

3


3


6


9


12


15

4


4


8


12


16


20

5


5


10


15


20


25

From the table above, we can deduce that the value v=15 occurs only in the houses(i,r)

(3,5) (5,3)

Hence, the output is 2.

Example 2:

Input :

3    Value of N i.e. rows=3, columns=3

10   Value of V

Output :
NO POWER   number of houses where i*r value matches V

Explanation:

From the inputs given above

i=3 r=3

The below table represents values (i*r)

i/j


1


2


3

1


1


2


3

2


2


4


6

3


3


6


9

From the table above, we can deduce that the value v=10 doesn’t match with the voltage in any of the houses.

Hence, the output is NO POWER

Constraints:

0<N<=50

0<V<=250

The input format for testing

The candidate has to write the code to accept 2 inputs

First input : Accept value for N (Positive integer number)

Second input : Accept value for V(positive integer number)

The output format for testing

The output should be a positive integer number or print the message (if any) given in the problem statement. (Check the output in Example 1, Example 2).


'''

n=int(input())
v=int(input())

a=[]
for i in range(1,n+1):
    z=[]
    for j in range(1,n+1):
        x=i*j
        z.append(x)
    a.append(z)
count=0
for i in range(n):
    for j in range(n):
        if a[i][j]==v:
            count+=1
if count==0:
    print("NO POWER")
else:
    print(count)