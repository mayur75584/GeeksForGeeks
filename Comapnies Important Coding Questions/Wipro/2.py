'''
2.
You are playing an online game. In the game, a list of N numbers is given. The
player has to arrange the numbers so that all the odd numbers of the list come
after the even numbers. Write an algorithm to arrange the given list such that
all the odd numbers of the list come after the even numbers.
Input
The first line of the input consists of an integer num, representing the size of
the list(N). The second line of the input consists of N space-separated integers
representing the values of the list
Output
Print N space-separated integers such that all the odd numbers of the list come
after the even numbers
Example
Sample Input
8
10 98 3 33 12 22 21 11
Sample Output
10 98 12 22 3 33 21 11
'''
#Incomplete code

# num=int(input())

# list1=[]
# list1=list(map(int,input().split()[:num]))

# list1=[]
# for j in range(1,num+1):
#     list1.append([int(i) for i in input().split()])

# list1=list(map(int,input().split()))
# even=[]
# odd=[]
# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# # print(even,odd)
# even1=''
# odd1=''
#
# for j in even:
#     even1=" ".join(str(even))
#
# print(even1)
#
# for k in odd:
#     odd1=" ".join(str(odd))
# print(odd1)

# even=''
# odd=''
# for i in list1:
#     if i%2==0:
#         even+=str(i)+' '
#         print(even)
#     else:
#         odd+=str(i)+' '
# # print(even,odd)
# # even=''.join(even)
# # print(even)
# # odd=''.join(odd)
# # print(odd)
# res=even+odd
# print(res)

num=int(input())
list1=list(map(int,input().split()))

even1=[]
odd1=[]
for i in list1:
    if i%2==0:
        even1.append(i)
    else:
        odd1.append(i)

# print(even1,odd1)

for j in odd1:
    even1.append(j)
# print(even1)

for k in even1:
    print(k,end=" ")













