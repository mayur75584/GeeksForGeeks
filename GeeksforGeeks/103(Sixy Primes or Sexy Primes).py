'''
Sixy Primes

Sixy primes are prime numbers that differ from each other by six. For example, the numbers 5 and 11 are both sixy primes, because they differ by 6. Given a range of the form [L, R]. The task is to find all the sixy prime pairs in the range in increasing order.

Example 1:

Input: L = 11, R = 19
Output: [11, 17, 13, 19]
Explanation: There are total two pair possible
with difference 6 and these are 11,17,13,19.


Example 2:

Input: L = 6, R = 20
Output: [7, 13, 11, 17, 13, 19]
Explanation: There are total three pair possible
with difference 6 and these are 7,13,11,17,13,19.


Your Task:
You dont need to read input or print anything. Complete the function sixyPrime() which takes L and R as input parameter and returns all the sixy prime exist and if there are no sixy prime exist returns -1.

Expected Time Complexity: O(nloglogn)
Expected Auxiliary Space: O(n)

Constraints:
1 <= L <= R <=103
'''

class Solution:
    def sixyPrime(self,L,R):
        lst = []
        for i in range(L, R + 1):
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    break
            else:
                lst.append(i)

        lst1 = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if abs(lst[i] - lst[j]) == 6:
                    lst1.append(lst[i])
                    lst1.append(lst[j])
        # print(*lst1)
        # print(len(lst1))
        z1=[-1]
        if len(lst1) == 0:
            return z1

        else:
            return lst1

if __name__ == '__main__':
    # T=int(input())
    T=1
    for i in range(T):
        # L,R=input().split()
        # L=int(L)
        # R=int(R)
        # L,R=11,19
        L,R=1,5
        # L,R=14,36
        ob=Solution()
        ans=ob.sixyPrime(L,R)
        for i in range(len(ans)):
            print(ans[i],end=' ')
        print()