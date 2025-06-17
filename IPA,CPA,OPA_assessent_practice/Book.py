'''
Question number 6 from IPA Sample Questions

Sample Input1-
3
100
C++ Programming
200
Introduction to SQL
300
Core Java

C
3
Odyssey
Core Java
Hello World

Sample Output1-
2
C++ Programming
Introduction to SQL

Sample Input2-
3
200
RS Agrawal
300
abc
400
xyz

R
3
RS Agrawal
abc
lmn

Sample Output2-
1
xyz

'''



class Book:

    def __init__(self,book_id,book_name):
        self.book_id = book_id
        self.book_name = book_name

class Library:

    def __init__(self,library_id,address,book_list):
        self.library_id = library_id
        self.address = address
        self.book_list = book_list

    def count_books(self,char):
        counter=0
        'Logic 1'
        for i in self.book_list:
            x=i.book_name
            if x[0]==char:
                counter+=1
        return counter
        'Logic 2'
        # for i in self.book_list:
        #     if i.book_name.startswith(char)==True:
        #         counter+=1
        # return counter

    def remove_books(self,names):
        'Logic 1'
        for j in names:#For comparing between two list always use two loops to avoid error
            for k in self.book_list:
                if k.book_name==j:
                    self.book_list.remove(k)#Here only k becuase if we give k.book_name it will throw error so its better to delete entire object

        'Logic 2 is wrong logic'
        # for j in self.book_list:
        #     if j.book_name in names:
        #         self.book_list.remove(j.book_name)




if __name__ == '__main__':
    n=int(input())
    list_obj=[]
    for i in range(n):
        book_id = int(input())
        book_name = input()
        list_obj.append(Book(book_id,book_name))

    char=input()
    c=int(input())
    names=[]
    for j in range(c):
        names.append(input())

    l=Library(123,"Mumbai",list_obj)
    # answer1=Library.count_books(char)
    # answer2=Library.remove_books(names)
    print(l.count_books(char))
    l.remove_books(names)
    for i in l.book_list:
        print(i.book_name)




