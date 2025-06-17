'''
Write the code to define a class to create objects of type
Toy with following attributes:

ToyID,
ToyType,
Price,
Discount Applicable
Define a method in the class which sets value to the first 3 attribute
by taking values as argument in the sequence mentioned above
while creating a Toy object.

Value for Discount Applicable should be set to 0.

Write the code to define a Class to create a Store object
with the following attributes.

A list of Toy Objects
Applicable Discount Details for different Toy Types are stored as key:value pairs as
"Toy Type: discount rate".
Define a method in the class which sets values to the attributes by
taking values as argument in the sequence mentioned above while
creating a Store object.

Define another method inside the class to fulfill the requirement defined below:

This method will be used to calculate discount for the Toys in the
Toy list of the Store.

For each Toy in the Toy List of the Organization method
will calculate the discount amount based on the Toy Type
and the discount rate for that Toy Type maintained by the Store.
Method will update the value of the discount applicable attribute
of the Toy with the value(discount amount) calculated using
the following formula

Discount Applicable = price*(discount rate/100)

If the Toy Type of a Toy is not found in the discount
details of the Store as key for any key:value pairs
Discount Applicable is considered as 0.

This method will not return any value.

For more clarity, please refer to the sample input and output below.

Note: All the searches should be case insensitive

Instructions to write main section of the code.

1. You should require to write the main section completely,
hence please follow the below instructions for the same.

2.You would require to write the main program which is inline to the "sample input
description section" mentioned below and to read the data in the same sequence.

3.Create the respective objects(Toy and Store) with the given sequence of arguments
to fulfill the requirements of the methods defined in the respective classes to initialize
the attribute while creating objects referring to the below instructions.

a- Create a list of Toy objects for the Store Object to be created.

To create the list:

a) First read the number of Toy objects you want to store in the list.
b) Create a Toy object after reading the data related to it.
Toy id,Toy Type and Price and add the object to a list of
Toy objects to be provided to the Store object for the Toy List
attribute. This point repeats for the number of Toy objects(considered
in the first line of input) to be created.

b- Create a list of "Toy Type; dicount rate"
pairs(dictionary) for the Store object to be created.

To create the list read values for 3 pairs of values for
"Toy Type: discount rate" and add to the list.

c- Create Store object by passing the ToyList(created above
in point #3.a) and the list of "Toy Type:dicount rate"
pairs(created in point #3.b) as the arguments.

4.Call the second method defined in the Store to calculate
the discount for the Toys in the Toy list of the Store.

5.Print the Toy ID,Price and the Price after discount for each
Toy in the Toy List of the Store one by one(with a single space between
each value).

In the output, the details of the toy with highest discount amount should
be in the top of the list(i.e In the descending order of "Price after discount")

Refer to sample output for more details on format pf the output

Sample Input(below) description

1) The first input to be given is the count of Toy objects to be created
and added to the Toy list of the Store class.
2)The next set of inputs are the Toy Id, Toy Type and Price of the
for each Toy object taken one after another and is repeated for the
number of Toy objects given in the point#1
3)The next input refers the values for 3"Toy Type:discount rate"pairs
for the list for Applicable Discount Details for different Toy Types
of the Store.

Sample Input:
4
101
puzzle
550
102
Light and sound
700
103
puzzle
600
104
Soft Toy
1500
Soft Toy
12
puzzle
15
electronics
10

Output:

104 1500 1320.0
103 600 510.0
101 550 467.5
102 700 700
'''

class Toy:
    def __init__(self,ToyID,ToyType,Price,DiscountApplicable=0):
        self.ToyID = ToyID
        self.ToyType = ToyType
        self.Price = Price
        self.DiscountApplicable = DiscountApplicable

class Store:
    def __init__(self,lst_obj,lst):
        self.lst_obj = lst_obj
        self.lst = lst

    def Organization(self):
        for i in self.lst:
            x,y=i[0],i[1]
            # print(x,y)
            for j in self.lst_obj:
                if x.lower()==j.ToyType.lower():
                    dis=j.Price*(y/100)
                    j.DiscountApplicable=j.Price-dis


if __name__ == '__main__':
    n=int(input())
    lst_obj=[]
    for i in range(n):
        ToyID=int(input())
        ToyType=input()
        Price=int(input())
        t=Toy(ToyID,ToyType,Price)
        lst_obj.append(t)
    dict1={}
    for i in range(3):
        Toy_type=input()
        Discount_rate=int(input())
        dict1[Toy_type]=Discount_rate
    # print(dict1)
    lst=list(dict1.items()) #notice here you need to use .items() else it will make only list of keys
    # print(lst)

    s=Store(lst_obj,lst)
    s.Organization()
    z=[]
    for i in lst_obj:
        # print(i.ToyType,i.DiscountApplicable)
        z.append(i.DiscountApplicable)
    z.sort(reverse=True)
    # print(z)
    for i in z:
        if i!=0:
            for j in lst_obj:
                if i==j.DiscountApplicable:
                    print(j.ToyID,end=' ')
                    print(j.Price,end=' ')
                    print(j.DiscountApplicable)
        elif i==0:
            for j in lst_obj:
                if i==j.DiscountApplicable:
                    print(j.ToyID,end=' ')
                    print(j.Price,end=' ')
                    print(j.Price)



'Practice'

# class Toy:
#     def __init__(self,ToyID,ToyType,Price,DiscountApplicable=0):
#         self.ToyID = ToyID
#         self.ToyType = ToyType
#         self.Price = Price
#         self.DiscountApplicable = DiscountApplicable
#
# class Store:
#     def __init__(self,lst_obj,lst):
#         self.lst_obj = lst_obj
#         self.lst = lst
#
#     def Organization(self):
#         for i in lst:
#             for j in lst_obj:
#                 if i[0].lower()==j.ToyType.lower():
#                     x=j.Price*(i[1]/100)
#                     j.DiscountApplicable=j.Price-x
#
#
#
# if __name__ == '__main__':
#     n=int(input())
#     lst_obj=[]
#     for i in range(n):
#         ToyID = int(input())
#         ToyType = input()
#         Price = int(input())
#         t=Toy(ToyID,ToyType,Price)
#         lst_obj.append(t)
#     dict={}
#     for i in range(3):
#         Toy_Type=input()
#         discount_rate=int(input())
#         dict[Toy_Type]=discount_rate
#     lst=list(dict.items())
#     s=Store(lst_obj,lst)
#     s.Organization()
#     x=[]
#     for i in lst_obj:
#         x.append(i.DiscountApplicable)
#     x=sorted(x,reverse=True)
#     for i in x:
#         for j in lst_obj:
#             if i==0 and i==j.DiscountApplicable:
#                 print(j.ToyID,end=' ')
#                 print(j.Price,end=' ')
#                 print(j.Price)
#
#             elif i==j.DiscountApplicable:
#                 print(j.ToyID,end=' ')
#                 print(j.Price,end=' ')
#                 print(j.DiscountApplicable)











