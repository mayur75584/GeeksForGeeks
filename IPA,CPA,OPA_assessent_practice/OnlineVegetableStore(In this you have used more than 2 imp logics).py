'''
Online Vegetable Store

Create a class Vegetable with the below attributes:
name of type String name of the vegetable price of type float //price ( in Rupees ) of the Fx: Kilogram quantity of type int ,/ quantity — number of units / Number of Kilograms
Create the init method which takes all parameters in the above sequence. The method should set the value of attributes with the parameter values received from main function.
Create another class Store with the below attribute: storeName of type String /specifies the vegList of type List L ist of Vegetable which takes all sequence. The method should set the value of attributes with the parameter values received from main.
Create method inside the Store class with name categorizeVegetablesAlphabetically
This method use and traverse the list of Vegetables(vegList) and returns a dictionary of alphabetically categorized and sorted vegetable names(name), where in key represent an alphabet character(e.g. ‘a’, ‘b’, se etc) and value represents a tuple, containing vegetable names that starts with that specific character as per key. Both the keys and values are sorted in alphabetically. The comparison needs to be case insensitive. If there are more vegetable names starts with the respective alphabet (which is acting as the key for the respective tuple of vegetable names), then the list of vegitable names also needs to be sorted.
e.g. Ex on fruits, resultant dictionary data looks like : fas:(‘ananas’, ‘apple), ’13: (‘banana’), ‘p’:(‘pineapple)) Here ‘a’ ,’b’ and ‘p’ (excluding the single quote ) represents the keys of dictionary and (‘ananass, ‘apple), (‘banana’), (pineapple’) ,excluding the ‘single quote and brackets’ represents the tuple for respective and corresponding keys(a , b, p ).
For more details refer the sample test case input and respective output
Create another method inside Store class with the name filterVegetablesForPriceRange This method takes minimum price and maximum price in Rupees as input parameters and return a list of alphabetically sorted vegetable names(name), where in the Vegetable unit price falls in the given range(minimum price and maximum price). This method use and traverse the list of Vegetables(vegList) for comparing the price of vegetable per Unit with the given range
If there is no vegetable in given price range, the method returns an empty list and based on the value main function should print “No Vegetable(s) in the given price range” (Excluding the double quotes) .
For more details refer the sample test case input and respective output
You can use/refer the below given sample input and output to verify your solution using ‘ Custom Input ‘ option ,down the coding editor
Instructions to write main and to call the methods of the classes defined above:

​

a. You would required to write the main function completely, please follow the below instructions for the same.

b. You would required to write the main program which is inlign to the “sample input description section” mentioned below and to read the data in the same sequence.

c. Create the respective objects(Vegetable and Store) with the given sequence of arguments to fulfill the constructor requirement defined in the respective class.

​

i.Create a Vegetable object after reading the data related to Vegetable and add the Vegetable object to list of Vegetable objects, This point repeats for the number of Vegetable objects you want to create and add to Vegetable list or as mentioned in the first line of input in the input data

ii. Create Store object by passing the Store name and list of Vegetable objects ( created and as mentioned in above point# c.i ) as the arguments to the constructor .

​

d. Call the methods ( categorizeVegetablesAlphabetically and f ilterVegetablesForPriceRange) mentioned above from the main function in the same order , they appear in the question text. e. Display the data returned by the functions , in the main program as per the order of calling the functions and as per the format mentioned in the sample output. f. If None/empty list is returned.

y 1 terVegeta function then display “No Vegetable found for given prince range” (excluding the double quotes) in the main function.


Sample Input (below) description:


• The first input line represents the count of vegetable objects to create and add to the vegetable list.

• Second set of inputs lines(2nd to 4th ) represents vegetable name, vegetable price and quantity of first vegetable object and this set(Name,Price and Quantity for each different vegetable object ) of input is repeated for the number of vegetable objects mentioned in the first line of input .

• Next inputs represents store name(third line of input from last).

• Last two lines represents the minimum price and maximum price to be supplied to the filterVegetablesForPriceRange to find the vegitables, whose price falls in the range

​

Sample Testcase Input:

​

5
corn
20.0
30
onion
10.0
15
potato
30.0
10
cucumber
5.0
10
brocolli
24.5
8
big
bazaar
5.0
25.0


SampleTestcaseOutput:


b
brocolli
c
corn
cucumber
o
onion
P
potato
5.0-25.0
brocolli
corn
cucumber
onion

​

​

Solutions:

​

import string
class Vegetable:
    def __init__(self, n, p, q):
        self.name = n
        self.price = p
        self.quantity = q

class Store:
    def __init__(self, s, v):
        self.storeName = s
        self.vegList = v

    def categorizeVegetablesAlphabetically(self):
        self.vegList.sort(key= lambda x: x.name)
        a = list(string.ascii_lowercase)
        r = {}
        for i in a:
            temp = []
            for j in self.vegList:
                if i == j.name[0]:
                    temp.append(j.name)
            if len(temp) >0:
                r[i] = tuple(temp)
        return r

    def filterVegetablesForPriceRange(self, min, max):
        self.vegList.sort(key= lambda x: x.name)
        r = []
        for i in self.vegList:
            if min <= i.price <= max:
                r.append(i.name)
        return r

count = int(input())
t = []

for i in range(count):
    n1 = input()
    p1 = float(input())
    q1 = int(input())
    v = Vegetable(n1.lower(),p1,q1)
    t.append(v)

name = input()
min1 = float(input())
max1 = float(input())
store = Store(name,t)
catVegAlpha = store.categorizeVegetablesAlphabetically()
priceList = store.filterVegetablesForPriceRange(min1, max1)

for keys, value in catVegAlpha.items():
    print(keys)
    for x in value:
        print(x)
print(str(min1) + '-' + str(max1))
if len(priceList) > 0:
    for x in priceList:
        print(x)
else:
    print("No Vegetable(s) in the given price range")
'''

