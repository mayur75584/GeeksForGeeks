# import string
#
# a=list(string.ascii_lowercase)
# for i in a:
#     print(a)


# 19 Nov 2021 IPA
#
# class Employee:
#
#     def __init__(self,employee_name,designation,salary,overTimeContribution,overTimeStatus="False"):
#         self.employee_name = employee_name
#         self.designation = designation
#         self.salary = salary
#         self.overTimeContribution = overTimeContribution
#         self.overTimeStatus = overTimeStatus
# class Organisation:
#
#     def __init__(self,employee_list):
#         self.employee_list = employee_list
#
#     def overTimeStatus(self,overTimeThreshold):
#         for i in self.employee_list:
#             z=i.overTimeContribution.values()
#             sum1=int(sum(z))
#             if sum1>=overTimeThreshold:
#                 i.overTimeStatus = "True"
#         return self.employee_list
#     def totalbonus(self,ratePerHour):
#         sum1=0
#         for i in self.employee_list:
#             if i.overTimeStatus=="True":
#                 sum1+=int(sum(i.overTimeContribution.values()))
#         return sum1*ratePerHour
#
#
# if __name__ == '__main__':
#     n=int(input())
#     list_obj=[]
#     for i in range(n):
#         employee_name = input()
#         designation = input()
#         salary = int(input())
#         overTimeContribution = {}
#         c=int(input())
#         for j in range(c):
#             key=input()
#             value=int(input())
#             overTimeContribution[key]=value
#         e=Employee(employee_name,designation,salary,overTimeContribution)
#         list_obj.append(e)
#     overTimeThreshold = int(input())
#     ratePerHour = int(input())
#     o=Organisation(list_obj)
#     answer1=o.overTimeStatus(overTimeThreshold)
#     answer2=o.totalbonus(ratePerHour)
#     for i in answer1:
#         print(i.employee_name,i.overTimeStatus)
#     print(answer2)

#Account

# class Apartment:
#
#     def __init__(self,flat_number,ownerName,electricityBillAmount):
#         self.flat_number = flat_number
#         self.ownerName = ownerName
#         self.electricityBillAmount = electricityBillAmount
#
# class Apartment_Demo:
#
#     def __init__(self):
#         pass
#     def getSecondMinBill(self,list_obj):
#         z=[]
#         for i in list_obj:
#             z.append(i.electricityBillAmount)
#         z1=sorted(z)
#         return z1[1]
#
#
# if __name__ == '__main__':
#     n=int(input())
#     list_obj = []
#     for i in range(n):
#         flat_number = int(input())
#         ownerName = input()
#         electricityBillAmount = int(input())
#         a=Apartment(flat_number,ownerName,electricityBillAmount)
#         list_obj.append(a)
#     a=Apartment_Demo()
#     answer1=a.getSecondMinBill(list_obj)
#     print(answer1)

#Bill

# class Bill:
#
#     def __init__(self,mobile_number,payment_bill):
#         self.mobile_number = mobile_number
#         self.payment_bill = payment_bill
#
#
# class Mobile:
#
#     def __init__(self,serviceProvider,mobileNumber,dataUsed,payment_method):
#         self.serviceProvider = serviceProvider
#         self.mobileNumber = mobileNumber
#         self.dataUsed = dataUsed
#         self.payment_method = payment_method
#
#     def calculatebill(self,list_obj):
#         result=[]
#         for i in list_obj:
#             res=[]
#             bill=0
#             if i.serviceProvider.lower()=='airtel':
#                 if i.payment_method.lower()=='paytm':
#                     bill=i.dataUsed*11
#                     bill1=(bill*(10/100))
#                     z=round(bill-bill1)
#                     res.append(i.mobileNumber)
#                     res.append(z)
#                     result.append(res)
#
#                 else:
#                     bill=round(i.dataUsed*11)
#                     res.append(i.mobileNumber)
#                     res.append(bill)
#                     result.append(res)
#             elif i.serviceProvider.lower()=='jio':
#                 bill=round(i.dataUsed*10)
#                 res.append(i.mobileNumber)
#                 res.append(bill)
#                 result.append(res)
#         return result







