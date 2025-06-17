'''
Solution-> https://www.geeksforgeeks.org/find-the-size-of-largest-subset-with-positive-bitwise-and/
'''
'''
Find the size of Largest Subset with positive Bitwise AND

Given an array arr[] consisting of N positive integers,
the task is to find the largest size of the subset of the array arr[] with positive Bitwise AND.

Examples:

Input: arr[] = [7, 13, 8, 2, 3]
Output: 3
Explanation:
The subset having Bitwise AND positive is {13, 7, 3} is of length 3,
which is of maximum length among all possible subsets.

Input: arr[] = [1, 2, 4, 8]
Output: 1
'''
'''
Approach: The given problem can be solved by counting the number of set bits at 
each corresponding bits position for all array elements and then the count of 
the maximum of set bits at any position is the maximum count of subset required because 
the Bitwise AND of all those elements is always positive. Follow the steps below to solve the given problem:

Initialize an array, say bit[] of size 32 that stores the count of set bits at each ith bit position.
Traverse the given array and for each element, say arr[i] increment the frequency of the ith bit in the array bit[] 
if the ith bit is set in arr[i].
After the above steps, print the maximum of the array bit[] to print the maximum size of the subset.
'''
def solution(A):
    # Stores the number of set bits
    # at each bit position
    z=[0 for _ in range(32)]
    for i in range(len(A)):
        # Current bit position
        m=31
        # Loop till array element
        # becomes zero
        while(A[i]>0):
            # If the last bit is set
            if(A[i]&1==1):
                # Increment frequency
                z[m]+=1
            # Divide array element by 2
            A[i]=A[i]>>1
            # Decrease the bit position
            m-=1
    ans=max(z)
    # Size of the largest possible subset
    return ans


if __name__ == '__main__':
    # A=list(map(int,input().split()))
    # A=[13,7,2,8,3]
    # A=[1,2,4,8]
    A=[16,16]
    print(solution(A))