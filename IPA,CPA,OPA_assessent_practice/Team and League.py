
'''


Input -
5
DC
395
21
Pant
RCB
184
5
Virat
MI
132
75
Rohit
CSK
904
87
Dhoni
PK
849
74
Rahul

Output-
RCB
184.0
5
Virat
5
21
74
75
87
'''

class Team:

    def __init__(self,owner,value,id,name):
        self.owner = owner
        self.value = value
        self.id = id
        self.name = name
class League:

    def __init__(self,leagueName,teamList):
        self.leagueName = leagueName
        self.teamList = teamList

    def findMinimumTeamById(self):
        if len(self.teamList)<=0:
            return None
        else:
            sortedList=sorted(self.teamList,key= lambda x:x.id) #Important logic to sort all teams values in one list on basis of id
            return sortedList[0]
    def sortTeamById(self):
        if len(self.teamList)<=0:
            return None
        else:
            sortedList=sorted(self.teamList,key=lambda x:x.id)
            return sortedList



if __name__ == '__main__':
    n=int(input())
    list_obj = []
    for i in range(n):
        owner=input()
        value=int(input())
        id=int(input())
        name=input()
        t=Team(owner,value,id,name)
        list_obj.append(t)
    l=League("ipl",list_obj)
    answer1=l.findMinimumTeamById()
    answer2=l.sortTeamById()
    if answer1==None:
        print("No data found")
    else:
        print(answer1.owner,"%.1f"%answer1.value,answer1.id,answer1.name,sep="\n")
    if answer2==None:
        print("No data found")
    else:
        for i in answer2:
            print(i.id)




