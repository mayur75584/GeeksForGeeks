
'''

Question number 8 of IPA sample questions pdf

Sample Input1-
3
1
Bread
30
5
2
Milk
50
10
3
Cookies
100
2

3
Bread
2
Butter
1
Milk
2

Sample Output-
60
160
'''
class Item:

    def __init__(self,item_id,item_name,item_price,quantity_available):

        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price
        self.quantity_available = quantity_available

    def calculate_price(self,quantity):
        Total_price=0
        if self.quantity_available>=quantity:
            self.quantity_available-=quantity
            Total_price=self.item_price*quantity
            return Total_price
        else:
            return 0




class Store:

    def __init__(self,item_list):
        self.item_list = item_list

    def generate_bill(self,dict):
        bill=0
        for i in dict:
            for j in self.item_list:
                if i==j.item_name:
                    bill+=j.calculate_price(dict[i])
        return bill





n=int(input())
list_obj=[]
for i in range(n):
    item_id = int(input())
    item_name = input()
    item_price = int(input())
    quantity_available = int(input())

    list_obj.append(Item(item_id,item_name,item_price,quantity_available))

s=Store(list_obj)
dict={}
ccount=int(input())
for j in range(ccount):
    name=input()
    quantity = int(input())
    dict[name]=quantity
answer1=list_obj[0].calculate_price(2)
answer2=s.generate_bill(dict)
print(answer1)
print(answer2)



