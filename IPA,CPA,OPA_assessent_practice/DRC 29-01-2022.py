'''
Create a class Volcano with below attributes
volcanoName:(string type)
country:(string type)
elevation:(number type)
areaInKmSq:(number type)
lastEruptionYear:(number type)

Define the __init__ method which takes parameters in above sequence and sets the values for
attributes volcanoName,country,elevation,areaInKmSq and lastEruptionYear.

Create another class Eruption with attributes as below:
volcanoList a List of Volcano Objects

Define two methods in this class as below:

findVolcanoByCountry: The method takes list of volcano objects and country as the argument
and returns the list of volcano objects whose country matches with the country passed as an argument.

If no volcano fulfilling the conditions mentioned is found,
then the method should return None.

getVolcanoCategorization: The method will take takes a list of Volcano objects and volcanoName
as parameter and return the status of the Volcano for the given name passed as argument from the
volcanoList in the Eruption class.

The status is calculated based on below categorization:
IF the volcano has not erupted for 1 to 25 years, status should be
'High probability'.
If the volcano has not erupted for 25 to 50 years, status should be 'Low probability'
If the volcano is currently in erruption state, status should be 'Active'
otherwise should be 'Inactive'.
If no volcano with given name is found in the volcanoList, the
method should return None.

Note: All search should be case insensitive
Assume the current year as 2021

Instruvtions to write main function
a) You should require to write the main section completely,
hence please follow the below instructions for the same.
b) You would require to write the main program which is
inline to the "sample input descripton section" mentioned
below and to read the data in same sequence.
c) Create the respective objects (Volcano and Eruption) with
the given sequence of the arguments to fulfill the
__init__ method requirement defined in the respective classes
referring to the below instructions.

. Create a list of Volcano. To create the list
1- First read the number of volcano you want to store
in the list.
2- Read the values for the volcano, create the Volcano object and add to
the list. This point repeates for the number of Volcano
objects(consider the input taken in point 1 obove) to be created.
a) First read the name of volcano.
b) Then read the country,elevtion,areaInKmSq and lastEruptionYear.
c)Finally read the values for country and volcano name to be passed as argument to the method
findVolcanoByCountry and getVolcanoCategorization respectively.
d)Call the method findVolcanoByCountry mentuoned above
from the main section
e)Display the volcanoName,country and lastEruptionYear of
the volcano returned by the method. You may refer to the sample
output for the display format. If None is returned by the method, then display the message
"No Matching records found"(excluding quotes).
f)Call the methid getVolcanoCategorization mentioned above
from the main section.
g)Display the status of the volcano returned by the method.
You may refer to the sample output for the display format. If method returns None, then isplay the
,essage "No Volcano is avaiable with the given name"(excluding quotes).

You can use/refer the below given sample input and output for more details of the format for input and
output.

Sample Input description.
a) First line represents the inetger value which represents
the number of Volcano objects.
b)Next lines of input represents one volcano specific data as below
one by one in each line.

volcanoName
country
elevation
areaInKmSq
lastEruptionYear

c)The point b repeats for the number of objects mentioned in the point a.
d)The next line of input is the name of the country to be
passed as argument to the method
findVolcanoByCountry
e)The last line of input is the name of the volcano to be
passe as argument to the method getVolcanoCategorization.

Sample Input1:
5
Mauna Loa
United States
4169
5271
1984
Mount Etna
Italy
3350
190
2021
Mount Merapi
Indonesia
2930
1356
2020
Mount Vesuvius
Italy
1281
1232
1944
Mount Pinatubo
Philippine
1486
1486
1991
Italy
Mount Etna

Output:
Mount Etna
Italy
2021
Mount Vesuvius
Italy
1944
Active

Sample Input 2:
5
Mauna Loa
United States
4169
5271
1984
Mount Etna
Italy
3350
1190
2021
Mount Merapi
Indonesia
2930
1356
2020
Mount Vesuvius
Italy
1281
1232
1944
Mount Pinatubo
Philippine
1486
1486
1991
Japan
Mount Fauji

Output:
No Matching records found.
No Volcano is available with the given name
'''
'Dont know whether the solution is correct or not as it was DRC question'

class Volcano:
    def __init__(self,VolcanoName,country,elevation,areaInKmSq,lastEruptionYear):
        self.VolcanoName = VolcanoName
        self.country = country
        self.elevation = elevation
        self.areaInKmSq = areaInKmSq
        self.lastEruptionYear = lastEruptionYear
class Eruption:
    def __init__(self,volcanoList):
        self.volcanoList = volcanoList
    def findVolcanoByCountry(self,volcanoList,Country1):
        lst=[]
        for i in volcanoList:
            if i.country.lower()==Country1.lower():
                lst.append(i)
        if len(lst)!=0:
            return lst
        else:
            return None
    def getVolcanoCategorization(self,volcanoList,VolcanoName1):
        for i in volcanoList:
            if i.VolcanoName.lower()==VolcanoName1.lower():
                x=i.lastEruptionYear
                if x==2021:
                    return 'Active'
                elif 1<=(2021-x)<=25:
                    return 'High Probability'
                elif 25<=(2021-x)<=50:
                    return 'Low Probability'
                else:
                    return 'Inactive'
        return None


if __name__ == '__main__':
    n=int(input())
    lst_obj=[]
    for i in range(n):
        VolcanoName = input()
        country = input()
        elevation = int(input())
        areaInKmSq = int(input())
        lastEruptionYear = int(input())
        lst_obj.append(Volcano(VolcanoName,country,elevation,areaInKmSq,lastEruptionYear))
    Country1=input()
    VolcanoName1=input()
    eruption=Eruption(lst_obj)
    ans1=eruption.findVolcanoByCountry(lst_obj,Country1)
    ans2=eruption.getVolcanoCategorization(lst_obj,VolcanoName1)
    if ans1==None:
        print('No matching records found')
    else:
        for i in ans1:
            print(i.VolcanoName)
            print(i.country)
            print(i.lastEruptionYear)
    if ans2==None:
        print('No Volcano is available with given name')
    else:
        print(ans2)




