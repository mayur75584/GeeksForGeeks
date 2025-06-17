'''
Note-> For such kind of questions mostly seen coders use recurrsion
'''
'Not Understood Solution'
'''
A ‘coin vend’ kiosk is installed all the major metro stations The machine allows one to obtain cash of ‘R’ rupees in exchange for coins.
The machine operates with the following conditions:
Only coins of denomination 1 rupee and 2 rupee can be exchanged.
Coins of denomination 2 rupees should not be inserted successively twice.
The task here to find all the possible combinations of the coins 
that can be inserted to get rupees from the kiosk Say, R=1, 
then only one coin of 1 rupee can be inserted to get 1 rupee


Example1:

Input:
3 - Value of R
Output:
3 - Different ways to insert the coins to get "R" rupees.


Explanation:
The possible way of inserting 1rs and 2rs coins for 3rs in cash
are 
Way1:(1,1,1)
Way2:(2,1)
Way3:(1,2)

Example2:
Input:
5-Value of R
Output:
6-Different ways to insert the coins to get "R" rupees.

Explanation:

Way1:(1,1,1,1,1,1)
Way2:(2,1,1,1)
Way3:(1,1,1,2)
Way4:(1,1,2,1)
Way5:(1,2,1,1)
Way6:(2,1,2)

Constraints:
0<R<=50

Input format for testing:
The candidate has to write the code to accept 1 input-
Accept value for N(positive integer number)

Output format for testing:
The output should be a positive integer number
(Check the output in Example 1 and Example 2).
'''
def CountCoin(R):
    if R==0:
        return 1
    if R==1:
        return 1
    if R==2:
        return 1+1
    return CountCoin(R-1)+CountCoin(R-3)



if __name__ == '__main__':
    R=int(input())
    print(CountCoin(R))