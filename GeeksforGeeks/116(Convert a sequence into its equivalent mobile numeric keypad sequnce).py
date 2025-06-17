'''
Convert a sentence into its equivalent mobile numeric keypad sequence

Link for diagram ->  https://practice.geeksforgeeks.org/problems/convert-a-sentence-into-its-equivalent-mobile-numeric-keypad-sequence0547/1/?problemStatus=unsolved&difficulty[]=0&page=2&sortBy=newest&query=problemStatusunsolveddifficulty[]0page2sortBynewest#

Given a sentence in the form of a string in uppercase, convert it into its equivalent mobile numeric keypad sequence.



Example 1:

Input:
S = "GFG"
Output: 43334
Explanation: For 'G' press '4' one time.
For 'F' press '3' three times.

Example 2:

Input:
S = "HEY U"
Output: 4433999088
Explanation: For 'H' press '4' two times.
â€‹For 'E' press '3' two times. For 'Y' press '9'
three times. For white space press '0' one time.
For 'U' press '8' two times.



Your Task:
You dont need to read input or print anything. Complete the function printSequence() which takes a string as input parameter and returns its equivalent mobile numeric keypad sequence as a string.


Expected Time Complexity: O(Length of String)
Expected Auxiliary Space: O(Length of String)


Constraints:

1 <= Length of String <= 105
Characters of string can be empty space or capital alphabets.
'''


class Solution:
    def printSequence(self,S):
        _2='ABC'
        _3='DEF'
        _4='GHI'
        _5='JKL'
        _6='MNO'
        _7='PQRS'
        _8='TUV'
        _9='WXYZ'
        s1=''
        for i in S:
            if i in _2:
                x=_2.index(i)+1
                s1+='2'*x
            elif i in _3:
                x=_3.index(i)+1
                s1+='3'*x
            elif i in _4:
                x=_4.index(i)+1
                s1+='4'*x
            elif i in _5:
                x=_5.index(i)+1
                s1+='5'*x
            elif i in _6:
                x=_6.index(i)+1
                s1+='6'*x
            elif i in _7:
                x=_7.index(i)+1
                s1+='7'*x
            elif i in _8:
                x=_8.index(i)+1
                s1+='8'*x
            elif i in _9:
                x=_9.index(i)+1
                s1+='9'*x
            elif i==' ':
                s1+='0'
        return s1



if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # inputStr=input()
        # inputStr='GFG'
        inputStr='HEY U'
        solObj=Solution()
        print(solObj.printSequence(inputStr))
