'''
Create a class 'CricketPlayer' with below attributes
cplayerName: string type
cplayedCountry: set of strings
cplayerAge: int type
cpCountryFrom: string type

Create a constructor which takes all the above values in same sequence.

Create a class 'Soluton' with attributes as set of players obtained from
main function

Define two functions inside 'Soluton' class.

countPlayers: It takes a string represent 'country name' as argument and returns the
total count of players belonging to that country.

getPlayedForMaxCountry: It finds the name of player from players
list of Soluton class who has played against highest number of countries.

Input -
3
virat
5
aus
nze
eng
wi
pak
35
ind
raina
3
aus
pak
nze
34
ind
gayle
3
aus
ind
pak
42
wi
ind

Output-
2
virat

Input -
3
dhoni
5
wi
srilanka
pak
nze
aus
39
ind
virat
2
srilanka
aus
32
ind
gayle
3
ind
pak
aus
42
wi
wi

Output-
1
dhoni
'''
class CricketPlayer:

    def __init__(self,cplayerName,cplayedCountry,cplayerAge,cpCountryFrom):
        self.cplayerName = cplayerName
        self.cplayedCountry = cplayedCountry
        self.cplayerAge = cplayerAge
        self.cpCountryFrom = cpCountryFrom

class Solution:

    def __init__(self,list_obj):
        self.list_obj = list_obj

    def countPlayers(self,country_name):
        counter=0
        for i in self.list_obj:
            if i.cpCountryFrom.lower() == country_name.lower():
                counter+=1
        return counter

    def getPlayedForMaxCountry(self):
        # max1=-1
        # name=''
        # for i in self.list_obj:
        #     if len(i.cplayedCountry)>=max1:
        #         max1=len(i.cplayedCountry)
        #         name=i.cplayerName
        # return name
        dict={}
        for i in self.list_obj:
            dict[i.cplayerName] = len(i.cplayedCountry)
        print(dict)
        lst=[]
        max1=max(dict.values())
        for k in dict:
            if dict[k]==max1:
                lst.append(k)
        return lst




if __name__ == '__main__':
    n=int(input())
    list_obj=[]
    for i in range(n):
        cplayerName = input()
        c=int(input())
        lst=[]
        for j in range(c):
            p=input()
            lst.append(p)
        cplayedCountry=set(lst)
        cplayerAge = int(input())
        cpCountryFrom = input()
        c1=CricketPlayer(cplayerName,cplayedCountry,cplayerAge,cpCountryFrom)
        list_obj.append(c1)
    s=Solution(list_obj)
    country_name=input()
    answer1=s.countPlayers(country_name)
    answer2=s.getPlayedForMaxCountry()
    print(answer1)
    if len(answer2)==0:
        print("No players found")
    else:
        for j in answer2:
            print(j)