# if __name__ == '__main__':
#     n=int(input())
#     list_obj = []
#     for i in range(n):
#         serviceProvider = input()
#         mobileNumber = int(input())
#         dataUsed = int(input())
#         payment_method = input()
#         list_obj.append(Mobile(serviceProvider,mobileNumber,dataUsed,payment_method))
#     m=Mobile("",0,0,"")
#     answer=m.calculatebill(list_obj)
#     for i in answer:
#         print("("+str(i[0])+","+str(i[1])+")")

#Book

# class Book:
#
#     def __init__(self,book_id,book_name):
#         self.book_id = book_id
#         self.book_name = book_name
#
# class Library:
#
#     def __init__(self,library_id,address,book_list):
#         self.library_id = library_id
#         self.address = address
#         self.book_list = book_list
#
#     def count_books(self,char):
#         counter=0
#         for i in self.book_list:
#             if i.book_name[0]==char:
#                 counter+=1
#         return counter
#
#
#     def remove_books(self,names):
#         for i in names:
#             for j in self.book_list:
#                 if i==j.book_name:
#                     self.book_list.remove(j)
#         return self.book_list
# if __name__ == '__main__':
#     n=int(input())
#     list_obj = []
#     for i in range(n):
#         book_id = int(input())
#         book_name = input()
#         list_obj.append(Book(book_id,book_name))
#     char=input()
#     c=int(input())
#     names=[]
#     for i in range(c):
#         names.append(input())
#     l=Library(123,"XYZ",list_obj)
#     answer1=l.count_books(char)
#     answer2=l.remove_books(names)
#     print(answer1,end=' ')
#     for i in answer2:
#         print(i.book_name,end=' ')

# count_words
#
# def count_words(input_string):
#     dict={}
#     words=input_string.split()
#     for i in words:
#         dict[i]=words.count(i)
#     return dict
#
# def max_occurence_word(input_string):
#     d=count_words(input_string)
#     v=list(d.values())
#     k=list(d.keys())
#     return k[v.index(max(v))]
#
#
# if __name__ == '__main__':
#     input_string = input()
#     dict=count_words(input_string)
#     print(dict)
#     st=max_occurence_word(input_string)
#     print(st)

#Doctor

# class Doctor:
#
#     def __init__(self,doctorId,doctorName,specialization,consultationFee):
#         self.doctorId = doctorId
#         self.doctorName = doctorName
#         self.specialization = specialization
#         self.consultationFee = consultationFee
#
# class Hospital:
#
#     def __init__(self,doctorDB):
#         self.doctorDB = doctorDB
#
#     def searchByDoctorName(self,name):
#         result=[]
#         for i in doctorDB.keys():
#             if doctorDB[i].doctorName==name:
#                 result.append(doctorDB[i])
#         if len(result)==0:
#             return None
#         else:
#             return result
#
#     def calculateConsultationFeeBySpecialization(self,ans_specialization):
#         result=0
#         for i in self.doctorDB.keys():
#             if self.doctorDB[i].specialization==ans_specialization:
#                 result+=self.doctorDB[i].consultationFee
#         if result==0:
#             return 0
#         else:
#             return result
#
# if __name__ == '__main__':
#     n=int(input())
#     list_obj=[]
#     for i in range(n):
#         doctorId=int(input())
#         doctorName=input()
#         specialization=input()
#         consultationFee=int(input())
#         list_obj.append(Doctor(doctorId,doctorName,specialization,consultationFee))
#     doctorDB={}
#     c=1
#     for i in range(len(list_obj)):
#         doctorDB[c]=list_obj[i]
#         c+=1
#
#     name=input()
#     ans_specialization=input()
#     h=Hospital(doctorDB)
#     answer1=h.searchByDoctorName(name)
#     if answer1==None:
#         print("No Doctor Exists with the given DoctorName")
#     else:
#         for i in answer1:
#             print(i.doctorId)
#             print(i.doctorName)
#             print(i.specialization)
#             print(i.consultationFee)
#     answer2=h.calculateConsultationFeeBySpecialization(ans_specialization)
#     if answer2==0:
#         print("No doctor with the given specialization")
#     else:
#         print(answer2)

# Employee2

