'''
Implement Atoi

Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.

Note: You are not allowed to use inbuilt function.

Example 1:

Input:
str = 123
Output: 123

Example 2:

Input:
str = 21a
Output: -1
Explanation: Output is -1 as all
characters are not digit only.

Your Task:
Complete the function atoi() which takes a string as input parameter and returns integer value of it. if the input string is not a numerical string then returns 1..

Expected Time Complexity: O(|S|), |S| = length of string str.
Expected Auxiliary Space: O(1)

Constraints:
1<=length of S<=10


Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.
'''
class Solution:
    def atoi(self,string):
        value={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'-1':-1,'-2':-2,'-3':-3,'-4':-4,'-5':-5,'-6':-6,'-7':-7,'-8':-8,'-9':-9}
        result=0
        s1='0123456789'
        # lst=[]
        flag=False
        for i in string:

            if i in s1:
                result = 10*result+value[i]
            elif i=='-':
                flag=True

            else:
                return -1
        # print(type(result))
        if flag==True:
            # print(type(result))
            return -1 * result
        else:
            return result


if __name__ == '__main__':
    # t=int(input())
    t=1
    for i in range(t):
        # string = input().strip()
        string='123'
        # string='21a'
        # string='-12'
        ob = Solution()
        print(ob.atoi(string))