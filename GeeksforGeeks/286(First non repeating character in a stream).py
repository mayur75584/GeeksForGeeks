'''
First non-repeating character in a stream

Given an input stream of A of n characters consisting only of lower case alphabets.
The task is to find the first non repeating character,
each time a character is inserted to the stream.
If there is no such character then append '#' to the answer.

Example 1:
Input: A = "aabc"
Output: "a#bb"
Explanation: For every character first non
repeating character is as follow-
"a" - first non-repeating character is 'a'
"aa" - no non-repeating character so '#'
"aab" - first non-repeating character is 'b'
"aabc" - first non-repeating character is 'b'

Example 2:
Input: A = "zz"
Output: "z#"
Explanation: For every character first non
repeating character is as follow-
"z" - first non-repeating character is 'z'
"zz" - no non-repeating character so '#'

Your Task:
You don't need to read or print anything.
Your task is to complete the function FirstNonRepeating()
which takes A as input parameter and returns a string after processing the input stream.

Expected Time Complexity: O(26 * n)
Expected Space Complexity: O(26)

Constraints:
1 <= n <= 105
'''
class Solution:
    def FirstNonRepeating(self,A):
        x = []
        y = []
        ans = ''
        for i in A:
            if i not in x:
                x.append(i)
                y.append(1)
                if 1 not in y:
                    ans += '#'
                else:
                    ind = y.index(1)
                    ans += x[ind]
            else:
                z = x.index(i)
                y[z] += 1
                if 1 not in y:
                    ans += "#"
                else:
                    ind = y.index(1)
                    ans += x[ind]
        return ans

if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # A=input()
        # A="aabc"
        # A="zz"
        A="hrqcvsvszpsjammdrw"
        ob=Solution()
        ans=ob.FirstNonRepeating(A)
        print(ans)
