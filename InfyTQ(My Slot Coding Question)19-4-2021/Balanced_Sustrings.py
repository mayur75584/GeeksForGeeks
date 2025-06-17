'''
Consider a non-empty instr consisting of lower case alphabets ONLY.Identify
and print outarr based on the following logic:

1. Identify all the unique balanced substrings that can be formed using
instr and add them to outarr in the increasing order of their length.
1.1. A balanced substring is one where ALL the characters of the substring
can be partitioned into two groups G1 and G2 such that G1==G2.
2.If two or more balanced substrings have the same length,add them to outarr
in alphabetical order
3.Print -1,if no balanced substring can be formed using instrr.

Input Format:
First line contains instr
Read the input from the standard input stream.

Output format:
Print outarr with elements separated by ','(comma) or -1 accordingly to the standard
output stream.

Sample Input-1:
abccbaa

Sample Output-1:
aa,cc,bccb,abccba,bccbaa

Explanation:
For the given input instr,balanced substrings are:
.'cc' with length 2
.'bccb' with length 4
.'abccba' with length 6 and
.'aa' with length 2
.'bccba' with length 6

Balanced substrings 'cc' and 'aa' have the same length as well as 'abccba'
and 'bccbaa'.Adding the identified balanced substrings to outarr based on the increasing
order of their length and arranging the balanced substrings of the same length in the
alphabetical order results in 'aa','cc','bccb','abccba','bccbaa'.

Sample Input-2:
abcba

Sample output-2:
-1

Explanation:
For the given input instr,no balanced substring can be formed using instr. Hence
the output

'''

input_str = input()
temp = set()
a = 2
list1 = []


for i in range(len(input_str)):
    for j in range(len(input_str) - a + 1):
        n = input_str[j:j+a]
        if all(map(lambda x:not n.count(x)%2,n)):temp.add(n)

    x = sorted(temp)
    list1.extend(x)
    temp.clear()

    a+=2

if list1:
    print((",".join(list1)))
else:
    print(-1)