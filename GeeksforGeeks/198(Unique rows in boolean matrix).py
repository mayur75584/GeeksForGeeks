'''
Unique rows in boolean matrix

Given a binary matrix your task is to find all unique rows of the given matrix.

Example 1:

Input:
row = 3, col = 4
M[][] = {{1 1 0 1},{1 0 0 1},{1 1 0 1}}
Output: 1 1 0 1 $1 0 0 1 $
Explanation: Above the matrix of size 3x4
looks like
1 1 0 1
1 0 0 1
1 1 0 1
The two unique rows are 1 1 0 1 and
1 0 0 1 .

Your Task:
You only need to implement the given function uniqueRow().
The function takes three arguments the first argument is a matrix M and the next two arguments are row
and col denoting the rows and columns of the matrix. The function should return the list of the unique
 row of the martrix. Do not read input, instead use the arguments given in the function.

Note: The drivers code print the rows "$" separated.

Expected Time Complexity: O(row * col)
Expected Auxiliary Space: O(row * col)

Constraints:
1<=row,col<=40
0<=M[][]<=1
'''

import re
def uniqueRow(row,col,matrix):
    z=re.findall(r'\d+',str(matrix)) #here in matrix give str(matrix) otherwise
    #will get error
    lst=list(map(int,z))
    print(lst)
    i=0
    j=col
    ans=[]
    while(j<=len(lst)):
        x=lst[i:j]
        if x not in ans:
            ans.append(x)
        j+=col
        i+=col
    return ans
if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t):
        # row,col=map(int,input().split())
        # matrix=input().split()
        row,col=3,4
        matrix='1 1 0 1 1 0 0 1 1 1 0 1'
        a=uniqueRow(row,col,matrix)

        for row in a:
            for value in row:
                print(value,end=' ')
            print("$",end='')
        print()
        t-=1