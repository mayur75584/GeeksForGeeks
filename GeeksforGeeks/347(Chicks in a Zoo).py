'''
Chicks in a Zoo

Initially, the zoo have a single chick.
A chick gives birth to 2 chicks every day and the life expectancy of a chick is 6 days.
Zoo officials want to buy food for chicks so they want to know the number of chicks on an Nth day.
Help the officials with this task.

Example 1:

Input: N = 2
Output: 3
Explanation: First day there is only 1 chick.
On second day total number of chicks = 3.

Example 2:

Input: N = 3
Output: 9
Explanation: First day there is only 1 chick.
On second day total number of chicks = 3.
On third day total number of chicks = 9



Your Task:
You don't need to read or print anything,
Your task is to complete the function NoOfChicks() which takes N as the input parameter
and returns the total no. of chicks on the Nth day.


Expected Time Complexity: O(N)
Expected Space Complexity: O(N)


Constraints:
1 <= N <= 35

'''

class Solution:
    def NoOfChicks(self,N):
        if(N<1):
            return 0
        sum1=1
        arr=[0,1]
        if N==1:
            return 1
        id=1
        for i in range(2,N+1):
            if(i<=6):
                x=sum1*2
                arr.append(x)
                sum1+=x
            else:
                sum1-=arr[id]
                x=sum1*2
                arr.append(x)
                sum1+=x
                id+=1
        return sum1


if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # N=int(input())
        # N=8
        N=12
        obj=Solution()
        ans=obj.NoOfChicks(N)
        print(ans)