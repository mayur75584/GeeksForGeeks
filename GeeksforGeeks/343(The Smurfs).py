'''
The Smurfs

A geek once visited a magical island where he found a special creature.
He named it as Smurf.
He noticed a very strange thing there.
The smurfs resembled the primary colors of light.
To make it more clear, the primary colors of light are Red(R), Green(G), and Blue(B).
He talked to one of the smurfs. The smurfs came to know that he is a good programmer.
The smurfs suggested a deal that they will ask him one question and if he is able to answer that question,
they will allow the geek to take anything from the island.
The question is as follows:
The smurfs possess a very magical property. When two smurfs of different colors meet with other,
they gets converted into a smurf of the third color. How many minimum number of smurfs
will be remaining after this transformation? The question looked simple to geek.
However, the smurfs put another constraint to make the geek think more. The two smurfs must be adjacent to each other
to make the transformation take place. There are n smurfs the colors of which are given in an array a[].

Example 1:

Input: n = 5
a = {'R' , 'G', 'B', 'R', 'B'}
Output: 1
Explaination: First 'R' and 'G' makes 'B'.
Then 'B' and 'R' makes 'G' and that 'G'
with 'B' at index 2 makes 'R', Now the 'R'
and the last 'B' makes 'G'.

Example 2:

Input: n = 2
a = {'R', 'R'}
Output: 2
Explaination: There are two 'R' s. So
they cannot change to anything else.

Your Task:
You do not need to read input or print anything.
Your task is to complete the function findMin() which takes n and a
as input parameters and retunrs the minimum number of smurfs existing at the end.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 1000

'''
'''
Logic Pattern
{'R','G','B','R',B','G'}

B G R
B B  => count=2

if count of any colour is even then answer is 2

If odd
{'R','G','B'}

B B=> 2

if occurrence is odd then answer is 2

if we have

G G G=> 3
R R=> 2
B=> 1
if any of the count is equal to n then answer is n


Last Remaining possibility is 1.
'''
class Solution:
    def minFind(self,n,a):
        redCount=0
        greenCount=0
        blueCount=0

        for i in a:
            if i=='R':
                redCount+=1
            elif(i=='G'):
                greenCount+=1
            else:
                blueCount+=1
        if(greenCount==n or blueCount==n or redCount==n):
            return n
        if((greenCount%2==0 and redCount%2==0 and blueCount%2==0) or
                (greenCount%2==1 and redCount%2==1 and blueCount%2==1)):
            return 2
        return 1


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # a=list(map(str,input().split()))
        # n=5
        # a=['R','G','B','R','B']
        # n=2
        # a=['R','R']
        n=18
        a=['G','R','B','G','R','R','G','G','G','G','B','B','B','B','G','B','B','G']
        ob=Solution()
        print(ob.minFind(n,a))