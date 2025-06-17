'''
Minimum Gifts
A Company has decided to give some gifts to all of its employees. For that, the company has given some rank to each employee. Based on that rank, the company has made certain rules to distribute the gifts.
The rules for distributing the gifts are:
Each employee must receive at least one gift.
Employees having higher ranking get a greater number of gifts than their neighbours.
What is the minimum number of gifts required by the company?
Constraints
1 < T < 10
1 < N < 100000
1 < Rank < 10^9
Input
First line contains integer T, denoting the number of test cases.
For each test case:
First line contains integer N, denoting the number of employees.
Second line contains N space separated integers, denoting the rank of each employee.

Output

For each test case print the number of minimum gifts required on a new line.

Example 1

Input

2

5

1 2 1 5 2

2

1 2

Output

7

3


Explanation

For test case 1, adhering to the rules mentioned above,

Employee # 1 whose rank is 1 gets one gift

Employee # 2 whose rank is 2 gets two gifts

Employee # 3 whose rank is 1 gets one gift

Employee # 4 whose rank is 5 gets two gifts

Employee # 5 whose rank is 2 gets one gift

Therefore, total gifts required is 1 + 2 + 1 + 2 + 1 = 7

Similarly, for testcase 2, adhering to rules mentioned above,

Employee # 1 whose rank is 1 gets one gift

Employee # 2 whose rank is 2 gets two gifts

Therefore, total gifts required is 1 + 2 = 3
'''

def func(n,a):
    left_neighbour=[1]
    right_neighbour=[0]*n
    right_neighbour[-1]=1
    # print(right_neighbour)

    for i in range(1,n):
        if a[i]>a[i-1]:
            left_neighbour.append(left_neighbour[-1]+1)
        else:
            left_neighbour.append(1)
    for i in range(n-2,-1,-1):
        if a[i]>a[i+1]:
            right_neighbour[i]=right_neighbour[i+1]+1
        else:
            right_neighbour[i]=1
    print(left_neighbour)
    print(right_neighbour)

    count1=0
    for i in range(len(left_neighbour)):
        #taking maximum from left_neighbour and right_neighbour because in left and right neigbour array we have taken minimum so now here
        #we will take maximum
        count1+=max(left_neighbour[i],right_neighbour[i])
    return count1

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # a=list(map(int,input().split()))

        # n=5
        # a=[1,2,1,5,2]

        # n=6
        # a=[1,2,3,2,5,7]

        # n=2
        # a=[1,2]

        n=8
        a=[5,7,10,3,1,5,13,9]
        res=func(n,a)
        print(res)


