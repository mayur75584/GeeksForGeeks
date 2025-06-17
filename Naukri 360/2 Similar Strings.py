'''
Similar Strings
Ninja
200/200
Average time to solve is 70m
Contributed by
Asked in companies
Problem statement
You are given three strings, 'A', 'B', and 'C', each of length 'N' consisting of lower case alphabets. The difference between the three strings is defined as ∑|A[i] − B[i]| + |A[i] − C[i]| where |A[i] − B[i]| and |A[i] − C[i]| are the absolute differences between ASCII values of the characters at the position i in strings 'A', 'B' and 'A' ,'C' respectively. You are allowed to rotate the string 'A' cyclically. There are a total of 'N' possible rotations of a string of length 'N'.

Your task is to return the maximum and minimum difference of the three strings for all the possible rotations of string a.

For Example:
If the value of 'N' is 2, 'A' is "ab" , 'B' is "aa" and 'C' is "bb".
Then the answer for this input is
min = 2
max = 2

Because current difference is 1 + 1 = 2
After one rotation difference will be 1 + 1 = 2
Hence, the minimum and the maximum answer is 2.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 50
1 <= N <= 10^4

Time Limit: 1 sec.
Sample Input 1:
2
3
abc
aaa
bba
2
ab
bb
ab
Sample Output 1:
6 4
3 1
Explanation For Sample Input 1:
For the first test case, there will be 3 possible rotations for the
string 'A'. in the first rotation, it will make the difference of 6 in
the second rotation, the difference will be 4 and in the third
rotation, the difference will be 6.

Hence max answer is 6, and the min is 4 here.

Similarly, in the second test case, the max answer will be 3 and
the min will be 1.
Sample Input 2:
2
2
ab
bb
ac
2
ab
bb
ac
Sample Output 2:
4 2
3 3
'''

def similarStrings(n,a,b,c):
    max1=0
    min1=9999999999999999999999999999999999

    lst=[]
    for i in range(n):
        a1=a[0]
        a+=a1
        a=a[1:]
        # print(a)
        lst1=[]
        for j in range(n):
            lst1.extend(list(zip(a[j],b[j],c[j])))
        lst.append(lst1)
    print(lst)

    for i in lst:
        sum1=0
        lst2=[]
        for j in i:
            sum1+=(abs(ord(j[0])-ord(j[1]))+abs(ord(j[0])-ord(j[2])))
        lst2.append(sum1)
        print(lst2)
        if max(lst2)>max1:
            max1=max(lst2)
        if min(lst2)<min1:
            min1=min(lst2)
        # print(sum1)
    # print(max1,min1)
    return [max1,min1]
if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # a=input()
        # b=input()
        # c=input()
        # n=3
        # a="abc"
        # b="aaa"
        # c="bba"
        n=2
        a="ab"
        b="bb"
        c="ab"
        ans=similarStrings(n,a,b,c)
        print(ans)