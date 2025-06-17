'''
Create a class Painting with the below attributes:

paintingID: string type
painterName: string type
paintingPrice: int type
painting type: string type

create constructor (__init__ method) which takes all the above attributes in the same sequence.
Method will set the values passed as an argument to the attributes of the Painting object created.
Create a class ShowRoom with the attribute as a list of paintings obtained from the main function.
paintingList: of type List of Painting objects.
Define two methods inside ShowRoom class.
getTotalPaintingPrice: It takes a string representing the painting type as argument, and returns the total painting price of the paintings of the given type from the paintingList of the ShowRoom. If no paintings of the given type is present in the list then the method returns None.
getPainterWithMaxCountOfPaintings: It finds the name of the painter from the paintingList of the ShowRoom who has the highest count of Paintings. If more than one painter has the highest count of paintings, the method returns the name of the painter whose name comes first as per the alphabetical orders(A-Z).

Instructions to write the main function:
a. You would require to write the main section completely. Hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the “sample input description section” mentioned below and to read the data in the same sequence.
c. Create the respective objects(Painting and ShowRoom) with the given sequence of arguments to fulfill the __init__ method as mentioned in requirements, defined to the respective classes referring to the below instructions.

    i) Create a list of Painting objects which will be passes as argument while calling the functions in main. To create the list,
        a. Read a number for the count of Painting objects to be created and added to the list.
        b. Create a Painting object after reading the data related to it and add the objects to the list to be created. This points repeats for the number of Paintings object to be created(considered in the first line of input) as per point #c.i.a
    ii) Create the ShowRoom object by passing the list created in point #c.i

d. Read a value for painting type to be passed as argument to the method getTotalPaintingPrice.
e. Call the method getTotalPaintingPrice by passing the value read in point #d.
f. Call the method getPainterWithMaxCountOfPaintings.
g. Display the value returned by the method getTotalPaintingPrice. If function return None,Then display “Painting not found”(excluding the quotes).
h. Display the value returned by the method getPainterWithMaxCountOfPaintings.
You can use/refer the below-given sample input and output for more details of the format for input and output.
Sample Input description:
a) First line represents the integer value which represents the number of Painting objects.
b) Next lines of input represents one Painting specific data as below one by one in each line.

paintingId
paintingName
paintingPrice
paintingType

c) The points #b repeats for the number of objects mentioned in the point #a.
d) The last line of input is the painting type to be passed as argument to the method getTotalPaintingPrice.

Consider Case Insensitive for this problem statement.
Consider below sample input and output to verify your implementations:
Sample test case 1 : input:

5
101
Raman
50000
portrait
102
kamaal
30000
portrait
103
Raman
25600
modern
104
sumiran
31000
landscape
105
sumiran
50000
Modern
Modern

Sample test case 1: output:

75600
raman

Sample test case 2 : input:

5
101
Raman
50000
portrait
102
kamaal
30000
portrait
103
ankit
25600
modern
104
sumiran
31000
landscape
105
sumiran
50000
Modern
portrait

Sample test case 2 : output:

80000
sumiran

Now, Let’s see the Solution:
# Create a Painting class
class Painting:

  # Create a constructor method
  """
  pid for paintingID
  pname for painterName
  pprice for paintingPrice
  ptype for painting type
  """
  def __init__(self, arg1, arg2, arg3, arg4):
    self.pid = arg1
    self.pname = arg2
    self.pprice = arg3
    self.ptype = arg4

# Create a ShowRoom class
class ShowRoom :

    # Create a constructor method
    # plist for paintingList
    def __init__(self, arg1):
         self.plist = arg1

    # Define method for this class
    """
    It takes a string representing the painting type
    as argument, and returns the total painting
    price of the paintings of the given type
    from the paintingList of the ShowRoom.
    If no paintings of the given type is
    present in the list then method returns None.
    """
    def getTotalPaintingPrice(self, ptype) :

        tprice = 0
        flag = 0
        for obj in self.plist :
            if obj.ptype == ptype :
                flag = 1
                tprice += obj.pprice

        if flag :
            return tprice

        return None

    # Define method for this class
    """
    It finds the name of the painter from
    the paintingList of the ShowRoom who
    has the highest count of Paintings.
    If more than one painter has highest
    count of paintings, method returns that
    name of the painter whose name comes first
    as per the alphabetical orders(A-Z).
    """
    def getPainterWithMaxCountOfPaintings(self) :
        nameCount = {}
        rslt = []

        for obj in self.plist :
            if obj.pname in nameCount:
                nameCount[obj.pname] += 1
            else :
                nameCount[obj.pname] = 1

        # sort a dictionary based on values
        # returns list of tuples of key,value
        sort = sorted(nameCount.items(), key = lambda x : x[1])

        # takes last tuple element 2nd value
        val = sort[-1][1]

        """
        If more than one painter has highest
        count of paintings, method returns that
        name of the painter whose name comes first
        as per the alphabetical orders(A-Z).
        """
        for value in sort :
            if val == value[1]:
                rslt.append(value[0])

        if len(rslt) > 1 :
            rslt.sort()
            return rslt[0]
        else :
            return sort[-1][0]

# main program starts here
if __name__ == "__main__" :

    # take input for number
    # of Painting object created
    n = int(input())

    # take empty list
    plist = []

    # take values for particular object
    for val in range(n) :

        # case insensitiveness consider
        val1 = input().lower()
        val2 = input().lower()
        val3 = int(input())
        val4 = input().lower()

        # create a object with initial value
        pobj = Painting(val1, val2, val3, val4)

        plist.append(pobj)

    # create a object with initial value
    sobj = ShowRoom(plist)

    ptype = input().lower()

    # method called
    rslt = sobj.getTotalPaintingPrice(ptype)

    if rslt :
        print(rslt)

    else :
        print("Painting not found")

    # method called
    rslt = sobj.getPainterWithMaxCountOfPaintings()

    print(rslt)
'''
class Painting:

    def __init__(self,paintingID,painterName,paintingPrice,painting_type):
        self.paintingID = paintingID
        self.painterName = painterName
        self.paintingPrice = paintingPrice
        self.painting_type = painting_type