# class Employee:
#
#     def __init__(self,empno,empname,leaves):
#         self.empno = empno
#         self.empname = empname
#         self.leaves = leaves
#
# class Company:
#
#     def __init__(self,cname,emps):
#         self.cname = cname
#         self.emps = emps
#
#     def display_leave(self,emp_number,leave_type):
#         for i in self.emps:
#             if i.empno == emp_number:
#                 return i.leaves[leave_type]
#
#     def leave_application(self,emp_number,leave_type,noOfLeaves):
#         for i in self.emps:
#             if i.empno == emp_number:
#
#
#
# if __name__ == '__main__':
#     n=int(input())
#     list_obj = []
#     for i in range(n):
#         empno = int(input())
#         empname = input()
#         leaves={}
#         leaves["CL"]=int(input())
#         leaves["EL"]=int(input())
#         leaves["SL"]=int(input())
#         list_obj.append(Employee(empno,empname,leaves))
#     emp_number=int(input())
#     leave_type=input()
#     noOfLeaves=int(input())
#     c=Company("TCS",list_obj)
#     answer1=c.display_leave(emp_number,leave_type)
#     print(answer1)
#     answer2=c.leave_application(emp_number,leave_type,noOfLeaves)
#     print(answer2)

#Online Vegetable Store
#Practice for this once more without looking at solution
'''
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
'''
# import string
# class Vegetables:
#
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
# class Store:
#
#     def __init__(self,storeName,vegList):
#         self.storeName = storeName
#         self.vegList = vegList
#
#     def categorizeVegetablesAlphabetically(self):
#         self.vegList.sort(key=lambda x:x.name)
#         a=list(string.ascii_lowercase)
#
#         dict={}
#
#         for i in a:
#             res=[]
#             for j in self.vegList:
#                 if i==j.name[0]:
#                     res.append(j.name)
#             if len(res)>0:
#                 dict[i]=tuple(res)
#         return dict
#
#     def filterVegetablesForPriceRange(self,min_price,max_price):
#         res=[]
#         for i in self.vegList:
#             if min_price<=i.price<=max_price:
#                 res.append(i.name)
#         return sorted(res)
#
#
#
#
# if __name__ == '__main__':
#     n=int(input())
#     list_obj=[]
#     for i in range(n):
#         name = input()
#         price = float(input())
#         quantity = int(input())
#         list_obj.append(Vegetables(name,price,quantity))
#     storeName = input()
#     min_price=float(input())
#     max_price=float(input())
#     s=Store(storeName,list_obj)
#     answer1=s.categorizeVegetablesAlphabetically()
#     answer2=s.filterVegetablesForPriceRange(min_price,max_price)
#     for key,value in answer1.items():
#         print(key)
#         if len(value)>1:
#             z=list(value)
#             for j in z:
#                 print(j)
#         else:
#             z=list(value)
#             print(z[0])
#     print(str(min_price)+'-'+str(max_price))
#     for i in answer2:
#         print(i)

# Painting #Practice once this question also
#
# class Painting:
#
#     def __init__(self,paintingID,painterName,paintingPrice,painting_type):
#         self.paintingID = paintingID
#         self.painterName = painterName
#         self.paintingPrice = paintingPrice
#         self.painting_type = painting_type
#
# class ShowRoom:
#
#     def __init__(self,paintingList):
#         self.paintingList = paintingList
#
#     def getTotalPaintingPrice(self,paintingType):
#         sum1=0
#         for i in self.paintingList:
#             if i.painting_type.lower()==paintingType.lower():
#                 sum1+=i.paintingPrice
#         if sum1==0:
#             return None
#         else:
#             return sum1
#     def getPainterWithMaxCountOfPaintings(self):
#         # z=sorted(self.paintingList,key=lambda x:x.painterName.lower())
#         # name=''
#         # max1=0
#         # for i in z:
#         #     if i.paintingPrice>max1:
#         #         max1=i.paintingPrice
#         #         name=i.painterName
#         # return name.lower()
#         # Above logic is not correct
#         dict={}
#         for i in self.paintingList:
#             if i.painterName in dict:
#                 dict[i.painterName]+=1
#             else:
#                 dict[i.painterName]=1
#         sort1=sorted(dict.items(),key=lambda x:x[1])
#         result=[]
#         val=sort1[-1][-1]
#         for i in sort1:
#             if val==i[1]:
#                 result.append(i[0])
#         if len(result)>1:
#             result.sort()
#             return result[0]
#         else:
#             return sort1[-1][0]
#
#
#
#
# if __name__ == '__main__':
#     n=int(input())
#     list_obj = []
#     for i in range(n):
#         paintingID = input()
#         painterName = input()
#         paintingPrice = int(input())
#         painting_type = input()
#         list_obj.append(Painting(paintingID,painterName,paintingPrice,painting_type))
#     paintingType=input()
#     s=ShowRoom(list_obj)
#     answer1=s.getTotalPaintingPrice(paintingType)
#     answer2=s.getPainterWithMaxCountOfPaintings()
#     print(answer1)
#     # for i in answer2:
#     #     print(i.painterName)
#     print(answer2)




