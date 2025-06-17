'''
Jumping on the Clouds

There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus or

. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered
if they are safe or

if they must be avoided.

Example
Index the array from . The number on each cloud is its index in the list so the player must avoid the clouds at indices and . They could follow these two paths: or . The first path takes jumps while the second takes . Return

.

Function Description

Complete the jumpingOnClouds function in the editor below.

jumpingOnClouds has the following parameter(s):

    int c[n]: an array of binary integers

Returns

    int: the minimum number of jumps required

Input Format

The first line contains an integer
, the total number of clouds. The second line contains space-separated binary integers describing clouds where

.

Constraints

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0

7
0 0 1 0 0 1 0

Sample Output 0

4

Explanation 0:
The player must avoid
and . The game can be won with a minimum of

jumps:

[jump(2).png]

Sample Input 1

6
0 0 0 0 1 0

Sample Output 1

3

Explanation 1:
The only thundercloud to avoid is
. The game can be won in

jumps:

[jump(5).png]
'''
'Note-> Complete this'
def jumpingOnClouds(c):
    # count=1
    # for i in range(1,len(c)):
    #     if c[i]!=1:
    #         # if i!=len(c):
    #         if c[i+1]==0 and c[i+2]==0:
    #             count+=1
    #             c.pop(c[i+2])
    #             c.pop(c[i+1])
    #         elif c[i+1]==0 and c[i+2]==1:
    #             count+=1
    #             c.pop(c[i+1])
    #         elif c[i+1]==1 and c[i+2]==0:
    #             count+=1
    #             c.pop(c[i+2])
    #         # elif i==len(c):
    #         #     if c[i]==0:
    #         #         count+=1
    #     elif c[i]==1:
    #         i+=1
    # print(count)




    # n=len(c)
    # jumps=0
    # for i in range(0,n-1):
    #     if c[i]==1:
    #         continue
    #     if (i<n-2 and c[i+2]==0):
    #         i+=1
    #     jumps+=1
    # return jumps


    # count=0
    # n=len(c)
    # # for i in range(0,n-2):
    # i=0
    # while(i<n-2):
    #     if c[i]==1:
    #         continue
    #     if i<n-2 and (c[i+1]==0 and c[i+2]==0):
    #         # i+=2
    #         i+=1
    #         count+=1
    #     elif i<n-2 and (c[i+1]==0):
    #         i+=1
    #         count+=1
    #     elif i<n-2 and c[i+2]==0:
    #         # i+=2
    #         i+=1
    #         count+=1
    # return count

    count=0
    i=0
    n=len(c)-1
    while(i<=n-1):
        if i<=n-1 and c[i+1]==0 and c[i+2]==0:
            count+=1
            i+=2
        # elif i<=n-1 and c[]



if __name__ == '__main__':
    # n=int(input())
    # c=list(map(int,input().strip().split()))
    # n=6
    # c=[0,0,0,1,0,0]
    n=7
    c=[0,0,1,0,0,1,0]
    # jumpingOnClouds(c)
    result = jumpingOnClouds(c)
    print(result)

