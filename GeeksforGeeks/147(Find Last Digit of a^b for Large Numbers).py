'In this question i had focused more on time complexity so thats why used this logic'
'''
Find Last Digit Of a^b for Large Numbers 

You are given two integer numbers, the base a and the index b. You have to find the last digit of ab.

 

Example 1:

Input:
a = "3", b = "10"
Output:
9
Explanation:
310 = 59049. Last digit is 9.

Example 2:

Input:
a = "6", b = "2"
Output:
6
Explanation:
62 = 36. Last digit is 6.

 

Your Task:
You don't need to read input or print anything. Your task is to complete the function getLastDigit() which takes two strings a,b as parameters and returns an integer denoting the last digit of ab.

 

Expected Time Complexity: O(|b|)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= |a|,|b| <= 1000

Note:|a| = length of a and |b| = length of b. There will not be any test cases such that ab is undefined.
'''

class Solution:
    def getLastDigit(self,a,b):
        if b=='0':
            return 1
        z = str(int(b) % 4)
        if a[-1] == '1':
            return 1
        elif a[-1] == '2':
            if z == '2':
                return 4
            elif z == '3':
                return 8
            elif z == '0':
                return '6'
            elif z == '1':
                return '2'
        elif a[-1] == '3':
            if z == '2':
                return 9
            elif z == '3':
                return 7
            elif z == '0':
                return 1
            elif z == '1':
                return '3'
        elif a[-1] == '4':
            x = str(int(b) % 2)
            if x == '0':
                return 6
            elif x == '1':
                return 4
        elif a[-1] == '5':
            return 5
        elif a[-1] == '6':
            return 6
        elif a[-1] == '7':
            if z == '1':
                return 7
            elif z == '2':
                return 9
            elif z == '3':
                return 3
            elif z == '0':
                return 1
        elif a[-1] == '8':
            if z == '2':
                return 4
            elif z == '3':
                return 2
            elif z == '0':
                return 6
            elif z == '1':
                return 8
        elif a[-1] == '9':
            x = str(int(b) % 2)
            if x == '0':
                return 1
            elif x == '1':
                return 9
        elif a[-1] == '0':
            return 0




if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        a,b=map(str,input().split())

        ob=Solution()
        print(ob.getLastDigit(a,b))
