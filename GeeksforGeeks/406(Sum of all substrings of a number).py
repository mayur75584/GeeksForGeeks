'''
Sum of all substrings of a number
Difficulty: MediumAccuracy: 38.11%Submissions: 60K+Points: 4
Given an integer s represented as a string, the task is to get the sum of all possible sub-strings of this string.

Note: The number may have leading zeros.
It is guaranteed that the total sum will fit within a 32-bit signed integer.

Examples:

Input: s = "6759"
Output: 8421
Explanation:
Sum = 6 + 7 + 5 + 9 + 67 + 75 + 59 + 675 + 759 + 6759 = 8421
Input: s = "421"
Output: 491
Explanation:
Sum = 4 + 2 + 1 + 42 + 21 + 421 = 491
Constraints:
1 <= |s| <= 9

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
Topic Tags
Strings Dynamic Programming Data Structures Algorithms
'''
class Solution:
    def sumSubstrings(self,s):
        if len(s)==1:
            return int(s)
        ans=0
        for i in s:
            ans+=int(i)
        # ans+=int(s)s

        i,j=0,1
        while(j<len(s)):
            s1=s[i:j+1]
            ans+=int(s1)
            k=j+1
            while(k<len(s)):
                s2=s[i:k+1]
                ans+=int(s2)
                k+=1
            i+=1
            j+=1
        return ans



if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # s=input()
        # s="6759"
        # s="421"
        s="122"
        obj=Solution()
        ans=obj.sumSubstrings(s)
        print(ans)
        t-=1