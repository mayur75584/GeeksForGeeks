'''
Transform String

Given two strings A and B. Find the minimum number of steps required to transform string A into string B.
The only allowed operation for the transformation is selecting a character from string A
and inserting it in the beginning of string A.

Example 1:
Input:
A = "abd"
B = "bad"
Output: 1
Explanation: The conversion can take place in
1 operation: Pick 'b' and place it at the front.

Example 2:
Input:
A = "GeeksForGeeks"
B = "ForGeeksGeeks"
Output: 3
Explanation: The conversion can take
place in 3 operations:
Pick 'r' and place it at the front.
A = "rGeeksFoGeeks"
Pick 'o' and place it at the front.
A = "orGeeksFGeeks"
Pick 'F' and place it at the front.
A = "ForGeeksGeeks"

Your Task:
You dont need to read input or print anything.
Complete the function transform() which takes two strings A and B as
input parameters and returns the minimum number of steps required to transform A into B.
If transformation is not possible return -1.

Expected Time Complexity: O(N) where N is max(length of A, length of B)
Expected Auxiliary Space: O(1)

Constraints:
1<= A.length(), B.length() <= 104
'''
class Solution:
    def transform(self,A,B):
        dict1 = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                 "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
        dict2 = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                 "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
        a = A.lower()
        b = B.lower()
        for i in a:
            dict1[i] += 1
        for j in b:
            dict2[j] += 1
        if dict1 != dict2:
            return -1
        count1 = 0
        if len(A) == len(B):
            i = len(A) - 1
            j = len(B) - 1
            while (i != -1):
                if A[i] == B[j]:
                    i -= 1
                    j -= 1
                elif (A[i] != B[j]):
                    count1 += 1
                    i -= 1
            return count1


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # A,B=map(str,input().split())
        # A="GeeksForGeeks"
        # B="ForGeeksGeeks"
        # A="abd"
        # B="bad"
        A="abcd"
        B="efgh"
        ob=Solution()
        print(ob.transform(A,B))