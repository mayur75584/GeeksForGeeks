

'https://www.biochemithon.in/python-tutorials/python-programs/tcs-xplore-cpa-python-2/'
'Complete this'
class Property:

    def __init__(self,property_type,property_value,max_bid_price):
        self.property_type = property_type
        self.property_value = property_value
        self.max_bid_price = max_bid_price

class Tender:

    def __init__(self,buyerName,propertyType,bidPrice):
        self.buyerName = buyerName
        self.propertyType = propertyType
        self.bidPrice = bidPrice

def bidProperty(property_list,Tender_list):
    nameList=[]

    for i in property_list:
        for j in Tender_list:
            if i.property_type.lower() == j.propertyType.lower():
                pass




if __name__ == '__main__':
    n=int(input())
    property_list=[]
    for i in range(n):
        property_type=input()
        property_value=int(input())
        max_bid_price=int(input())
        p=Property(property_type,property_value,max_bid_price)
        property_list.append(p)
    c=int(input())
    Tender_list=[]
    for j in range(c):
        buyerName=input()
        propertyType=input()
        bidPrice=int(input())
        t=Tender(buyerName,propertyType,bidPrice)
        Tender_list.append(t)
    answer=bidProperty(property_list,Tender_list)