import string
class Vegetable:

    def __init__(self,vegetable_name,vegetable_price,quantity):
        self.vegetable_name = vegetable_name
        self.vegetable_price = vegetable_price
        self.quantity = quantity

class Store:

    def __init__(self,store_name,list_obj):
        self.store_name = store_name
        self.list_obj = list_obj

    def categorizeVegetablesAlphabetically(self):
        self.list_obj.sort(key=lambda x:x.vegetable_name) #Logic to sort dictionary with respect to vegetables_name
        a=list(string.ascii_lowercase) #list of string of all lowercase
        result={}
        for i in a:
            r=[]
            for j in self.list_obj:
                if i==j.vegetable_name[0]:
                    r.append(j.vegetable_name)
            if len(r)>0:
                result[i]=tuple(r)
        return result
    def filterVegetablesForPriceRange(self,min_price,max_price):
        self.list_obj.sort(key=lambda x:x.vegetable_name)
        r=[]
        for i in self.list_obj:
            if min_price<=i.vegetable_price<=max_price:
                r.append(i.vegetable_name)
        return r





if __name__ == '__main__':
    n=int(input())
    list_obj=[]
    for i in range(n):
        vegetable_name = input()
        vegetable_price = float(input())
        quantity = int(input())
        v=Vegetable(vegetable_name,vegetable_price,quantity)
        list_obj.append(v)
    store_name=input()
    min_price = float(input())
    max_price = float(input())

    store=Store(store_name,list_obj)

    answer1=store.categorizeVegetablesAlphabetically()

    answer2=store.filterVegetablesForPriceRange(min_price,max_price)

    for keys,values in answer1.items():
        print(keys)
        for x in values:
            print(x)
    print(str(min_price)+'-'+str(max_price))
    if len(answer2)>0:
        for i in answer2:
            print(i)
    else:
        print("No Vegetable found for given price range")

'Practice'
# import string
# class Vegetable:
#     def __init__(self,vegitableName,vegitablePrice,quantity):
#         self.vegitableName = vegitableName
#         self.vegitablePrice = vegitablePrice
#         self.quantity = quantity
# class Store:
#     def __init__(self,store_name,vegList):
#         self.store_name = store_name
#         self.vegList = vegList
#     def categorizeVegitablesAlphabetically(self):
#         dict={}
#         self.vegList.sort(key=lambda x:x.vegitableName)
#         a=list(string.ascii_lowercase)
#
#         for i in a:
#             res=[]
#             for j in self.vegList:
#                 if i==j.vegitableName[0].lower():
#                     res.append(j.vegitableName.lower())
#             if len(res)!=0:
#                 dict[i]=tuple(sorted(res))
#         print(dict)
#         return dict
#
#
#     def filterVegitablesForPriceRange(self,min_price,max_price):
#         res=[]
#         for i in self.vegList:
#             if min_price<=i.vegitablePrice<=max_price:
#                 res.append(i.vegitableName)
#         return sorted(res)
#
# if __name__ == '__main__':
#     n=int(input())
#     lst_obj=[]
#     for i in range(n):
#         vegitableName = input()
#         vegitablePrice = float(input())
#         quantity = int(input())
#         lst_obj.append(Vegetable(vegitableName,vegitablePrice,quantity))
#     store_name=input()
#     min_price=float(input())
#     max_price=float(input())
#     s=Store(store_name,lst_obj)
#     ans1=s.categorizeVegitablesAlphabetically()
#     ans2=s.filterVegitablesForPriceRange(min_price,max_price)
#
#     for i,j in ans1.items():
#         print(i)
#         for x in j:
#             print(x)
#     print(str(min_price)+'-'+str(max_price))
#     if len(ans2)==0:
#         print('No Vegitables in given range Price')
#     else:
#         for i in ans2:
#             print(i)







