'''
Common Subsequence OldP

Given two strings S1 and S2 print whether they contain any common subsequence (non empty) or not.
NOTE: Print 1 if they have a common subsequence (non empty) else 0.

Example 1:

Input: S1 = "ABEF" , S2 = "CADE"
Output: 1
Explanation: "A", "E", "AE" are in
both S1 and S2.

Example 2:

Input: S1 = "ABCDE" , S2 = "FGHIJ"
Output: 0
Explanation: There is no common
subsequences .


Your Task:
You dont need to read input or print anything. Complete the function commonSubseq() which takes S1 and S2 as input parameter and returns 1 if they have a common subsequence (non empty) else 0.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(K), Where K = Constant.

Constraints:
1<= |S1|=|S2| <=1000
'''
class Solution:
    def commonSubseq(self,S1,S2):
        count = 0
        for i in S1:
            if i in S2:
                count += 1
        if count >= 1:
            return 1
        else:
            return 0

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        S1,S2=input().split()

        ob=Solution()
        print(ob.commonSubseq(S1,S2))
