'''
Link to the question->
Question number 10 of this link

https://xploredimension.wordpress.com/2020/09/24/tcs-ira-opa-python/
'''
'''
Not complete question was available

University Management

Create a class Professor with the below attributes.

profId of integer type
profName of string type
subjectsDict of dictionary of subjects{subject is the key : years of experience as value}

where , profid represents professor id,profName represnets professor name
and subjectsDict represents the dictionary with subject Name, Number of years of experience as Key:Value pair.

Create another class with University name and create two methods in that

getTotalExperience method:
This method takes two input parametrs - the list of professor objects and a number
value which represents the profession id. It returns the total experience of that professor whose id 
matches with the given professor ID.
Total experience is to be calculated as the sum of experience of all the subjects of the
respective professor. The experience   of each subject can be accesssed from the dictionary
belonging to the professor object.
If no professor is available with the given id, the return 0

selectSeniorProfessorBySubject method:
This method takes two parametrs: the list of professor objects and a
string  representing the subject name. The method returns the professor
who has the highest experience in that subject(Assume no professor have
same years of experience in a given subject).

If there is no professor available for a given subject then return None.

All string searches are to be case insensitive.


input:

4

1
Shivakumar
3
Maths
10
Physics
10
Chemistry
10
2
Rajesh
4
MATHS
5
PHYSICS
5
CHEMISTRY
5
COMPUTERS
5
3
Vasudev
2
MATHS
4
PHYSICS
4
4
Srinivas
3
Maths
8
Physics
8
Chemistry
8
3
maths

Output:

8

1 Shivakumar {‘MATHS’: 10, ‘PHYSICS’: 10, ‘CHEMISTRY’: 10}

Test case 2:
2
1
Mayur
3
CSE
10
IT
15
Mech
20
2
Manasi
2
CSE
20
IT
15
1
CSE

Output-
45
2 Manasi {'CSE': 20, 'IT': 15}

​Solutions:

​class Professor():
    def __init__(self,profId, profName, subjectsDict):
        self.profId = profId
        self.profName = profName
        self.subjectsDict = subjectsDict
class University():
    def __init__(self, test):
        self.test = “tesint”
    def getTotalExperience(self,profList, profId):
        result = 0
        for item in profList:
            proFId=int(profId)
            if item.profId == proFId:
                for exp in item.subjectsDict.values():
                    result+=exp
        return result
    def selectSeniorProfessorBySubject(self,profList, subjectName):
        result= -9
        found = False
        obj=None
        for item in profList:
            if item.subjectsDict[subjectName.upper()]>= result:
                result = item.subjectsDict[subjectName.upper()]
                found = True
                obj = item
        if found == False:
            return ‘None’
        else:
            return str(obj.profId)+” “+ obj.profName+” “+str(obj.subjectsDict)
if __name__ == “__main__”:


    T = int(input().strip())

    profObjects=[]
    while T>0:
        profId = int(input())
        profName = input().strip()
        numSubjects = int(input().strip())
        subjectDict={}
        while numSubjects>0:
            subjectName = input().strip()
            exp = int(input().strip())
            subjectDict[subjectName.upper()] = exp
            numSubjects-=1
        obj = Professor(profId,profName,subjectDict)
        profObjects.append(obj)
        T-=1
    profSearch = input().strip()
    subjectSearch = input().strip()
    obj = University(“tset”)
    print(obj.getTotalExperience(profObjects,profSearch))
    print(obj.selectSeniorProfessorBySubject(profObjects, subjectSearch))
'''





class Professor:

    def __init__(self,profId,profName,subjectsDict):
        self.profId = profId
        self.profName = profName
        self.subjectsDict = subjectsDict

class University:
    def __init__(self,teset):
        self.teset = "teset"

    def TotalExperience(self,list_obj,res_profId):
        counter=0
        for i in list_obj:
            if i.profId == res_profId:
                for values in i.subjectsDict.values():
                    counter+=values
        return counter



    def selectSeniorProfessorBySubject(self,list_obj,subject_name):
        max1=-4
        name=''
        found=False
        for i in list_obj:
            for keys,values in i.subjectsDict.items():
                if subject_name.upper()==keys.upper():
                    if values>max1:
                        max1=values
                        name=i.profName
                        found=True
        if found==True:
            return name
        else:
            return "None"


        # for i in list_obj:
        #     if i.subjectsDict[subject_name.upper()]>=max1:
        #         max1=i.subjectsDict[subject_name.upper()]
        #         found=True
        #         name=i.profName
        # if found==True:
        #     return name
        # else:
        #     return "None"










if __name__ == '__main__':
    n=int(input())

    list_obj=[]
    for i in range(n):
        profId=int(input())
        profName=input()
        subjectsDict={}
        c=int(input())
        for j in range(c):
            keys=input().upper()
            values=int(input())
            subjectsDict[keys]=values
        p=Professor(profId,profName,subjectsDict)
        list_obj.append(p)
    res_profId=int(input())
    subject_name=input()
    obj=University("teset")
    answer1=obj.TotalExperience(list_obj,res_profId)
    answer2=obj.selectSeniorProfessorBySubject(list_obj,subject_name)

    if answer1==0:
        print(0)
    else:
        print(answer1)

    if answer2=="None":
        print("None")
    else:
        for i in list_obj:
            if i.profName==answer2:
                print(i.profId,i.profName,i.subjectsDict)

'Practice'

# class Professor:
#     def __init__(self,profId,profName,subjectsDict):
#         self.profId = profId
#         self.profName = profName
#         self.subjectsDict = subjectsDict
#
# class University:
#     def __init__(self,test):
#         self.test='tesint'
#
#     def getTotalExperience(self,lst_obj,prof_id):
#         res=0
#         for i in lst_obj:
#             if i.profId==prof_id:
#                 for j,k in i.subjectsDict.items():
#                     res+=k
#         if res==0:
#             return 0
#         else:
#             return res
#
#
#     def selectSeniorProfessorBySubject(self,lst_obj,sub_name):
#         max1=0
#         name=''
#         flag=False
#         for i in lst_obj:
#             for j,k in i.subjectsDict.items():
#                 if j.lower()==sub_name.lower():
#                     if max1<k:
#                         max1=k
#                         name=i.profName
#                         flag=True
#         if flag==True:
#             return name
#         else:
#             return None
#
# n=int(input())
# lst_obj=[]
# for i in range(n):
#     profId=int(input())
#     profName=input()
#     c=int(input())
#     subjectDict={}
#     for j in range(c):
#         subject=input()
#         experience=int(input())
#         subjectDict[subject]=experience
#     p=Professor(profId,profName,subjectDict)
#     lst_obj.append(p)
#
# prof_id=int(input())
# sub_name=input()
# u=University("tesint")
# ans1=u.getTotalExperience(lst_obj,prof_id)
# ans2=u.selectSeniorProfessorBySubject(lst_obj,sub_name)
# if ans1==0:
#     print(0)
# else:
#     print(ans1)
# if ans2==None:
#     print("None")
# else:
#     for i in lst_obj:
#         if i.profName==ans2:
#             print(i.profId,i.profName,i.subjectsDict)


