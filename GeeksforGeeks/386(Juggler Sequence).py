
'''
Juggler Sequence

Juggler Sequence is a series of integers in which the first term starts with a positive integer number a and the remaining terms are generated from the immediate previous term using the below recurrence relation:

         a_k**(1/2)  for even a_k
a_k+1 =
         a_k**(3/2) for odd a_k

Juggler Formula

Given a number n, find the Juggler Sequence for this number as the first term of the sequence until it becomes 1.


Example 1:

Input: n = 9
Output: 9 27 140 11 36 6 2 1
Explaination: We start with 9 and use
above formula to get next terms.


Example 2:

Input: n = 6
Output: 6 2 1
Explaination:
[61/2] = 2.
[21/2] = 1.


Your Task:
You do not need to read input or print anything.
Your Task is to complete the function jugglerSequence() which takes n as the input parameter and returns a list of integers denoting the generated sequence.



Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)



Constraints:
1 ≤ n ≤ 100


'''

class Solution:
    def jugglerSequence(self,n):
        lst=[n]
        while(n!=1):
            z=n
            if(n%2==0):
                z=int(z**0.5)
                # print(z)
                lst.append(z)
            else:
                z=int(z**1.5)
                # print(z)
                lst.append(z)
            n=z
        return lst



if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        n=9
        # n=6

        ob=Solution()
        arr=ob.jugglerSequence(n)
        for i in arr:
            print(i,end=" ")
        print()