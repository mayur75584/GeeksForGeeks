'''
Lata is an English teacher in primary school.She asks her students to find out the number of words and
characters to find out the number of words and character in a given sentence.

Your job is to write a program doing a count of words and characters in the given sentence.

Constraints
T=200

Example1:
Input
Lata is an English teacher in primary school
Output
8
44

Explanation
The sentence "Lata is an English teacher in primary school",
contains 8 words and 44 characters including seven white spaces.

Example2:
Input
I am a little bird
Output
5
18


Explanation
The sentence "I am a little bird",contains 5 words and 8 characters
including four white spaces.

The input format for testing:

The candidate has to write the code to accept a single string that represents
the sentence.The length of the sentence is less than or equal to buffer size T=200.

The output format for testing:

The output contains two positive integer numbers separated by the new line.
The first number represents the total number of words.
The second number represents the total number of characters in a given sentence.
Additional messages in the output will result in the failure of test cases.

Instructions:
The system doesn't allow any kind of hard-coded input value/values.
Written program code by a candidate will verify against the inputs that will be supplied from the system.
'''

s1=input()
count1=0
count2=0

for i in s1:
    if i==' ':
        count1+=1
for j in s1:
    count2+=1

print(count1+1)
print(count2)
