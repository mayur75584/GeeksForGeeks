
'''
Kids up to the age of 7 are confused formation of letters and numbers, 
teacher uses the different methodologies to make the concepts of mathematics clear to the students. 
One of the methods the teacher uses to emphasis on the addition and recognition of numbers is that she muddles up 
the numbers randomly and then asks the students to find difference between adjacent digits. 
The task here to find given number is CORRECT or INCORRECT.

-> A number is correct if the difference between the adjacent(right and left)
digits is 1.
->The number can be a positive or a negative.

Example:
7876-Value of N
Output:
Correct

Explanation:
the inputs given above  
N=7876

Difference between the digits
7-8=1
8-7=1
7-6=1
6-7=1

The maximum difference between all adjacent digits is 1,hence
output is CORRECT
'''
def func(n):
    z=[]
    a=abs(n)
    while(a!=0):
        rem=a%10
        z.append(rem)
        a=a//10
    z=z[::-1]
    print(z)
    for i in range(len(z)):
        if i==len(z)-1:
            if abs(z[i]-z[i-1])==1:
                continue
            else:
                return "INCORRECT"
        else:
            if abs(z[i]-z[i+1])==1:
                continue
            else:
                return "INCORRECT"
    return "CORRECT"

if __name__ == '__main__':
    # n=int(input())
    # n=7876
    # n=-7876
    # n=-8987
    # n=8987
    # n=1011109
    # n=987
    n=-987
    res=func(n)
    print(res)

'''
JAVA Code

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int number;
    cin>>number;
    number=abs(number);

    int remainder1=number%10;
    number=number/10;
    while(number>0)
    {
        int remainder2=number%10;
        if(abs(remainder1-remainder2)==1)
        { remainder1=remainder2;
            number=number/10;
        }
        else
            break;
    }
    if(number>0)
        cout<<"INCORRECT";
    else
        cout<<"CORRECT";
    return 0;
}

'''