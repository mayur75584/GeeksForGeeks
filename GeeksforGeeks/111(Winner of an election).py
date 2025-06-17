'''
Winner of an election

Given an array of names (consisting of lowercase characters) of candidates in an election. A candidate name in array represents a vote casted to the candidate. Print the name of candidate that received Max votes. If there is tie, print lexicographically smaller name.

Example 1:

Input:
n = 13
Votes[] = {john,johnny,jackie,johnny,john
jackie,jamie,jamie,john,johnny,jamie,
johnny,john}
Output: john 4
Explanation: john has 4 votes casted for
him, but so does johny. john is
lexicographically smaller, so we print
john and the votes he received.

Example 2:

Input:
n = 3
Votes[] = {andy,blake,clark}
Output: andy 1
Explanation: All the candidates get 1
votes each. We print andy as it is
lexicographically smaller.

Your Task:
You only need to complete the function winner() that takes an array of strings arr, and n as parameters and returns the name of the candiate with maximum votes and the number of votes the candidate got as an array of size 2.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= n <= 105
'''

class Solution:
    def winner(self,arr,n):
        z = list(sorted(set(arr)))
        lst = []
        result=[]
        for i in z:
            x = arr.count(i)
            lst.append(x)
        z1 = max(lst)
        if lst.count(z1) >= 2:
            x1 = lst.index(z1)
            result.append(z[x1])
            result.append(z1)
        else:
            x1 = lst.index(z1)
            result.append(z[x1])
            result.append(z1)
        return result


if __name__ == '__main__':
    # T=int(input())
    T=1
    for _ in range(T):
        # n=int(input())
        # arr=input().split()
        n=13
        arr=['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john']
        result=Solution().winner(arr,n)
        print(result[0],result[1])