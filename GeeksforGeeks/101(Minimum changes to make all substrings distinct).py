'''

Minimum changes to make all substrings distinct
Easy Accuracy: 73.18% Submissions: 97 Points: 2

Given a string s consisting only lower case alphabets, find the minimum number of changes required to it so that all substrings of the string become distinct.
Note: length of the string is at most 26.

Example 1:

Input: S = "aab"
Output: 1
Explanation: If we change one instance
of 'a' to any character from 'c' to 'z',
we get all distinct substrings.

â€‹Example 2:

Input: S = "ab"
Output: 0
Explanation: As no change is required
hence 0.

Your Task:
You don't need to read input or print anything. Your task is to complete the function minChange() which takes the string S as inputs and returns the answer.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(26)

Constraints:
1 ≤ |S| ≤ 26
'''


class Solution:
    def minChange(self,S):
        s=list(set(S))
        return len(S)-len(s)

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        s=input()
        ob=Solution()
        print(ob.minChange(S))