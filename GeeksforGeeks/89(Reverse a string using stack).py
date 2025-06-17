'''
Reverse a string using Stack

You are given a string S, the task is to reverse the string using stack.



Example 1:


Input: S="GeeksforGeeks"
Output: skeeGrofskeeG



Your Task:
You don't need to read input or print anything. Your task is to complete the function reverse() which takes the string S as an input parameter and returns the reversed string.



Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)



Constraints:
1 ≤ length of the string ≤ 100
'''
def reverse(S):
    stack=[]
    z=''
    for i in range(len(S)-1,-1,-1):
        stack.append(S[i])
        z+=stack.pop()
    return z



if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # str1=input()
        str1='GeeksforGeeks'
        print(reverse(str1))