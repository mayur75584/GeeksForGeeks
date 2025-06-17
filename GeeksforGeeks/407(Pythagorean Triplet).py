'''
Pythagorean Triplet

Given an array arr[], return true if there is a triplet (a, b, c) from the array (where a, b, and c are on different indexes) that satisfies a2 + b2 = c2, otherwise return false.

Examples:

Input: arr[] = [3, 2, 4, 6, 5]
Output: true
Explanation: a=3, b=4, and c=5 forms a pythagorean triplet.
Input: arr[] = [3, 8, 5]
Output: false
Explanation: No such triplet possible.
Input: arr[] = [1, 1, 1]
Output: false
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 103

Expected Complexities
Time Complexity: O(n + max(arr[i])^2)
Auxiliary Space: O(max(arr[i]))
Company Tags
AmazonAdobe
Topic Tags
Arrays Data Structures

'''
class Solution:
    def pythagoreanTripelt(self,arr):
        if len(arr)<3:
            return False
        dict1={}
        for i in arr:
            dict1[i]=i*i
        # print(dict1)
        val,key=[],[]
        dict1=sorted(dict1.items(),key=lambda x:x[1])
        # print(dict1)
        for i in dict1:
            key.append(i[0])
            val.append(i[1])

        i=0
        while(i<len(val)):
            j=i+1
            while(j<len(val)):
                sum0=val[i]+val[j]
                # print(sum0,val[i],val[j])
                if sum0 in val[j+1:]:
                    return True
                j+=1
            i+=1
        return False


if __name__ == '__main__':
    # t=int(input())
    t=1
    while(t>0):
        # arr=list(map(int,input().split()))
        # arr=[3,2,4,6,5]
        # arr=[3,8,5]
        # arr=[1,1,1]
        # arr=[18,20,7,13,20,13,13,21,9,24,15,15,80,22,82,14,9,22,21,27]
        # arr=[13,9,16,3,15,8,1,28,3,12,29,3,28,19,11,25,11,26,19,3]
        obj=Solution()
        print(obj.pythagoreanTripelt(arr))
        t-=1