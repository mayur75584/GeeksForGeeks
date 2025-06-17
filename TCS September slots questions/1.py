'Jack Sunday'

'''
Jack is always excited about sunday. It is favourite day, when he gets to play all day. And goes to cycling with his friends.

So every time when the months starts he counts the number of sundays he will get to enjoy. Considering the month can start with any day, be it Sunday, Monday…. Or so on.

Count the number of Sunday jack will get within n number of days.

Example 1:

Input

mon-> input String denoting the start of the month.

13  -> input integer denoting the number of days from the start of the month.

Output :

2    -> number of days within 13 days.

Explanation:

The month start with mon(Monday). So the upcoming sunday will arrive in next 6 days. And then next Sunday in next 7 days and so on.

Now total number of days are 13. It means 6 days to first sunday and then remaining 7 days will end up in another sunday. Total 2 sundays may fall within 13 days.
'''

s=input()
n=int(input())

count=0

if s=='mon':
    # if n>=6:
    n-=6
    count+=1
elif s=='tue':
    # if n>=5:
    n-=5
    count+=1
elif s=='wed':
    # if n>=4:
    n-=4
    count+=1
elif s=='thu':
    # if n<=3:
    n-=3
    count+=1
elif s=='fri':
    # if n<=2:
    n-=2
    count+=1
elif s=='sat':
    # if n<=1:
    n-=1
    count+=1


while n!=0:
    if n>=7:
        count+=1
        n-=7
    else:
        break
print(count)

'Onlinsestudy4u solution'

# d=input()
# n=int(input())
# days=['mon','tue','wed','thu','fri','sat','sun']
# index=days.index(d)
# i=index+1
# count=0
# while(n>0):
#     if (i==len(days)):
#         i=0
#     if(days[i]=='sun'):
#         count+=1
#     i+=1
#     n-=1
# print(count)





