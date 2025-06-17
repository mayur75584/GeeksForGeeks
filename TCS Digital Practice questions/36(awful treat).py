'''
Problem Statement:- A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.

For example, there are 4 prisoners and 6 pieces of candy. The prisoners arrange themselves in seats numbered 1 to 4 . Let’s suppose two are drawn from the hat. Prisoners receive candy at positions 2,3,4,1,2,3. The prisoner to be warned sits in chair number 3

Function Description

Write a function saveThePrisoner. It should return an integer representing the chair number of the prisoner to warn.

saveThePrisoner has the following parameter(s):

    n: an integer, the number of prisoners
    m: an integer, the number of sweets
    s: an integer, the chair number to begin passing out sweets from

Input Format

    The first line contains an integer t, denoting the number of test cases.
    The next t lines each contain 3 space-separated integers:
        – : n the number of prisoners
        – : m the number of sweets
        – : s the chair number to start passing out treats at

Output Format

    For each test case, print the chair number of the prisoner who receives the awful treat on a new line.

Sample Input

     2
     5 2 1
     5 2 2

Sample Output

    2
    3
'''



if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n,m,s=map(int,input().split())
        # n,m,s=5,2,1
        # n,m,s=5,2,2
        # n,m,s=5,3,3
        # n,m,s=100,52,80
        n,m,s=11111,202,650
        j=s
        z=[0]*(n+1)
        x=[]
        while(m!=0):
            if j==(n+1):
                j=1
            z[j]+=1
            x.append(j)
            j+=1
            m-=1
        print(x[-1])
'''
Prepinsta Solution

def saveThePrisoner(n, m, s):
    if (m + s - 1) % n == 0:
        return n
    else:
        return (m+s-1) % n
# t = int(input())
t=1
for t_itr in range(t):
    nms = input().split()
    n = int(nms[0])
    m = int(nms[1])
    s = int(nms[2])

    result = saveThePrisoner(n, m, s)
    print(result)
'''