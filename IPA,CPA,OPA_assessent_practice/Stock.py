'''
Create a class Stock having attributes StockName,StockSector,StockValue. Create a method getStockList with takes a list of Stock objects and a StockSector(string) and returns a list containing stocks of the given sector having value more than 500.

input:

3

TCS

IT

1000

INFY

IT

400

BMW

Auto

1200

IT

Output:​

TCS

​Solution:

class Stock:
  def __init__(self,sn,ss,sv):
    self.sn=sn
    self.ss=ss
    self.sv=sv
class StockDemo:
  def __init__(self):
    self.a=10
  def gets(self,l,s):
    k=[]
    for i in l:
      if(i.ss==s and i.sv>500):
        k.append(i)
    return k


if __name__==’__main__’:
  c=input()
  p=[]
  for i in range(c):
    sn=raw_input()
    ss=raw_input()
    sv=input()
    o=Stock(sn,ss,sv)
    p.append(o)
  s=raw_input()
  pra=StockDemo()
  l=pra.gets(p,s)
  for i in l:
      print i.sn,i.sv
'''
class Stock:

    def __init__(self,StockName,StockSector,StockValue):
        self.StockName = StockName
        self.StockSector = StockSector
        self.StockValue = StockValue

class StockDemo: #This class and below constructor was not mentioned in question but wihtout this constructor and class we get error
    def __init__(self):
        self.a=10

    def getStockList(self,list_Stock,StockSectorString):#If we will not create a constructor ,we will get error for StockSectorString
        result=[]
        for i in list_Stock:
            if i.StockSector==StockSectorString:
                if i.StockValue>500:
                    result.append(i.StockName)
        return result

if __name__ == '__main__':
    n=int(input())
    list_obj=[]
    for i in range(n):
        StockName=input()
        StockSector=input()
        StockValue=int(input())
        o=Stock(StockName,StockSector,StockValue)
        list_obj.append(o)
        # list_obj.append(Stock(StockName,StockSector,StockValue))
    StockSectorString=input()
    obj=StockDemo()
    answer1=obj.getStockList(list_obj,StockSectorString)
    for j in answer1:
        print(j)



