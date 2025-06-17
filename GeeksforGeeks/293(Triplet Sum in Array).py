'''
Triplet Sum in Array

Given an array arr of size n and an integer X.
Find if there's a triplet in the array which sums up to the given integer X.

Example 1:
Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:
1
Explanation:
The triplet {1, 4, 8} in
the array sums up to 13.

Example 2:
Input:
n = 5, X = 10
arr[] = [1 2 4 3 6]
Output:
1
Explanation:
The triplet {1, 3, 6} in
the array sums up to 10.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function find3Numbers() which takes the array arr[],
the size of the array (n) and the sum (X) as inputs
and returns True if there exists a triplet in the array arr[]
which sums up to X and False otherwise.

Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 103
1 ≤ A[i] ≤ 105
'''
'Method 1'
'''
This is a Hashing-based solution. 

Approach: This approach uses extra space but is simpler than the two-pointers approach. 
Run two loops outer loop from start to end and inner loop from i+1 to end. 
Create a hashmap or set to store the elements in between i+1 to j-1. 
So if the given sum is x, check if there is a number in the set 
which is equal to x – arr[i] – arr[j]. If yes print the triplet. 
 
Algorithm: 
Traverse the array from start to end. (loop counter i)
Create a HashMap or set to store unique pairs.
Run another loop from i+1 to end of the array. (loop counter j)
If there is an element in the set which is equal to x- arr[i] – arr[j], 
then print the triplet (arr[i], arr[j], x-arr[i]-arr[j]) and break
Insert the jth element in the set.
'''
# class Solution:
#     def find3Numbers(self,A,n,X):
#
#         for i in range(n):
#             s=set()
#             curr_sum=X-A[i]
#             for j in range(i+1,n):
#                 if(curr_sum-A[j] in s):
#                     x=[A[i],A[j],curr_sum-A[j]]
#                     print(x)
#                     return True
#                 s.add(A[j])
#         return False
#
# if __name__ == '__main__':
#     # t=int(input())
#     t=1
#     for i in range(t):
#         # n,X=map(int,input().split())
#         # A=list(map(int,input().split()))
#         # n,X=6,13
#         # A=[1,4,45,6,10,8]
#         n,X=5,10
#         A=[1,2,4,3,6]
#         ob=Solution()
#         if(ob.find3Numbers(A,n,X)):
#             print(1)
#         else:
#             print(0)

'Method 2'
'''
 This method uses sorting to increase the efficiency of the code. 

Approach: By Sorting the array the efficiency of the algorithm can be improved. 
This efficient approach uses the two-pointer technique. 
Traverse the array and fix the first element of the triplet. 
Now use the Two Pointers algorithm to find if there is a pair 
whose sum is equal to x – array[i]. 
Two pointers algorithm take linear time so it is better than a nested loop.
Algorithm : 
Sort the given array.
Loop over the array and fix the first element of the possible triplet, arr[i].
Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum, 
If the sum is smaller than the required sum, increment the first pointer.
Else, If the sum is bigger, Decrease the end pointer to reduce the sum.
Else, if the sum of elements at two-pointer is equal to given sum then print the triplet and break.
'''
class Solution:
    def find3Numbers(self,A,n,X):
        A.sort()
        for i in range(n):
            l=i+1
            r=n-1
            while(l<r):
                if(A[i]+A[l]+A[r]==X):
                    x=[A[i],A[l],A[r]]
                    print(x)
                    return True
                elif(A[i]+A[l]+A[r]<X):
                    l+=1
                else:
                    r-=1
        return False

if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n,X=map(int,input().split())
        # A=list(map(int,input().split()))
        # n,X=6,13
        # A=[1,4,45,6,10,8]
        n,X=5,10
        A=[1,2,4,3,6]
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)