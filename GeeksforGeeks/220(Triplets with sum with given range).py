'''
Triplets with sum with given range

Given an array Arr[] of N distinct integers and a range from L to R,
the task is to count the number of triplets having a sum in the range [L, R].


Example 1:
Input:
N = 4
Arr = {8 , 3, 5, 2}
L = 7, R = 11
Output: 1
Explaination: There is only one triplet {2, 3, 5}
having sum 10 in range [7, 11].


Example 2:
Input:
N = 5
Arr = {5, 1, 4, 3, 2}
L = 2, R = 7
Output: 2
Explaination: There two triplets having
sum in range [2, 7] are {1,4,2} and {1,3,2}.


Your Task:
You don't need to read input or print anything. Your task is to complete
the function countTriplets() which takes the array Arr[] and its size N and L and R
as input parameters and returns the count.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 103
1 ≤ Arr[i] ≤ 103
1 ≤ L ≤ R ≤ 109
'''


class Solution:
    def countTriplets(self,Arr,N,L,R):
        Arr.sort()
        c1=self.helper(Arr,N,L-1)
        c2=self.helper(Arr,N,R)

        return c2-c1
    def helper(self,a,n,x):
        res=0
        for i in range(0,n-1):
            j=i+1
            k=n-1
            while(j<k):
                sum=a[i]+a[j]+a[k]
                if(sum>x):
                    k-=1
                else:
                    res+=(k-j)
                    j+=1
        return res

if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # N=int(input())
        # Arr=list(map(int,input().split()))
        # L,R=map(int,input().split())
        # N=4
        # Arr=[8,3,5,2]
        # L,R=7,11
        N=5
        Arr=[5,1,4,3,2]
        L,R=2,7
        ob=Solution()
        print(ob.countTriplets(Arr,N,L,R))