#Parked Vehicles
# class ParkedVehicle:
#
#     def __init__(self,vehicleSeq,fourWheeler,parkedFor,valetParking):
#         self.vehicleSeq = vehicleSeq
#         self.fourWheeler = fourWheeler
#         self.parkedFor = parkedFor
#         self.valetParking = valetParking
#         self.parkedStatus = "Parked"
#
# class ParkingLot:
#
#     def __init__(self,parked_vehicles):
#         self.parked_vehicles = parked_vehicles
#
#     def updateParkedStatus(self,lot_Number):
#         if lot_Number in self.parked_vehicles.keys():
#             self.parked_vehicles[lot_Number].parkedStatus="Cleared"
#             tup=(lot_Number,"Cleared")
#             return tup
#         else:
#             return None
#     def getParkingCharges(self,lot_Number):
#         if lot_Number in self.parked_vehicles.keys():
#             if self.parked_vehicles[lot_Number].fourWheeler=="Yes":
#                 total=50*self.parked_vehicles[lot_Number].parkedFor
#                 if self.parked_vehicles[lot_Number].valetParking=="Yes":
#                     total+=10.0
#                 return total
#             else:
#                 total=30*self.parked_vehicles[lot_Number].parkedFor
#                 if self.parked_vehicles[lot_Number].valetParking=="Yes":
#                     total+=10.0
#                 return total
#         else:
#             return None
#
#
#
#
#
#
# if __name__ == '__main__':
#     n=int(input())
#     list_obj = []
#     parked_vehicles={}
#     for i in range(n):
#         vehicleSeq = int(input())
#         fourWheeler = input()
#         parkedFor = float(input())
#         valetParking = input()
#         lotNumber = int(input())
#         list_obj.append(ParkedVehicle(vehicleSeq,fourWheeler,parkedFor,valetParking))
#         parked_vehicles[lotNumber]=ParkedVehicle(vehicleSeq,fourWheeler,parkedFor,valetParking)
#     p=ParkingLot(parked_vehicles)
#     lot_Number = int(input())
#     answer1=p.updateParkedStatus(lot_Number)
#     answer2=p.getParkingCharges(lot_Number)
#     if answer1==None:
#         print("Lot Number Invalid")
#     else:
#         print(answer1[0],answer1[1])
#     if answer2==None:
#         print("Lot Number Invalid")
#     else:
#         print(answer2)

#Student and School

# class Student:
#
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
#
#     def calculateResult(self):
#         average=0
#         if self.sub1>40 and self.sub2>40 and self.sub3>40:
#             average=(self.sub1+self.sub2+self.sub3)/3
#         return average
#
# class School:
#
#     def __init__(self,name1,studentDict):
#         self.name1 = name1
#         self.studentDict = studentDict
#
#     def getStudentResult(self):
#         res=[]
#         for i in self.studentDict:
#             if i.calculateResult()>60:
#                 self.studentDict[i]="Pass"
#                 res.append(i.name)
#         if len(res)==0:
#             return 0
#         else:
#             return res
#
#     def findStudentWithHighestMarks(self):
#         max1=0
#         topper=''
#         for i in self.studentDict:
#             if self.studentDict[i]=="Pass":
#                 z=i.calculateResult()
#                 if max1<z:
#                     max1=z
#                     topper=i.name
#         return topper
#
#
# if __name__ == '__main__':
#     n=int(input())
#     list_obj = []
#     studentDict={}
#     for i in range(n):
#         name = input()
#         sub1 = float(input())
#         sub2 = float(input())
#         sub3 = float(input())
#         list_obj.append(Student(name,sub1,sub2,sub3))
#         studentDict[Student(name,sub1,sub2,sub3)]="Fail"
#     name1=input()
#     s=School(name1,studentDict)
#     answer1=s.getStudentResult()
#     if answer1==0:
#         print("No Student Pass")
#     else:
#         for i in answer1:
#             print(i)
#     answer2=s.findStudentWithHighestMarks()
#     print(answer2)
#
















