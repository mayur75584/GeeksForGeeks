'''

A physical education teacher asks students to assemble in a straight line for the morning assembly.
In spite of repeated instructions, the students do not obey the teacher.
Given an array of N number of arguments in which each element represents the height of the student in that position.
 The task here is to find the number of students, only for students numbered 1 to N -1(a[1] to a[N-1]),
 whose height is less than the height of their adjacent students.

Example 1:
Input:
N-5
a-(35,15,45,25,55)
Elements a[0] to a[n-1], where each input element is separated
by a new line.

Output:
2- Number of elements whose adjacent elements are greater

Explanation:
From the input array given above
a[0]=35
a[1]=15
a[2]=45
a[3]=25
a[4]=55

The elements whose adjacent values are greater are 15 and 25 as
a[0]>a[1]15<45a[2]>a[3]25<55a[4]

Hence the output is 2.

'''
def func(n,a):
    count1=0
    for i in range(1,n):
        if a[i]<a[i-1] and a[i]<a[i+1]:
            count1+=1
            print(a[i])
    print(count1)

if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))

    func(n,a)

