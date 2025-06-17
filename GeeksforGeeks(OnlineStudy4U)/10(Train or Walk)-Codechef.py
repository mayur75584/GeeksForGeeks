'''
Train or Walk

Chefland has all the cities on a straight line. There are N cities in Chefland numbered 1 to N. City i is located at coordinate xi on the x-axis. Guru wants to travel from city A to city B

. He starts at time t=0. He has following choices to travel.

    He can walk 1

metre in P
secs.
There is a train that travels from city C
to city D which travels 1 metre in Q secs which starts at time t=Y secs. Guru can take the train only at city C and leave the train only at city D

    .

Can you help Guru find the minimum time he will need to travel from city A
to B. Note that you cannot board the train after time t =Y

.
Input:

    First line will contain T

, number of testcases. Then the testcases follow.
First line of each testcase contains eight space separated integers N,A,B,C,D,P,Q,Y
.
Second line of each testcase contains N
space-separated integers with the i-th integer representing xi

    .

Output:

For each testcase, output in a single line containing the minimum travel time.
Constraints

    1≤T≤300

2≤N≤300
−1000≤xi≤1000
0≤Y≤100000
1≤A,B,C,D≤n
A≠B
C≠D
1≤P,Q≤100
xi<xj
if i<j

Sample Input:

1

4 1 3 2 4 3 2 4

1 2 3 4
Sample Output:

6
EXPLANATION:

Guru can walk directly in 6 secs.

If Guru takes train, then he will need atleast 11 secs.
'''



'Note-> Not able to understand the problem'