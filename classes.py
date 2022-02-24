from msilib.schema import Class
from typing_extensions import Self


class Student:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.marks=[]
    def average(self):
        return sum(self.marks)/len(self.marks)
vero=Student("Veronica","IUIU")
vero.marks.append(35)
vero.marks.append(75)
vero.marks.append(95)
#print(vero.average())
    #EXERCISE

class Store:
    def __init__(self,name,item):
        self.name=name
        self.item=[]
    def add_item(self,name,price):
        items={'name':'name','price':'price'}
        self.item.append(self.item)

    items_list=add_item("LongDress",900)
    print(Self.item)