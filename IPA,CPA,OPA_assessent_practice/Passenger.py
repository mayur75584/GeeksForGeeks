'''
Given passenger ID name gender distance
In last two lines they provide the passenger ID and discount percentage
We need to print the discount to be given for that particular passenger
if that given Id is not in the list print no name or no value

​

input :

​

4
101
a
f
10000
102
b
m
12000
103
c
f
45000
104
d
m
65000
101
5



output:


discount of 101 is: 500.0

​

Solution 1(without class):

​

n=int(input())
k=[]
for i in range(n):
    l=[]
    l.append(input())
    l.append(input())
    l.append(input())
    l.append(int(input()))
    k.append(l)
key=input()
dis=int(input())
z=[]
for ind in range(n):
    if(key==k[ind][0]):
        z.append(ind)
if(len(z)==0):
    print("no id found")
else:
    i=z[0]
    disc=k[i][3]*dis/100
    if(disc>0):
        print('discount of',k[i][0],'is:',disc)
    else:
        print(k[i][0],'is not eligible for discount')



Solution 2(with class):


class Passenger:
    def __init__(self,pid,pname,pgender,pmiles):
        self.pid=pid
        self.pname=pname
        self.pgender=pgender
        self.pmiles=pmiles
    def calculate_discount(self,pid,discount_rate):
        for i in pass_list:
            if i.pid==pid:
                discount=(i.pmiles*discount_rate)/100
                return discount
class Organisation(Passenger):
    def __init__(self,oname,pass_list):
        self.oname=oname
        self.pass_list=pass_list
if __name__ == '__main__':
    n=int(input())
    pass_list=[]
    for i in range(n):
        pid=input()
        pname=input()
        pgender=input()
        pmiles=int(input())
        pass_list.append(Passenger(pid,pname,pgender,pmiles))
    pid=input()
    discount_rate=int(input())
    o=Organisation('TCS',pass_list)
    discount=o.calculate_discount(pid,discount_rate)
    if discount<0:
        print("Passenger not eligible for discount")
    else:
        print("The discount of passenger "+pid+" is " +str(discount))
'''

class Passenger:

    def __init__(self,pass_id,pass_name,pass_gender,distance):
        self.pass_id = pass_id
        self.pass_name = pass_name
        self.pass_gender = pass_gender
        self.distance = distance

    def calculate_discount(self,pId,dis_per):
        result=0
        for i in list_obj:
            if i.pass_id==pId:
                result=i.distance*(dis_per/100)
        return result

class Organistaion(Passenger):

    def __init__(self,oname,pass_list):
        self.oname = oname
        self.pass_list = pass_list




if __name__ == '__main__':
    n=int(input())
    list_obj= []
    for i in range(n):
        pass_id = int(input())
        pass_name = input()
        pass_gender = input()
        distance = int(input())
        p=Passenger(pass_id,pass_name,pass_gender,distance)
        list_obj.append(p)
    pId = int(input())
    dis_per = int(input())
    o=Organistaion("ABC",list_obj)
    answer=o.calculate_discount(pId,dis_per)
    if answer==0:
        print("Passenger Not Found")
    else:
        print(answer)




