'''
Find the Town Judge
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Constraints:
    1 <= n <= 1000
    0 <= trust.length <= 104
    trust[i].length == 2
    All the pairs of trust are unique.
    ai != bi
    1 <= ai, bi <= n
'''
class Solution:
    def findJudge(self,n,trust):
        #Town Judge -> trusting nobody, everybody else would be trusting
        #[1,2] Person1 trusts Person2
        #1-n People, Trust Array-> elements which tell us who trusts whom
        #[1,2] 1 is trusting 2, Town Judge - 2
        #[1,2,3] and they 1->3,2->3
        #1->3,2->3,3->1 Return -1
        # In[] and Out[] [1->3]
        #[0,0,1] and [1,0,0]
        #[2->3]
        #[0,0,2] and [1,1,0]
        #In[] array contains the trusted counter
        #Out[] array contains trusting somebody else counter
        #TownJudge will be whose In[] array would be trusted by N-1 people and
        #Out[] array would be 0.
        In=[0]*n
        Out=[0]*n
        #Example , if n==3 and length of trust array is also 3 then there will be cycle so will simply return -1. Tesetcase 3 is the example for it
        #So thats why we have used below if statement
        if len(trust)<n-1:
            return -1
        for i in range(len(trust)):
            x=trust[i]
            trusting_somebody,trusted=x[0],x[1]
            In[trusted-1]+=1
            Out[trusting_somebody-1]+=1
        print(In,Out)
        for i in range(len(Out)):
            if Out[i]==0 and In[i]==n-1:
                return i+1
        else:
            return -1
if __name__ == '__main__':
    n=4
    trust=[[1,3],[1,4],[2,3],[2,4],[4,3]] #O/p - 3
    # n=3
    # trust=[[1,3],[2,3],[3,1]]
    # n=3
    # trust=[[1,3],[2,3]]
    ob=Solution()
    print(ob.findJudge(n,trust))
