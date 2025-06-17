'''
Count distinct elements in every window

Given an array of integers and a number K.
Find the count of distinct elements in every window of size K in the array.

Example 1:

Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: Window 1 of size k = 4 is
1 2 1 3. Number of distinct elements in
this window are 3.
Window 2 of size k = 4 is 2 1 3 4. Number
of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number
of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number
of distinct elements in this window are 3.

Example 2:

Input:
N = 3, K = 2
A[] = {4,1,1}
Output: 2 1

Your Task:
Your task is to complete the function countDistinct() which takes the array A[],
the size of the array(N) and the window size(K) as inputs
and returns an array containing
the count of distinct elements in every contiguous window of size K in the array A[].

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= K <= N <= 105
1 <= A[i] <= 105 , for each valid i
'''
'''
DefaultDict
Defaultdict is a container like dictionaries present in the module collections.
Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object.
The functionality of both dictionaries and defaultdict are almost same except for
the fact that defaultdict never raises a KeyError.
It provides a default value for the key that does not exists.

Syntax: defaultdict(default_factory)
Parameters:

default_factory: A function returning the default value for the dictionary defined.
If this argument is absent then the dictionary raises a KeyError.
'''
'''
Algorithm:
1-Create an empty hash map. Let the hash map be hM.
2-Initialize the count of distinct elements as dist_count to 0.
3-Traverse through the first window and insert elements of the first window to hM.
The elements are used as key and their counts as the value in hM.
Also, keep updating dist_count
4-Print distinct count for the first window.
5-Traverse through the remaining array (or other windows).
6-Remove the first element of the previous window.
6.1-If the removed element appeared only once, remove it from hM and decrease the distinct count,
i.e. do “dist_count–“
6.2-else (appeared multiple times in hM), then decrement its count in hM
7-Add the current element (last element of the new window)
7.1-If the added element is not present in hM, add it to hM and increase the distinct count, i.e. do “dist_count++”
7.2-Else (the added element appeared multiple times), increment its count in hM
'''
from collections import defaultdict
class Solution:
    def countDistinct(self,A,N,K):
        if N<K:
            return [-1]
        # Creates an empty hashmap hm
        mp=defaultdict(lambda :0)
        # print(mp)
        res=[]
        dis_count=0

        # Traverse the first window and store count
        # of every element in hash map
        for i in range(K):
            if mp[A[i]]==0:
                dis_count+=1
            mp[A[i]]+=1
        # print(dis_count)

        #just to see what happen in hasmap i.e mp
        for i in mp.items():
            print(i,end=' ')
        print()

        for i in range(K,N):
            res.append(dis_count)
            # Remove first element of previous window
            # If there was only one occurrence,
            # then reduce distinct count.
            if(mp[A[i-K]]==1):
                dis_count-=1
            mp[A[i-K]]-=1

            # Add new element of current window
            # If this element appears first time,
            # increment distinct element count
            if(mp[A[i]]==0):
                dis_count+=1
            mp[A[i]]+=1
        res.append(dis_count)
        return res


if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n,k=map(int,input().split())
        # arr=list(map(int,input().split()))
        # n,k=7,4
        # arr=[1,2,1,3,4,2,3]
        n,k=3,2
        arr=[4,1,1]
        res=Solution().countDistinct(arr,n,k)
        for i in res:
            print(i,end=' ')
        print()