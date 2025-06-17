'''



Example1:

Input: 4 nums=[1,2,3,1]
Output:4
Explanation:Rob house 1(money=1) and then rob house 3(mpney=3). total amount you can rob = 1+3=4.

Example2:

Input: 5 nums=[2,7,9,3,1]
Output:12
Explanation:Rob house 1(money=2), rob house 3(money=9) and rob house 5(money=1).Total amount
you can rob=2+9+1=12.
'''



def func(n,nums):
    if len(nums)==1:
        return nums[0]
    elif len(nums)==2:
        if nums[0]>nums[1]:
            return nums[0]
        else:
            return nums[1]
    else:
        pass



if __name__ == '__main__':
    n=int(input())
    nums=list(map(int,input().split()))
    result=func(n,nums)
    print(result)
