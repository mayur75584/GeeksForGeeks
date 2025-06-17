'''
You have been given a string S of length N. The given string is a binary string which consists of only 0’s and ‘1’s. Ugliness of a string is defined as the decimal   number that this binary string represents.

 Example:

“101” represents 5.
“0000” represents 0.
“01010” represents 10.
 There are two types of operations that can be performed on the given string.

Swap any two characters by paying a cost of A coins.
Flip any character by paying a cost of B coins
flipping a character means converting a ‘1’to a ‘0’or converting a ‘0’ to a ‘1’.
  Initially, you have been given coins equal to the value defined in CASH. Your task is to minimize the ugliness of the string by performing the above mentioned          operations on it. Since the answer can be very large, return the answer modulo 10^9+7.

  Note:

You can perform an operation only if you have enough number of coins to perform it.
After every operation the number of coins get deducted by the cost for that operation.
  Input Format

The first line contains an integer, N, denoting the number of character in the string
The next line contains a string, S, denoting the the binary string
The next line contains an integer, CASH, denoting the total number of coins present initially
Next will contains an integer, A, denoting the cost to swap two characters.
Then the next line contains an integer, B, denoting the cost to flip a character.
   Constraints

1 <= N <= 10^5
1< len(S)<= 10^5
1<=CASH <=10^5
1<=A<=10^5
1<=B<=10^5
  Sample Input 1 :

  4

  1111

  7

  1

  2

  Sample Output 1 :

  1

  Explanation:

   3 flips can be used to create “0001” which represents 1.

  Sample Input 2:

  6

  111011

  7

  1

  3

  Sample Output 2:

  7

  Explanation:

  First swap 0 with the most significant 1, then use flip twice first on index one and then on index two “111011”=>”0111111″=>”001111″=>”000111″ the value            represented is 7.

  Sample Input 3:

  6

  111011

  7

  3

  2

  Sample Output 3:

  3

 Explanation:

 Flip the 3 most significant characters to get “000011” : the value represented by this string is 3.N
'''
def swap(s,A,cash):
    i=0
    for x in range(len(s)):
        if s[x]=='1':
            i=x
            break
    j=len(s)-1
    while(j>i):
        if (cash<A):
            break
        if(s[j]=='0'):
            if(s[i]=='0'):
                i+=1
            else:
                # s=s.replace(s[i],s[j],1)
                # s=s.replace(s[j],s[i],1)
                s[i],s[j]=s[j],s[i]
                cash-=A
                j-=1
        else:
            j-=1
    return s




def flip(s,B,cash):
    i=0
    for x in range(len(s)):
        if s[x]=='1':
            i=x
            break
    while(cash>=B):
        if(i==len(s)-1):
            break
        if(s[i]=='1'):
            # s=s.replace(s[i],'0',1)
            s[i]='0'
            i+=1
            cash-=B
    return s


def mini(s,cash,A,B):
    s1=[]
    for i in s:
        s1.append(i)

    if A<B:
        s1=swap(s1,A,cash)
        s1=flip(s1,B,cash)
    else:
        s1=flip(s1,B,cash)
        s1=swap(s1,A,cash)
    x=''.join(s1)
    return int(x,2)

if __name__ == '__main__':
    # n=int(input())
    # s=input()
    # cash=int(input())
    # A=int(input())
    # B=int(input())
    n=6
    s='111011'
    cash=7
    A=3
    B=2
    # n=4
    # s='1111'
    # cash=7
    # A=1
    # B=2
    # n=6
    # s='111011'
    # cash=7
    # A=1
    # B=3
    result=mini(s,cash,A,B)
    print(result)