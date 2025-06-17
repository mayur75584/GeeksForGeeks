
'''
CamelCase Pattern Matching

Given a dictionary of words where each word follows CamelCase notation, print all words (in lexicographical order) in the dictionary that match with a given pattern consisting of uppercase characters only.

Example: GeeksForGeeks matches the pattern "GFG", because if we combine all the capital letters in GeeksForGeeks they become GFG.

CamelCase is the practice of writing compound words or phrases such that each word or abbreviation begins with a capital letter. Common examples include PowerPoint and Wikipedia, GeeksForGeeks, CodeBlocks, etc.

Example 1:

Input:
N=3
Dictionary=["WelcomeGeek",
"WelcomeToGeeksForGeeks","GeeksForGeeks"]
Pattern="WTG"
Output:
WelcomeToGeeksForGeeks
Explanation:
Since only WelcomeToGeeksForGeeks matches
the pattern, it is the only answer.

Example 2:

Input:
N=8
Dictionary=["Hi","Hello","HelloWorld",
"HiTech","HiGeek","HiTechWorld",
"HiTechCity","HiTechLab"]
Pattern="HA"
Output:
-1
Explanation:
Since the pattern matches none of the words
of the string,the output is -1.

Your Task:
You don't need to read input or print anything. Your Task is to complete the function CamelCase() which takes an integer N, a Vector of strings Dictionary and a string Pattern and returns the strings in the dictionary that match the pattern, if not found any return -1.

Expected Time Complexity: O(N*|S|) S=Longest string in Dictionary
Expected Auxillary Space: O(26*N)

Constraints:
1<=N<=1000
1<=|S|<=100
1<=|Pattern|<=|S|<=100
S is the longest word in Dictionary.
View Bookmarked Problems
Company Tags
Ola Cabs
Topic Tags
StringsTrieData StructuresAdvanced Data Structure
'''

class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        s=[]
        k=0
        x=-1
        for i in Dictionary:
            x+=1
            z=[]
            for j in i:
                if j.isupper():
                    z.append(j)
                    k=len(z)-1
                if len(z)>0 and ''.join(z)==Pattern:
                    break
                if j.isupper() and j==Pattern[k]:
                    k=len(z)-1
                    continue
                elif len(z)>0 and z[k]!=Pattern[k]:
                    break
                elif k==len(Pattern):
                    s.append(i)
                    k=0
                    break
            s1=''.join(z)
            if  s1==Pattern or s1[:len(Pattern)]==Pattern:
                k=0
                s.append(i)
            else:
                k=0

        if len(s)>0:
            return s
        else:
            return [-1]


if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # Dictionary=list(map(int,input().split()))
        # Pattern=input()
        N=3
        Dictionary=["WelcomeGeek","WelcomeToGeeksForGeeks","GeeksForGeeks"]
        Pattern="WTG"
        # N=8
        # Dictionary=["Hi","Hello","HelloWorld","HiTech","HiGeek","HiTechWorld","HiTechCity","HiTechLab"]
        # Pattern="HA"
        # N=3
        # Dictionary=["WelcomeGeek","WelcomeToGeeksForGeeks","GeeksForGeeks"]
        # Pattern="GFG"
        # N=3
        # Dictionary=["WelcomeGeek" ,"WelcomeToGeeksForGeeks" ,"GeeksForGeeks"]
        # Pattern="GG"
        # N=8
        # Dictionary=["XbZLTl", "jhKtsPiqgz", "QbLaJHw", "tzKlcInXHT", "hxlnzzzwau", "svEnAxiKVB", "UfEtVRZQL", "pOzrL"]
        # Pattern="KI"
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()
