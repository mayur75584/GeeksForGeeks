'''

Screenshots are taken in mobile

Input -
4
101
coll1
AHD
3.5
102
coll2
BLR
4.4
103
coll3
KOL
5.0
104
coll4
TVM
3.7
BLR

Output -
102
coll2
BLR
4.4
101
104
102
103

Input2-
4
101
coll1
AHD
3.0
102
coll2
BLR
3.4
103
coll3
KOL
4.0
104
coll4
TVM
3.9
LKO

Output2-
No data found
101
102
104
103
'''

# class College:
#
#     def __init__(self,collegeID,Name,City,Rating):
#         self.collegeID = collegeID
#         self.Name = Name
#         self.City = City
#         self.Rating = Rating
#
# class University:
#
#     def __init__(self,universityName,collegeCollection):
#         self.universityName = universityName
#         self.collegeCollection = collegeCollection
#
#     def findCollegeByCity(self,s_city):
#         result=[]
#         for i in self.collegeCollection:
#             if i.City.lower()==s_city.lower():
#                 result.append(i.collegeID)
#                 result.append(i.Name)
#                 result.append(i.City)
#                 result.append(i.Rating)
#         if len(result)==0:
#             return None
#         else:
#             return result
#
#
#     def sortCollegeByRating(self):
#         # result=[]
#         # for i in self.collegeCollection:
#         #     result.append(i.Rating)
#         # if len(result)==0:
#         #     return None
#         # else:
#         #     return sorted(result)
#         'or'
#         sorted1=[]
#         sorted2=[]
#         if len(self.collegeCollection)<=0:
#             return None
#         else:
#             sorted1=sorted(self.collegeCollection, key=lambda x:x.Rating)
#             for i in sorted1:
#                 sorted2.append(i.collegeID)
#             return sorted2
#
# if __name__ == '__main__':
#     n=int(input())
#     list_obj=[]
#     for i in range(n):
#         collegeID = int(input())
#         Name = input()
#         City = input()
#         Rating = float(input())
#         c=College(collegeID,Name,City,Rating)
#         list_obj.append(c)
#     s_city=input()
#     u=University("ABC",list_obj)
#     answer1=u.findCollegeByCity(s_city)
#     answer2=u.sortCollegeByRating()
#
#     if answer1==None:
#         print("No data found")
#     else:
#         for i in answer1:
#             print(i)
#
#     if answer2==None:
#         print("No data found")
#     else:
#         for i in answer2:
#             print(i)

'Practice'



class College:
    def __init__(self,collegeID,Name,City,Rating):
        self.collegeId = collegeID
        self.Name = Name
        self.City = City
        self.Rating = Rating

class University:
    def __init__(self,universityName,collegeCollection):
        self.universityName = universityName
        self.collegeCollection = collegeCollection

    def findCollegeByCity(self,city1):
        res=[]
        for i in self.collegeCollection:
            if i.City.lower()==city1.lower():
                res.append(i.collegeId)
                res.append(i.Name)
                res.append(i.City)
                res.append(i.Rating)
                return res
        else:
            return None

    def sortCollegeByRating(self):
        res=[]
        #Below is one of the logic to directly sort the list of objects
        #on basis from one of its attribute
        #As here we have sort list of objects from its Rating attribute
        z=sorted(self.collegeCollection,key=lambda x:x.Rating)
        for i in z:
            res.append(i.collegeId)
        if len(res)==0:
            return None
        else:
            return res

n=int(input())
lst_obj=[]
for i in range(n):
    collegeId = int(input())
    Name = input()
    City = input()
    Rating = float(input())
    c=College(collegeId,Name,City,Rating)
    lst_obj.append(c)
u=University("XYZ",lst_obj)
city1=input()
ans1=u.findCollegeByCity(city1)
ans2=u.sortCollegeByRating()
if ans1==None:
    print("No data found")
else:
    for i in ans1:
        print(i)

if ans2==None:
    print("No data found")
else:
    for i in ans2:
        print(i)

