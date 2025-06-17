'''
Create a class called apartment with attributes flat-number, owner name, electicitybillamount.
Create another class apartment_demo with def init(self): pass to create a method getSecondMinBill that takes the list of objects and gives the second minimum electricity bill as output.

Sample Input:
3
1000
Hari
5000
1001
Hena
5002
1002
Harsha
5001

Sample Output:
5001

Sample Input-
5
1
a
10
2
b
20
3
c
30
4
d
30
5
e
40

Sample Output-
20
'''

class apartment:

    def __init__(self,flat_number,owner_name,electicitybillamount):
        self.flat_number = flat_number
        self.owner_name = owner_name
        self.electicitybillamount = electicitybillamount

class apartment_demo:
    def __init__(self):
        pass

    @classmethod
    def getSecondMinBill(cls,list_obj):
        bill=[]
        for i in list_obj:
            if i.electicitybillamount not in bill:
                bill.append(i.electicitybillamount)
        z=sorted(bill)
        return z[1]



n=int(input())
list_obj=[]
for i in range(n):
    flat_number=int(input())
    owner_name=input()
    electicitybillamount=int(input())
    list_obj.append(apartment(flat_number,owner_name,electicitybillamount))

answer1=apartment_demo.getSecondMinBill(list_obj)
print(answer1)

'''
Online Found Solution
class apartment:
    def __init__(self,flatNumber,ownerName,eBillAmt):
        self.flatNumber = flatNumber
        self.ownerName = ownerName
        self.eBillAmt = eBillAmt

class apartment_demo:
    def __init__(self):
        pass
    def getSecondMinBill(self,billList):
        bills = []
        for i in billList:
            bills.append(i.eBillAmt)
        bills.sort()
        second = bills[1]
        return print(second)

if __name__=='__main__':
    count = int(input())
    billList = []
    for i in range(count):
        flatNumber = int(input())
        ownerName = input()
        eBillAmt = int(input())
        billList.append(apartment(flatNumber,ownerName,eBillAmt))
    output = apartment_demo().getSecondMinBill(billList)
 
'''




