'Tough Question'
'''
Important Table:- On basis of this table Logic was made

SUM   5Rs   2Rs    1Rs

1     0     0       1

2     0     0       2

3     0     1       1

4     0     1       2

5     0     2       1

6     0     2       2

7     0     3       1

8     0     3       2

9     1     1       2     - Here for 2Rs and 1Rs used 4Rs values

10    1     2       1     - Here for 2Rs and 1Rs used 5Rs values

11    1     2       2     - Here for 2Rs and 1Rs used 6Rs values


.....
.....
.....
This will keep on continuing
'''

number=int(input())

five = int((number-4)/5)

if((number-5*five)%2)==0:
    one=2
else:
    one=1

two=(number-5*five-one)//2

print(one+two+five,five,two,one)
