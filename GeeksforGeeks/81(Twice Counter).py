'''
Twice Counter

Given a list of N words. Count the number of words that appear exactly twice in the list.

Example 1:

Input:
N = 3
list = {Geeks, For, Geeks}
Output: 1
Explanation: 'Geeks' is the only word that
appears twice.

Example 2:

Input:
N = 8
list = {Tom, Jerry, Thomas, Tom, Jerry,
Courage, Tom, Courage}
Output: 2
Explanation: 'Jerry' and 'Courage' are the
only words that appears twice.


Your Task:
You dont need to read input or print anything. Complete the function countWords() which takes integer N and list of strings as input parameters and returns the number of words that appear twice in the list.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1<= N <= 104
'''

class Solution:
    def countWords(self,List,n):
        z=set(List)
        count=0
        for i in z:
            if List.count(i)==2:
                count+=1
        return count


if __name__ == '__main__':
    # T=int(input())
    T=1
    for tcs in range(T):
        # n=int(input())
        # List=input().split()
        n=8
        List=["Tom","Jerry","Thomas","Tom","Jerry","Courage","Tom","Courage"]
        ob=Solution()
        print(ob.countWords(List,n))