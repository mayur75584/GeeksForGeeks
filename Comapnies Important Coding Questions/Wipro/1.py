'''
1.
Write a program to implement a bubble sort algorithm for sorting the elements of
an array.
'''
#
list1=list(map(int,input().split(',')))
n=len(list1)

for i in range(0,n-1):
    for j in range(0,n-1-i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
for k in range(len(list1)):
    print(list1[k])



### Function

# def bubbleSort(list1):
#     n=len(list1)
#
#     for i in range(n-1):
#         for j in range(0,n-1-i):
#             if list1[j]>list1[j+1]:
#                 temp=list1[j]
#                 list1[j]=list1[j+1]
#                 list1[j+1]=temp
#
# list1=list(map(int,input().split(',')))
#
# bubbleSort(list1)
#
# for i in range(len(list1)):
#     print(list1[i])