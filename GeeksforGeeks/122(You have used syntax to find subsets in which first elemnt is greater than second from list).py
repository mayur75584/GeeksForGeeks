'Code is correct but getting memory error'
'''
Mr. Modulo and Arrays 
Mr. Modulo lives up to his name and is always busy taking modulo of numbers and making new problems.
Now he comes up with another problem. He has an array of integers with n elements and wants to find a pair of elements 
{arr[i], arr[j]} such that arr[i] ≥ arr[j] and arr[i] % arr[j] is maximum among all possible pairs where 1 ≤ i, j ≤ n.
Mr. Modulo needs some help to solve this problem. Help him to find this maximum value arr[i] % arr[j]. 


Example 1:

Input:
n=3
arr[] = {3, 4, 7} 
Output: 3
Explanation: There are 3 pairs which satisfies 
             arr[i] >= arr[j] are:-
             4, 3 => 4 % 3 = 1
             7, 3 => 7 % 3 = 1
             7, 4 => 7 % 4 = 3
             Hence maximum value among all is 3.

Example 2:

Input:
n=4
arr[] = {4, 4, 4, 4} 
Output: 0

Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function maxModValue() that takes array arr and n as parameters and return the required answer.

 

Expected Time Complexity: O(nLog(n) + Mlog(M)) n is total number of elements and M is maximum value of all the elements.
Expected Auxiliary Space: O(1).

 

Constraints:
1 ≤ n ≤ 105

1 ≤ arr[i] ≤ 105
'''
import itertools

def maxModValue(arr,n):
    if len(list(set(arr)))==1:
        return 0
    else:
        result=[(x,y) for x,y in itertools.product(arr,arr) if x>y] #syntax to find subset in which first element is
        #greater than second
        print(result)
        max1=0
        for i in result:
            x=list(i)
            if (x[0]%x[1])>max1:
                max1=x[0]%x[1]
        return max1
        # result=[]
        #
        # for x in arr:
        #     for y in arr:
        #         if x>y:
        #             z=[]
        #             z.append(x)
        #             z.append(y)
        #             result.append(z)
        # # print(result)
        # max1=0
        # for i in result:
        #     x=list(i)
        #     if (x[0]%x[1])>max1:
        #         max1=x[0]%x[1]
        # return max1





if __name__ == '__main__':
    # t=int(input())
    t=1
    for _ in range(t):
        # n=int(input())
        # a=list(map(int,input().split()))
        n=3
        a=[3,4,7]
        # n=4
        # a=[4,4,4,4]
        print(maxModValue(a,n))