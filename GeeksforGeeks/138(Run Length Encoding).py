'''
Run Length Encoding

Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string.
eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.
You are required to complete the function encode that takes only one argument the string which is to be encoded and returns the encoded string.

Example 1:

Input:
str = aaaabbbccc
Output: a4b3c3
Explanation: a repeated 4 times
consecutively b 3 times, c also 3
times.

Example 2:

Input:
str = abbbcdddd
Output: a1b3c1d4

Your Task:
Complete the function encode() which takes a character array as a input parameter and returns the encoded string.

Expected Time Complexity: O(N), N = length of given string.
Expected Auxiliary Space: O(1)

Constraints:
1<=length of str<=100
'''

def encode(arr):
    s1=''
    i=0
    count=1
    while(i!=len(arr)-1):
        if arr[i]==arr[i+1]:
            count+=1
            i+=1
        elif arr[i]!=arr[i+1]:
            s1+=arr[i]
            s1+=str(count)
            count=1
            i+=1
    s1+=arr[i]
    s1+=str(count)
    # print(s1)
    return s1




if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # arr=input()
        # arr='aaaabbbccc'
        arr='abbbcdddd'
        print(encode(arr))
