'''
Consider an array inarr of positive integers. Identify and print outarr based on the
below logic:
1. For every element,elem, in inarr, identify the value, val, from the set of elements
on the right side of elem which is greater than elem and occurs the most. Add val to outarr.

2. If more than one val is identified, then choose the lowest value and add it to
outarr.

3. Add -1 to outarr if no val can be identified for an elem

Assumption:- zero is a positive number

Input Format:
Read the input array inarr with the elements separated by ','(comma) from the standard
Input stream.

Output Format:
Print outarr with the elements separated by ','(comma) to the standard output stream

Sample Input1:
4,5,2,25,10,5,10,3,10,5

Sample Output1:
5,10,10,-1,-1,10,-1,5,-1,-1

Explanation:

For the given input array, inarr considering the:

1. 1st element,elem,4:
   The set of elements on the right side of 4 and greater than 4 are
    <> 5 occuring thrice
    <> 25 occuring once
    <> 10 occuring thrice

5 and 10 occur the most. The lowest value amongst 5 and 10 i.e 5 is
added to outarr

2. 2nd element,elem,5:
   The set of elements on the right side of 5 and greater than 5 are
    <> 25 occuring once
    <> 10 occuring thrice

10 occurs the most. 10 is added to outarr.

Similarly,

<> 3rd element,elem,2:
    10 is added to outarr
<> 4th element,elem,25:
     -1 is added to outarr
<> 5th element,elem,10:
     -1 is added to outarr
<> 6th element,elem,5:
    10 is added to outarr
<> 7th element,elem,10:
   -1 is added to outarr
<> 8th element,elem,3:
    5 is added to outarr

Hence the output
'''

# lst=list(map(int,input().split(',')))
# lst1=[]
# lst=[4,5,2,25,10,5,10,3,10,5]
# for i in range(len(lst)):
#     max=0
#     final=999
#     for j in range(i+1,len(lst)):
#         if lst[i]<lst[j]:
#             temp=lst[j:].count(lst[j])
#             if max<temp:
#                 final=lst[j]
#                 max=temp
#             elif max==temp:
#                 final=min(final,lst[j])
#     if final==999:
#         lst1.append(-1)
#     else:
#         lst1.append(final)
# print(lst1)

############################################################################################
# input_list = list(map(int, input().split(',')))
# for i in range(len(input_list)):
#     final = 999999
#     max = 0
#
#     for j in range(i+1,len(input_list)):
#         if input_list[i]<input_list[j]:
#             temp=input_list[j:].count((input_list[j]))
#             if max<temp:
#                 final = input_list[j]
#                 max = temp
#             elif max == temp:
#                 final = min(final, input_list[j])
#
#     if final == 999999:
#         input_list[i] = -1
#     else:
#         input_list[i] = final
#
# input_list = list(map(str, input_list))
# print(','.join(input_list))