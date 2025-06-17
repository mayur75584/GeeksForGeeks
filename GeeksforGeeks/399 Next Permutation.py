'''
Next Permutation
Difficulty: MediumAccuracy: 40.66%Submissions: 148K+Points: 4
Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order).

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

Examples:

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.
Input: arr = [3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
Input: arr = [3, 4, 2, 5, 1]
Output: [3, 4, 5, 1, 2]
Explanation: The next permutation of the given array is {3, 4, 5, 1, 2}.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
'''


'''
Algorithm / Intuition
The steps are the following:

Find the break-point, i: Break-point means the first index i from the back of the given array where arr[i] becomes smaller than arr[i+1].
For example, if the given array is {2,1,5,4,3,0,0}, the break-point will be index 1(0-based indexing).
Here from the back of the array, index 1 is the first index where arr[1] i.e. 1 is smaller than arr[i+1] i.e. 5.
To find the break-point, using a loop we will traverse the array backward and store the index i where arr[i] is less than the value at index (i+1) i.e. arr[i+1].

If such a break-point does not exist i.e. if the array is sorted in decreasing order, the given permutation is the last one in the sorted order of all possible permutations.
So, the next permutation must be the first i.e. the permutation in increasing order.
So, in this case, we will reverse the whole array and will return it as our answer.

If a break-point exists:
Find the smallest number i.e. > arr[i] and in the right half of index i(i.e. from index i+1 to n-1) and swap it with arr[i].
Reverse the entire right half(i.e. from index i+1 to n-1) of index i. And finally, return the array.

'''

class Solution:
    def nextPermutation(self,arr):
        x=sorted(arr)
        if arr==x[::-1]:
            arr.clear()
            arr.extend(x)
        else:
            ind=-1
            for i in range(len(arr)-2,-1,-1):
                if arr[i]<arr[i+1]:
                    ind=i
                    break

            if ind==-1:
                arr.reverse()
                return

            for i in range(len(arr)-1,ind,-1):
                if arr[i]>arr[ind]:
                    arr[i],arr[ind]=arr[ind],arr[i]
                    break
            print(arr)

            arr[ind+1:]=reversed(arr[ind+1:])
            return arr

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # arr=list(map(int,input().split()))
        # arr=[2,4,1,7,5,0]
        # arr=[3,2,1]
        arr=[3,4,2,5,1]
        # arr=[1,2,3,6,5,4]
        ob=Solution()
        ob.nextPermutation(arr)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
