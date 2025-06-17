'''
Full Question is in this link - https://www.biochemithon.in/python-tutorials/python-programs/tcs-xplore-cpa-python-3/

Create a class DairyProduct with below attributes:

dairyld -> Number
dairyBrand  -> String
productType -> String
price -> Number
grade -> String


Sample Test Cases:
Input 1:

5
011
Ankit
Milk
25
grade3
131
Rahul
Curd
35
Grade1
021
Heritage
Milk
27
Gaade2
055
Kwality
lazzi
40
Grade1
060
Amul
Yogurt
35
Grade1
3
Grade1
10
Grade2
20
Grade3
5
Amul
Milk

Output 1:

No dairy product found

Input 2:

5
011
Aavin
Milk
25
grade3
131
Hatsun
Curd
35
Grade1
021
Heritage
Milk
27
Grade2
055
Kwality
lazzi
40
Grade1
060
Amul
Yogurt
35
Grade1
3
Grade1
25
Grade2
15
Grade3
5
Amul
Yogurt

Output 2:

Dairy Brand: Amul
Price: 43.75


Now let’s see the implementation for this problem statement:
# Create a DairyProduct
# class with its attributes
class DairyProduct :

    # Define a constructor method
    # for initializing its attributes
    def __init__(self, *args) :

        # * is generally used for taking
        # variable number of arguments
        # in function/method

        # args is tuple of arguments
        # so we can access these arguments
        # with indices
        self.dairyId = int(args[0])
        self.dairyBrand = args[1]
        self.productType = args[2]
        self.price = int(args[3])
        self.grade = args[4]

# Create a ProductGrade
# class with its attributes
# and method
class ProductGrade :

    # Define a constructor method
    # for initializing its attributes
    def __init__(self, *args) :

        self.dairyList = args[0]
        self.weightageDict = args[1]

    # Define a method for updating the price
    # as per requirement and return list of
    # tuple of brand name and its updated price
    def priceBasedOnBrandAndType(self, brand, ptype) :

        # empty list
        ans = []

        # iterate through each DairyProduct
        # objects present in the list
        for obj in self.dairyList :

            # if given condition is satisfied then
            # update the price for that brand
            # and appending into the list
            if obj.dairyBrand == brand and obj.productType == ptype :

                obj.price += (obj.price * self.weightageDict[obj.grade]) / 100

                ans.append((brand, obj.price))

        # if list is empty then return
        # None otherwise return
        # that list
        if len(ans) :
            return ans
        else :
            return None

# Main program starts here
if __name__ == "__main__" :

    # read the number of DairyProduct
    n1 = int(input())

    # empty list
    dairyProducts = []

    # Create a n1 number of
    # DairyProduct objects
    for i in range(n1) :

        # reading the data related
        # to DairyProduct class
        dId = input()
        dBrand = input()
        pType = input()
        price = input()
        grade = input().lower()

        # Create DairyProduct object
        # with its attributes
        dpObj = DairyProduct(dId, dBrand, pType, price, grade)

        # adding DairyProduct object
        # to the list
        dairyProducts.append(dpObj)

    #  read the number of dictionary elements
    n2 = int(input())

    # empty dictionary
    weightageDict = {}


    for i in range(n2) :

        # reading the key,value
        # pair for a dictionary
        grade = input().lower()
        value = int(input())

        # insert key,value pair
        # to the dictionary
        weightageDict[grade] = value

    # Create ProductGrade object
    # with its attributes
    pgObj = ProductGrade(dairyProducts, weightageDict)

    # reading brand name and product type
    dairyBrand = input()
    producttype = input()

    # priceBasedOnBrandAndType() method called
    rslt = pgObj.priceBasedOnBrandAndType(dairyBrand, producttype)

    # if rslt is not empty
    # then print required outputs
    # otherwise print message
    # "No dairy product found"
    if rslt :

        for item in rslt :
            print("Dairy Brand:", item[0])
            print("Price:", item[1])

    else :
        print("No dairy product found")
'''

class DairyProduct:

    def __init__(self,dairyId,dairyBrand,productType,price,grade):
        self.dairyId = dairyId
        self.dairyBrand = dairyBrand
        self.productType = productType
        self.price = price
        self.grade = grade

class ProductGrade:
    def __init__(self,dairyList,weightageDict):
        self.dairyList = dairyList
        self.weightageDict = weightageDict

    def priceBasedOnBrandAndType(self,res_dairyBrand,res_productType):
        ans=[]
        for i in self.dairyList:
            if i.dairyBrand==res_dairyBrand and i.productType==res_productType:
                i.price+=(i.price*self.weightageDict[i.grade])/100
                ans.append(res_dairyBrand)
                ans.append(i.price)


        if len(ans)==0:
            return None
        else:
            return ans





if __name__ == '__main__':
    n=int(input())
    list_obj=[]
    for i in range(n):
        dairyId=int(input())
        dairyBrand=input()
        productType=input()
        price=int(input())
        grade=input()
        d=DairyProduct(dairyId,dairyBrand,productType,price,grade)
        list_obj.append(d)
    c=int(input())
    weightageDict={}
    for j in range(c):
        grade=input()
        weightage=int(input())
        weightageDict[grade]=weightage
    res_dairyBrand=input()
    res_productType=input()

    p=ProductGrade(list_obj,weightageDict)
    answer=p.priceBasedOnBrandAndType(res_dairyBrand,res_productType)
    if answer==None:
        print("No dairy product found")
    else:
        # for i in answer:
        print("Dairy Brand:",answer[0])
        print("Price:",answer[1])
#

'Practice'

# class DairyProduct:
#     def __init__(self,dairyId,dairyBrand,productType,price,grade):
#         self.dairyId = dairyId
#         self.dairyBrand = dairyBrand
#         self.productType = productType
#         self.price = price
#         self.grade = grade
#
# class ProductGrade:
#     def __init__(self,dairyList,weightageDict):
#         self.dairyList = dairyList
#         self.weightageDict = weightageDict
#
#     def priceBasedOnBrandAndType(self,dairy_Brand,product_Type):
#         ans=[]
#         for i in self.dairyList:
#             z=[]
#             if (i.dairyBrand.lower()==dairy_Brand.lower()) and (i.productType.lower()==product_Type.lower()):
#                 x=weightageDict[i.grade]
#                 res=i.price+(i.price*(x/100))
#                 i.price=res
#                 z.append(i.dairyBrand)
#                 z.append(i.price)
#                 ans.append(z)
#         if len(ans)==0:
#             return None
#         else:
#             return ans
#
#
# if __name__ == '__main__':
#     n=int(input())
#     lst_obj=[]
#     for i in range(n):
#         dairyId=int(input())
#         dairyBrand=input()
#         productType=input()
#         price=int(input())
#         grade=input()
#         d=DairyProduct(dairyId,dairyBrand,productType,price,grade)
#         lst_obj.append(d)
#     count1=int(input())
#     weightageDict={}
#     for i in range(count1):
#         key=input()
#         value=int(input())
#         weightageDict[key]=value
#     p=ProductGrade(lst_obj,weightageDict)
#     dairy_Brand=input()
#     product_Type=input()
#     ans1=p.priceBasedOnBrandAndType(dairy_Brand,product_Type)
#     if ans1==None:
#         print("No dairy Product Found")
#     else:
#         for i in ans1:
#             print('Dairy Brand:',i[0])
#             print('Price:',i[1])




