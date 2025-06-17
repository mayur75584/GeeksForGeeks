'''
 Create a class Bill with attributes mobile number and payment bill.
 Create another class mobile with attributes serviceprovider, mobilenumber, dataused, payment method. Service provider may be airtel or jio.
 Data used is integer values in Gigabytes(GB). Payment method may be paytm, gpay, amazon and soon.
 Create a method calculatebill that takes the list of objects and calculates the bill and returns the list of objects of class bill with mobile number and paymentbill.
The payment is calculated as follows:
1. If the service provider is airtel, the bill is Rs.11 for every 1GB used and if it is jio, the bill is Rs.10 for every 1GB used.
2.If the payment method is paytm there is a cash back of 10% of the total bill for airtel users only.
The bill is calculated and rounded off after deducing the cashback value.

Sample Input:
3
airtel
123
16
paytm
airtel
456
10
amazon
jio
789
10
paytm

Sample Output:


(123,158)
(456,110)
(789,100)
'''

class Bill:

    def __init__(self,mobileNumber,paymentBill):
        self.mobileNumber = mobileNumber
        self.paymentBill = paymentBill

class Mobile:

    def __init__(self,serviceprovider,mobileNumber,dataused,paymentmethod):
        self.serviceprovider = serviceprovider
        self.mobileNumber = mobileNumber
        self.dataused = dataused
        self.paymentmethod = paymentmethod

    def calculatebill(self,list_obj):
        bill=[]
        totalbill=0
        for i in list_obj:
            if i.serviceprovider=='airtel':
                billamount=i.dataused*11
                if i.paymentmethod=='paytm':
                    totalbill=billamount-(billamount*0.1)
                else:
                    totalbill=billamount
            elif i.serviceprovider=='jio':
                billamount=i.dataused*10
                totalbill=billamount
            bill.append(Bill(i.mobileNumber,int(totalbill)))
        return bill




n=int(input())
list_obj=[]
for i in range(n):
    serviceprovider=input()
    mobileNumber=int(input())
    dataused=int(input())
    paymentmethod=input()

    list_obj.append(Mobile(serviceprovider,mobileNumber,dataused,paymentmethod))

answer1=Mobile("",0,0,"").calculatebill(list_obj)
for j in answer1:
    print('('+str(j.mobileNumber)+","+str(j.paymentBill)+')')


