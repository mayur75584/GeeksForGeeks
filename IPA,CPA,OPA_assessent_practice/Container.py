'''
'Both Sample Inputs are wrong as full sample input is not available'
'Screenshot of this question is taken in mobile.
Input - 1

4
101
2
2
200
102
3
3
3
120
103
1
2
1
50
104
2
5
1
100
200

Output - 1:
No Container Found
102 27

Input - 2:
5
101
3
4
5
120
102
15
130
103
4
100
104
7
7
7
100
105
40
103

Output - 2:
6000
105 512
'''

class Container:

    def __init__(self,id,length,breadth,height,price_PerSqFt):
        self.id = id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.price_PerSqFt = price_PerSqFt

    def find_Volume(self):
        v=(self.length*self.breadth*self.height)
        return v

class Packaging_Company:
    def __init__(self,container_List):
        self.container_List = container_List

    def find_ContainerCost(self,ans_id):
        for i in self.container_List:
            if i.id == ans_id:
                z=i.find_Volume()
                result=z*i.price_PerSqFt
                return result
        else:
            return None

    def findLargestContainer(self):
        result=[]
        for i in self.container_List:
            z=i.find_Volume()
            result.append(z)
        max1=max(result)
        result2=[]
        for i in self.container_List:
            if max1==i.find_Volume():
                result2.append(i.id)
                result2.append(i.find_Volume())
        return result2



if __name__ == '__main__':
    n=int(input())
    list_obj = []
    for i in range(n):
        id=int(input())
        length=int(input())
        breadth=int(input())
        height=int(input())
        price_PerSqFt=int(input())
        c=Container(id,length,breadth,height,price_PerSqFt)
        list_obj.append(c)
    p=Packaging_Company(list_obj)
    ans_id=int(input())
    answer1=p.find_ContainerCost(ans_id)
    answer2=p.findLargestContainer()
    if answer1==None:
        print("No Container Found")
    else:
        print(answer1)
    for i in answer2:
        print(i,end=' ')




