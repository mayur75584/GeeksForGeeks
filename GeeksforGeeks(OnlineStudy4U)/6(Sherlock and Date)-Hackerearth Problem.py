'''
Sherlock and Date

Problem

Watson gives a date to Sherlock and asks him what is the date on the previous day.
Help Sherlock. You are given date in DD MM YYYY format. DD is an integer without leading zeroes.
MM is one of the "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November" and "December" (all quotes for clarity).
YYYY is also an integer between 1600 and 2000 without leading zeroes. You have to print the date of the previous day in same format.

Input and Output
First line, T (≤ 100), the number of testcases. Each testcase consists of date in specified format.
For each testcase, print the required answer in one line. Given date will be a valid date.
Sample Input

3
23 July 1914
2 August 2000
5 November 1999

Sample Output

22 July 1914
1 August 2000
4 November 1999

Time Limit: 2
Memory Limit: 256
Source Limit:
'''
'Note-> All the test case are not passing in python code but c++ code is running successfully'

'''
C++ Code


#include<iostream>
using namespace std;

int isLeapYear(int year)
{
    if((year%4==0)&&(year%100!=0) || (year%400==0))
        return 1;
    else
        return 0;
}
void previousDay(int d, string m , int y)
{
    string MONTHS[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November" , "December"};
    int DAYS[] = {31,28,31,30,31,30,31,31,30,31,30,31};

    if(d==1)
    {
        if(m=="January")
        {
            y--;
            printf("31 December %d\n",y);
        }
        else
        {
            int index;
            for(int i=0;i<12;i++)
            {
                if(m==MONTHS[i])
                {
                    index = i;
                    break;
                }
            }
            index--;
            int newD = DAYS[index];
            if(isLeapYear(y) && m=="March")
                newD++;

            cout<<newD<<" "<<MONTHS[index]<<" "<<y<<"\n";
        }
    }
    else
    {
        d--;
        cout<<d<<" "<<m<<" "<<y<<"\n";
    }
}

int main()
{
    int T;
    cin>>T;

    for(int i=0;i<T;i++)
    {
        int d,y;
        string m;
        cin>>d>>m>>y;

        previousDay(d,m,y);
    }
}

'''


def isLeapYear(year):
    if ((year%4==0 and year%100!=0) or year%400==0):
        return 1
    else:
        return 0

def previousDay(date,month,year):
    m=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November" , "December"]
    d=[31,28,31,30,31,30,31,31,30,31,30,31]
    lst=[]
    if date==1:
        if month=="January": #New year
            year-=1
            d=31
            m="December"
            lst.append(d)
            lst.append(m)
            lst.append(year)

        else: #Date is 1 and month is not January
            index=0
            for i in range(0,12):
                if month==m[i]:
                    index=i
                    break
            # print(index)
            # month=m[index-1]
            index-=1

            date1=d[index]
            if(isLeapYear(year) and month=="March"):
                date1+=1
            lst.append(date1)
            lst.append(month)
            lst.append(year)

    else:
        date-=1
        lst.append(date)
        lst.append(month)
        lst.append(year)

    print(*lst)




t=int(input())
# t=1
for i in range(t):
    date,month,year=map(str,input().strip().split())
    date=int(date)
    year=int(year)
    # date,month,year=1,'May',1999
    # print(type(date),type(month),type(year))
    previousDay(date,month,year)







