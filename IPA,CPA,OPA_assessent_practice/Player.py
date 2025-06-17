
'''

Create a class Player with below attributes

playerName:(string type)
String playerCountry:(string type)
playerAge:(int type)
noOfMatches:(int type)
onOfRuns:(int type)
noOfWickets:(int type)

Create a constructor which takes all the above attribute in the same sequence

Define another class Team with the below member function

getMinRuns: Which takes list of Player objects as input parameter
and returns the player details who scored Minimum runs(Assume that no player has same number of runs scored).

getMaxWickets: Which takes list of Player objects as input parameter and returns the player,
who took the Maximum wickets(Assume that no player has same number of wickets).

Input -
5
Sachin
India
40
350
15000
120
Klusnar
SouthAfrica
37
270
3000
250
Dhoni
India
38
345
12000
0
RickyPointing
Australia
42
290
11000
3
Dravid
India
39
320
11200
12

Output-
Klusnar
3000
SouthAfrica
Klusnar
250
SouthAfrica
'''
class Player:

    def __init__(self,playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets):
        self.playerName = playerName
        self.playerCountry = playerCountry
        self.playerAge = playerAge
        self.noOfMatches = noOfMatches
        self.noOfRuns = noOfRuns
        self.noOfWickets = noOfWickets

class Team:

    def __init__(self,list_obj):
        self.list_obj = list_obj

    def getMinRuns(self):
        min1=[]
        result=[]
        for i in self.list_obj:
            min1.append(i.noOfRuns)
        z=min(min1)
        for i in self.list_obj:
            if z==i.noOfRuns:
                result.append(i.playerName)
                result.append(i.noOfRuns)
                result.append(i.playerCountry)
        if len(result)==0:
            return None
        else:
            return result


    def getMaxWickets(self):
        max1=[]
        result=[]
        for i in self.list_obj:
            max1.append(i.noOfWickets)
        z=max(max1)
        for i in self.list_obj:
            if z==i.noOfWickets:
                result.append(i.playerName)
                result.append(i.noOfWickets)
                result.append(i.playerCountry)
        if len(result)==0:
            return None
        else:
            return result


if __name__ == '__main__':
    n=int(input())
    list_obj = []
    for i in range(n):
        playerName = input()
        playerCountry = input()
        playerAge = int(input())
        noOfMatches = int(input())
        noOfRuns = int(input())
        noOfWickets = int(input())
        p=Player(playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets)
        list_obj.append(p)
    t=Team(list_obj)
    answer1=t.getMinRuns()
    answer2=t.getMaxWickets()
    if answer1==None:
        print("No Player Found")
    else:
        for i in answer1:
            print(i)
    if answer2==None:
        print("No Player Found")
    else:
        for i in answer2:
            print(i)







