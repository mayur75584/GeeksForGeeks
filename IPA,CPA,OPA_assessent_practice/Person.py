'''
Screenshots of question Person is taken in Mobile
'''
'''
Input-
5
Rajesh
5
50
Suman
4
89
gopi
5
9
Radhika
6
120
Rajesh
5
120

Output-
The Average height is: 5.0
Persons taller than the Average height
Radhika
'''

class Person:

    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

class Society:

    def __init__(self,personList):
        self.personList = personList

    def findAverageHeight(self):
        avg=0
        sum1=0
        count1=0
        for i in self.personList:
            sum1+=i.height
            count1+=1
        avg=sum1/count1
        return avg
    def findTallerThanAgeratePerson(self):
        avg=self.findAverageHeight()
        result=[]
        for i in self.personList:
            if i.height>avg:
                result.append(i.name)
        return result




if __name__ == '__main__':
    n=int(input())
    list_obj = []
    for i in range(n):
        name = input()
        height = int(input())
        weight = int(input())
        p=Person(name,height,weight)
        list_obj.append(p)
    s=Society(list_obj)
    answer1=s.findAverageHeight()
    answer2=s.findTallerThanAgeratePerson()
    print("The Average height is:",answer1)
    print("Persons taller than the Average height")
    for i in answer2:
        print(i)

