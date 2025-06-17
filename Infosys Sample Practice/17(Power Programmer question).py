'''
You are given an array A containing N elements. You do the following
step repeatedly;

1. Take any 2 elements and add their absolute difference back to the array

Calculate the number of distinct possible values the array contains after infinite number of
steps modulo 10^9+7.

Sample Input: 2 2 6
Sample Output: 3
Explanation: You can add 6-2=4 in one step, no more unique numbers can be
added. Total numbers = 3.

Sample Input: 5 1 2 3 4 5
Sample Output: 5
Explanation: Since array already contains all absolute differences of any two elements,
no more number can be added.

Sample Input: 2 1 100
Sample Output: 100
Explanation: Since array contains 1, you can add any number 1<=j<=100 to the array

Sample Input: 6 9 6 12 15 24 27
Sample Output: 9
Explanation: We can add abs(6-9)=3 to the array in one step. Then we can add 24-3=21 in another step.
We can also add 21-3 or 27-9=18 to the array.Adding 3,21,18 to the original array makes the number of elements equal to 9. One can
verify that we can't add any other elements.
'''


'''
Logic is GCD(Greatest common divisior)
A=[2,6]
Here greatest common divisior in array is 2
So max(A) i.e 6 // gcd i.e 2 = 3

A=[6,9,6,12,15,24,27]
Here in array gcd is 3 and maximum elemnt is 27
27//3 = 9

A=[1,100]
Here in array gcd is 1 and maximum element is 100
100/1 = 1
'''

import math

# n=6
# A=[6,9,6,12,15,24,27]
n=2
A=[1,100]
# n=5
# A=[1,2,3,4,5]
# n=2
# A=[2,6]
result=A[0]

for i in range(1,len(A)):
    b=math.gcd(result,A[i])
    print(b)
    result=b
print(result)
print("Original Answer is:")
print(max(A)//result)