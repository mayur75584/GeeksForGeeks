'''
Sample Input1-
5
Sachin
4
Japan
Brazil
China
Nepal
40
India
Kamini
4
Denmark
Australia
Indonesia
Ghana
37
Nepal
Saurav
6
Brazil
Bhutan
Afganistan
UK
Nepal
Newszealand
32
Bangladesh
Ricky
3
Australia
Europe
Germany
42
UK
Dravid
2
India
Bhutan
39
Pakistan

Australia

Sample Output1-
2
Saurav

Sample Input2-
5
anchal
3
a
b
c
21
a
aman
4
a
b
c
d
22
b
prachi
2
a
d
21
c
monika
1
d
44
d
brij
5
a
b
d
f
g
45
e

d

Sample Output2-
4
brij

Sample Input3-
6
anchal
3
a
b
c
21
a
aman
4
a
b
c
d
22
b
prachi
2
a
d
21
c
monika
1
d
44
d
brij
5
a
b
d
f
g
45
e
mayur
5
a
b
z
f
g
21
x

d

Sample Output3-
4
brij
'''

class Traveler:

    def __init__(self,travelerName,traveledCountry,travelerAge,countryFrom):
        self.travelerName = travelerName
        self.traveledCountry = traveledCountry
        self.travelerAge = travelerAge
        self.countryFrom = countryFrom

class TravelAgency:

    @classmethod
    def countTravelersTraveledCountry(cls,list_obj,find_country):

        counter=0
        for i in list_obj:
            if find_country in i.traveledCountry:
                counter+=1
        return counter

    @classmethod
    def getTravelerTravelledMax(cls,list_obj):
        max_con=0
        max_name=''
        for i in list_obj:
            list1=i.traveledCountry
            if max_con<len(list1):
                max_con=len(list1)
                max_name=i.travelerName
        return max_name



n=int(input())
list_obj=[]
for i in range(n):
    travelerName = input()
    c=int(input())
    traveledCountry = []
    for j in range(c):
        traveledCountry.append(input())
    travelerAge = int(input())
    countryFrom = input()

    list_obj.append(Traveler(travelerName,traveledCountry,travelerAge,countryFrom))

find_country = input()

answer1=TravelAgency.countTravelersTraveledCountry(list_obj,find_country)

answer2=TravelAgency.getTravelerTravelledMax(list_obj)

print(answer1)
print(answer2)

