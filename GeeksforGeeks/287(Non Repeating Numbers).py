'''
Non Repeating Numbers

Given an array A containing 2*N+2 positive numbers,
out of which 2*N numbers exist in pairs whereas the other two number occur
exactly once and are distinct. Find the other two numbers.

Example 1:
Input:
N = 2
arr[] = {1, 2, 3, 2, 1, 4}
Output:
3 4
Explanation:
3 and 4 occur exactly once.

Example 2:
Input:
N = 1
arr[] = {2, 1, 3, 2}
Output:
1 3
Explanation:
1 3 occur exactly once.

Your Task:
You do not need to read or print anything.
Your task is to complete the function singleNumber() which takes
the array as input parameter and returns a list of two numbers
which occur exactly once in the array. The list must be in ascending order.

Expected Time Complexity: O(N)
Expected Space Complexity: O(1)

Constraints:
1 <= length of array <= 106
1 <= Elements in array <= 5 * 106
'''
class Solution:
    def singleNumber(self,nums):
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=-1
            else:
                dict1[i]-=1
        print(dict1)
        res=[]
        for i,j in dict1.items():
            if j==-1:
                res.append(i)
        return sorted(res)

if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # n=int(input())
        # v=list(map(int,input().split()))
        # n=2
        # v=[1,2,3,2,1,4]
        # n=1
        # v=[2,1,3,2]
        n=4
        v=[18,24,24,21,10,29,8,10,29,18]
        ob=Solution()
        ans=ob.singleNumber(v)
        for i in ans:
            print(i,end=" ")
        print()