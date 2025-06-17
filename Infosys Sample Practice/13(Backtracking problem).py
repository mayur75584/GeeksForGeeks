'''
Given an array of distinct integers candidates and a target,
return a list of all unique combinations of candidates where
the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited
number of times. Two combinations are unique if the frequency
of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up
to target is less than 150 combinations for the given input.

Input:
candidates = [2,3,6,7]
target = 7
Output:
[[2,2,3],[7]]

Explanation:

2 and 3 are candidates, and 2+2+3=7. Note that 2 can be used multiple
times.
7 is a candidate, and 7=7.
There are only two combinations.

Input:
candidates = [2,3,5]
target = 8
Output:
[[2,2,2,2],[2,3,3],[3,5]]
'''

def combinationSum(candidates,target):
    result=[]

    def backtrack(remain,comb,start):
        if remain==0:
            result.append(list(comb))
            return
        if remain<0:
            return
        for i in range(start,len(candidates)):
            comb.append(candidates[i])
            backtrack(remain-candidates[i],comb,i)
            comb.pop()
    backtrack(target,[],0)

    return result


if __name__ == '__main__':
    # candidates=list(map(int,input().split()))
    # target=int(input())
    candidates=[2,3,6,7]
    target=7
    # candidates=[2,3,5]
    # target=8
    result=combinationSum(candidates,target)
    for i in result:
        print(i,end=' ')