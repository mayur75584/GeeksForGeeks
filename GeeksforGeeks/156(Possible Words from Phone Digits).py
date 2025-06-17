'''
Possible Words From Phone Digits

Given a keypad as shown in the diagram, and an N digit number which is represented by array a[ ],
the task is to list all words which are possible by pressing these numbers.

Below is the link to see the diagram
https://practice.geeksforgeeks.org/problems/possible-words-from-phone-digits-1587115620/1#

1-'' 2-ABC 3-DEF 4-GHI 5-JKL 6-MNO 7-PQRS 8-TUV 9-WXYZ * 0 #
Example 1:
Input: N = 3, a[] = {2, 3, 4}
Output:
adg adh adi aeg aeh aei afg afh afi
bdg bdh bdi beg beh bei bfg bfh bfi
cdg cdh cdi ceg ceh cei cfg cfh cfi
Explanation: When we press 2,3,4 then
adg, adh, adi, ... cfi are the list of
possible words.

Example 2:
Input: N = 3, a[] = {3, 4, 5}
Output:
dgj dgk dgl dhj dhk dhl dij dik dil
egj egk egl ehj ehk ehl eij eik eil
fgj fgk fgl fhj fhk fhl fij fik fil
Explanation: When we press 3,4,5 then
dgj, dgk, dgl, ... fil are the list of
possible words.

Your Task:
You don't need to read input or print anything.
You just need to complete the function possibleWords() that takes an array a[ ] and N as input parameters
and returns an array of all the possible words in lexicographical increasing order.

Expected Time Complexity: O(4N * N).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 10
2 ≤ a[i] ≤ 9
'''
import itertools
class Solution:
    def possibleWords(self,a,N):
        dict={1:'',2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz',0:''}
        z=[]
        for i in a:
            z.append(dict[i])
        print(z)
        b=["".join(s) for s in itertools.product(*z)]
        print(len(b))
        return b
if __name__ == '__main__':
    # T=int(input())
    T=1
    while(T>0):
        # N=int(input())
        # a=[]
        # for i in range(N):
        #     a.append(int(input()))
        # N=3
        # a=[2,3,4]
        N=3
        a=[3,4,5]
        ob=Solution()
        res=ob.possibleWords(a,N)
        for i in range(len(res)):
            print(res[i],end=' ')
        print()

        T-=1