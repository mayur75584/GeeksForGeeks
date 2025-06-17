'''
Earthquake and the Paint Shop

Geek's Paint Shop is one of the famous shop in Geekland,
but 2014 Earthquake caused disarrangement of the items in his shop.
Each item in his shop is a 40-digit alpha numeric code .
Now Chunky wants to retain the reputation of his shop,
for that he has to arrange all the distinct items in lexicographical order.
Your task is to arrange the all the distinct items in lexicographical ascending order
and print them along with their count.

Example 1:

Input:
N = 3
A[] =
["2234597891 zmxvvxbcij 8800654113 jihgfedcba",
"1234567891 abcdefghij 9876543219 jihgfedcba",
"2234597891 zmxvvxbcij 8800654113 jihgfedcba"]
Output:
1234567891 abcdefghij 9876543219 jihgfedcba 1
2234597891 zmxvvxbcij 8800654113 jihgfedcba 2
Explanation:
We have 3 items (40 digit alphanumeric codes)
here. We arrange the items based on the
lexicographical order of their alpha-numeric
code. Distinct items are printed only once.
The count of the items describes how many
such items are there, so items that appear
more than once have their count greater than 1.

Example 2:

Input:
N = 2
A[] =
["3122049353 onafrnbhtr 9822827304 yzfhdgzcvx",
"2992299540 lpvkgykmlk 6946169466 vdqwvywwgg",
Output:
2992299540 lpvkgykmlk 6946169466 vdqwvywwgg  1
3122049353 onafrnbhtr 9822827304 yzfhdgzcvx  1
Explanation:
Out of the 2 items here no one is repeated.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function sortedStrings()
which takes an integer N and an array of strings A[ ]
and returns the array in sorted order along with the frequency of each distinct string.

Expected Time Complexity:O(NlogN)
Expected Auxillary Space:O(N)

Constraints:
1 ≤ N ≤ 10000

'''
import math

class alphanumeric:
    def __init__(self,name,count):
        self.name=name
        self.count=count
class Solution:
    def sortedStrings(self,N,A):
        dict1={}
        for i in A:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        dict1_sort=sorted(dict1.items(),key=lambda x:x[0])
        print(dict1_sort)
        dict1_keys=[]
        for i in dict1_sort:
            dict1_keys+=[i[0]]
        print(dict1_keys)
        ans=[]
        for i in dict1_keys:
            ans.append(alphanumeric(i,dict1[i]))
        return ans

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # a=[]
        # for i in range(N):
        #     x=input()
        #     a.append(x)
        # N=3
        # a=["2234597891 zmxvvxbcij 8800654113 jihgfedcba","1234567891 abcdefghij 9876543219 jihgfedcba","2234597891 zmxvvxbcij 8800654113 jihgfedcba"]
        # N=2
        # a=["3122049353 onafrnbhtr 9822827304 yzfhdgzcvx", "2992299540 lpvkgykmlk 6946169466 vdqwvywwgg",]
        N=5
        a=["2234597891 zmxvvxbcij 8800654113 jihgfedcba","1234567891 zxyabcvapo 0123434908 padmadngaa","1234567891 abcdefghij 9876543219 jihgfedcba","2234597891 zmxvvxbcij 8800654113 jihgfedcba","9120121291 zmxvvxbcij 0912114113 mnvxbedcba"]
        ob=Solution()
        ans=ob.sortedStrings(N,a)
        for i in ans:
            print(i.name,end=' ')
            print(i.count)
