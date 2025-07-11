'''
Match specific pattern

Given a dictionary of words and a pattern. Every character in the pattern is uniquely mapped to a character in the dictionary. Find all such words in the dictionary that match the given pattern.

Example 1:

Input:
N = 4
dict[] = {abb,abc,xyz,xyy}
pattern  = foo
Output: abb xyy
Explanation: xyy and abb have the same
character at index 1 and 2 like the
pattern.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findMatchedWords() which takes an array of strings dict[] consisting of the words in the dictionary and a string, Pattern and returns an array of strings consisting of all the words in the dict[] that match the given Pattern in lexicographical order.

Expected Time Complexity: O(N*K) (where K is the length of the pattern).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 10
'''


def findSpecificPattern(Dict,pattern):

    s1=''
    for i in pattern:
        s1+=str(pattern.count(i))
    z=[]
    for i in arr:
        x=''
        for j in i:
            x+=str(i.count(j))
        z.append(x)
    # print(s1)
    # print(type(z[0]))
    z1=[]
    for i in range(len(Dict)):
        if z[i]==s1:
            z1.append(Dict[i])
    return z1





if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr=list(map(int,input().split()))
        # string=input()
        n=4
        arr=['abb','abc','xyz','xyy']
        string='foo'
        res=findSpecificPattern(arr,string)
        for i in res:
            print(i,end=' ')
        print()