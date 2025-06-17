'Note-> Not able to solve'
'''
Max sum in the configuration


Given an array(0-based indexing), you have to find the max sum of i*A[i] where A[i] is the element at index i in the array. The only operation allowed is to rotate(clock-wise or counter clock-wise) the array any number of times.

Example 1:

Input:
N = 4
A[] = {8,3,1,2}
Output: 29
Explanation: Above the configuration
possible by rotating elements are
3 1 2 8 here sum is 3*0+1*1+2*2+8*3 = 29
1 2 8 3 here sum is 1*0+2*1+8*2+3*3 = 27
2 8 3 1 here sum is 2*0+8*1+3*2+1*3 = 17
8 3 1 2 here sum is 8*0+3*1+1*2+2*3 = 11
Here the max sum is 29

Your Task:
Your task is to complete the function max_sum which takes two arguments which is the array A [ ] and its size and returns an integer value denoting the required max sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1<=N<=104
1<=A[]<1000
'''
class Solution:
    def max_sum(self,arr,n):

        max=0
        for i in range(n):
            sum1=0
            for j in range(len(arr)):
                sum1+=arr[j]*arr.index(arr[j])
            z=arr[0]
            arr.remove(z)
            arr.append(z)
            if sum1>max:
                max=sum1
        return max



if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # n=int(input())
        # arr=list(map(int,input().strip().split()))
        # n=4
        # arr=[8,3,1,2]
        n=84
        arr=[887 ,778 ,916 ,794 ,336 ,387 ,493 ,650 ,422 ,363 ,28 ,691 ,60 ,764 ,927 ,541 ,427 ,173 ,737 ,212 ,369 ,568 ,430 ,783 ,531 ,863 ,124 ,68 ,136 ,930 ,803 ,23 ,59 ,70 ,168 ,394 ,457 ,12 ,43 ,230 ,374 ,422 ,920 ,785 ,538 ,199 ,325 ,316 ,371 ,414 ,527 ,92 ,981 ,957 ,874 ,863 ,171 ,997 ,282 ,306 ,926 ,85 ,328 ,337 ,506 ,847 ,730 ,314 ,858 ,125 ,896 ,583 ,546 ,815 ,368 ,435 ,365 ,44 ,751 ,88 ,809 ,277 ,179 ,789]
        ob=Solution()
        print(ob.max_sum(arr,n))