class ShowRoom:

    def __init__(self,paintingList):
        self.paintingList = paintingList

    def getTotalPaintingPrice(self,paintingType):
        sum1=0
        for i in self.paintingList:
            if i.painting_type==paintingType:
                sum1+=i.paintingPrice
        if sum1==0:
            return None
        else:
            return sum1

    def getPainterWithMaxCountOfPaintings(self):
        dict={}
        result=[]
        for i in self.paintingList:
            if i.painterName in dict:
                dict[i.painterName]+=1
            else:
                dict[i.painterName]=1
        #Important Logic
        #sort dictionary based on values return list of tuples of key,value
        sort=sorted(dict.items(),key=lambda x:x[1])

        #takes last tuple element 2nd value
        val=sort[-1][-1]

        """
                If more than one painter has highest
                count of paintings, method returns that
                name of the painter whose name comes first
                as per the alphabetical orders(A-Z).
        """
        for i in sort:
            if val==i[1]:
                result.append(i[0])
        if len(result)>1:
            result.sort()
            return result[0]
        else:
            return sort[-1][0]

if __name__ == '__main__':
    n=int(input())
    list_obj=[]
    for i in range(n):
        paintingID = input()
        painterName = input()
        paintingPrice = int(input())
        painting_type = input()
        p=Painting(paintingID,painterName,paintingPrice,painting_type)
        list_obj.append(p)
    paintingType=input()
    s=ShowRoom(list_obj)
    answer1=s.getTotalPaintingPrice(paintingType)
    answer2=s.getPainterWithMaxCountOfPaintings()
    if answer1!=None:
        print(answer1)
    else:
        print("Painting Not Found")

    print(answer2)

'Practice'
# class Painting:
#     def __init__(self, paintingID, painterName, paintingPrice, paintingType):
#         self.paintingID = paintingID
#         self.painterName = painterName
#         self.paintingPrice = paintingPrice
#         self.paintingType = paintingType
#
#
# class ShowRoom:
#     def __init__(self, paintingList):
#         self.paintingList = paintingList
#
#     def getTotalPaintingPrice(self, painting_type):
#         sum1 = 0
#         for i in self.paintingList:
#             if i.paintingType.lower() == painting_type.lower():
#                 sum1 += i.paintingPrice
#         if sum1 == 0:
#             return None
#         else:
#             return sum1
#
#     def getPainterWithMaxCountOfPaintings(self):
#         dict = {}
#         for i in self.paintingList:
#             if i.painterName.lower() not in dict:
#                 dict[i.painterName.lower()] = 1
#             else:
#                 dict[i.painterName.lower()] += 1
#         z = sorted(dict.items(), key=lambda x: x[1], reverse=True)
#         print(z)
#         res=''
#         for i in z:
#             res=i[0]
#             return res
#
# if __name__ == '__main__':
#     n = int(input())
#     lst_obj = []
#     for i in range(n):
#         paintingID = input()
#         painterName = input()
#         paintingPrice = int(input())
#         paintingType = input()
#         lst_obj.append(Painting(paintingID, painterName, paintingPrice, paintingType))
#     painting_type = input()
#     s = ShowRoom(lst_obj)
#     ans1 = s.getTotalPaintingPrice(painting_type)
#     ans2 = s.getPainterWithMaxCountOfPaintings()
#     if ans1 == None:
#         print('Painting Not Found')
#     else:
#         print(ans1)
#     print(ans2)





