
'''

Given an array of N integers where Ai denotes the currency of not that
the ith person has. The possible currencies are 5,10 and 20. All
the N people are standing in a queue waiting to buy an ice cream
from X which costs Rs5. Initially , X has an initial balance of 0.
Check if X will be able to provide change for all people who are
waiting to buy ice cream.

Input:
a=[5,5,5,10,20]
Output:
YES

Input:
a=[5,10,10,20]
Output:
NO

Input:
a=[5,10,5,20]
Output:
YES
'''
def func(a):
    dict={5:0,10:0,20:0}
    if a[0]>5:
        return 'NO'
    elif a[0]==5:
        dict[5]+=1
        for i in range(1,len(a)):
            if a[i]==5:
                dict[5]+=1
            elif a[i]==10:
                z=dict[5]
                if z>0:
                    dict[5]-=1
                    dict[10]+=1
                else:
                    return 'NO'
            elif a[i]==20:
                x,y=dict[5],dict[10]
                if x>0 and y>0:
                    dict[20]+=1
                    dict[10]-=1
                    dict[5]-=1
                elif x>=3:
                    dict[20]+=1
                    dict[5]-=3
                else:
                    return 'NO'
        return 'YES'

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # a=list(map(int,input().split()))
        # a=[5,5,5,10,20]
        # a=[5,10,10,20]
        # a=[10]
        # a=[5,10,5,20]
        a=[5,5,10,20]
        res=func(a)
        print(res)

# C++ code
'''
#include <bits/stdc++.h>
using namespace std;

int isChangeable(int notes[],int n)
{
    int fiveCount = 0;
    int tenCount = 0;
    
    for(int i=0;i<n;i++)
    {
        if(notes[i]==5)
        {
            fiveCount++;
        }
        else if(notes[i]==10)
        {
            if (fiveCount>0)
            {
                fiveCount--;
                tenCount++;
            }
            else
            {
                return 0;
            }
        }
        else
        {
            if(fiveCount > 0 && tenCount > 0)
            {
                fiveCount--;
                tenCount--;
            }
            else if(fiveCount>=3)
            {
                fiveCount-=3;
            }
            else
            {
                return 0;
            }
        }
        
    }
    return 1;
}

int main()
{
    int a[]={5,5,5,10,20};
    int n=sizeof(a)/sizeof(a[0]);
    
    if(isChangeable(a,n))
    {
        cout<<"YES";
    }
    else
    {
        cout<<"NO";
    }
    return 0;
}
'''